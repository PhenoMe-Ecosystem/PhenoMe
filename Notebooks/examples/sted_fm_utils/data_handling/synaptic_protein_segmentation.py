"""Load the Zooniverse synaptic-protein HDF5 file into full images and label stacks.

`export_cluster_crops` reads `images` and `metadata` from this object. It does not
iterate tiles, so this class only builds those two attributes.
"""

import json

import h5py
import numpy
from tqdm import tqdm


class SemanticProteinSegmentationDataset:
    """Full-resolution images and per-cluster label stacks from the Zooniverse HDF5 file."""

    ROUND = 0
    ELONGATED = 1
    PERFORATED = 2
    MULTIDOMAINS = 3

    def __init__(self, h5file: str) -> None:
        """Load original images and paint each annotation onto its label stack.

        Args:
            h5file: Path to the HDF5 file holding 'original_images', 'masks' and 'labels'.
        """
        self.h5file = h5file
        self.classes = ["round", "elongated", "perforated", "multidomains"]

        with h5py.File(self.h5file, "r") as file:
            valid_indices = []
            for c in self.classes:
                indices = (
                    numpy.argwhere(file["labels"][()].ravel() == getattr(self, c.upper()))
                    .ravel()
                    .tolist()
                )
                valid_indices.extend(indices)

            metadata = file["crops"].attrs["metadata"]
            metadata = json.loads(metadata)
            for i in range(len(metadata)):
                metadata[i]["idx"] = i
            self.metadata = [metadata[idx] for idx in valid_indices]

            self.images = {
                key: {
                    "image": value[()],
                    "label": numpy.zeros(
                        (value.shape[0], len(self.classes), value.shape[1], value.shape[2]),
                        dtype=numpy.float32,
                    ),
                }
                for key, value in file["original_images"].items()
            }

        self.create_segmentation()

    def create_segmentation(self):
        for i, metadata in enumerate(tqdm(self.metadata)):
            label = metadata["class_majority"]

            idx = metadata["idx"]
            with h5py.File(self.h5file, "r") as file:
                mask = file["masks"][idx][()]

            votes = numpy.array(metadata["seg_votes"])
            votes = votes[votes < len(mask)]
            masks = mask[votes]
            if len(votes) < 1:
                continue
            mask = numpy.mean(masks, axis=0)
            mask = mask.astype(numpy.float32)

            image = self.images[metadata["img_name"]]["label"][metadata["channel"]][0]
            coord = metadata["id_coord"]
            slc = tuple(
                slice(max(0, coord[i] - 40), min(coord[i] + 40, image.shape[i]))
                for i in range(len(coord))
            )
            self.images[metadata["img_name"]]["label"][metadata["channel"]][label][slc] += mask
