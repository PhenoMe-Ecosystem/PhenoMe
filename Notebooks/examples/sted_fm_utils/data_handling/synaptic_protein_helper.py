"""Shared helpers for cutting Zooniverse cluster crops.

Crops are taken from the full-resolution images in `dataset.images`, so recorded
coordinates stay in the original image.
"""

import os
import re

import numpy as np

# Mirrors SemanticProteinSegmentationDataset.classes (mask channel order)
CLASS_NAMES = ("round", "elongated", "perforated", "multidomains")

# R-Homer_GARSTAR635_M-PSD95_GAMAlexa594_GluGly_01.tif and the '-' separated variant
# R-Rim_GARSTAR635-M-Bassoon_GAMAlexa594_0MgGlyBic_02.tif
_IMAGE_NAME_PATTERN = re.compile(
    r"^R-(?P<protein_ch0>[^_-]+)_(?P<label_ch0>[^_-]+)[_-]"
    r"M-(?P<protein_ch1>[^_-]+)_(?P<label_ch1>[^_-]+)_"
    r"(?P<condition>[^_]+)_(?P<replicate>[^_.]+)"
)


def threshold_mask(mask, threshold=0.0):
    """Binarize a soft label mask.

    The label stacks built by `create_segmentation` accumulate the mean of the
    annotator votes, so any strictly positive pixel was annotated at least once.

    Args:
        mask: Array of any shape, e.g. (H, W) or (n_classes, H, W).
        threshold: Pixels strictly above this value are foreground.

    Returns:
        Boolean array with the same shape as `mask`.
    """
    return np.asarray(mask) > threshold


def extract_crop(array, window, fill=0):
    """Extract `window` from `array`, padding the part that falls outside.

    Args:
        array: 2D array to crop.
        window: (row0, col0, row1, col1). The stop bounds are exclusive.
        fill: Value used for the out-of-image padding.

    Returns:
        Array of shape (row1 - row0, col1 - col0) with the dtype of `array`.
    """
    row0, col0, row1, col1 = window
    height, width = array.shape

    src_row0, src_col0 = max(row0, 0), max(col0, 0)
    src_row1, src_col1 = min(row1, height), min(col1, width)

    crop = np.full((row1 - row0, col1 - col0), fill, dtype=array.dtype)
    if src_row0 < src_row1 and src_col0 < src_col1:
        crop[src_row0 - row0 : src_row1 - row0, src_col0 - col0 : src_col1 - col0] = array[
            src_row0:src_row1, src_col0:src_col1
        ]
    return crop


def parse_image_name(img_name):
    """Extract the experimental metadata encoded in an original image filename.

    Names follow `R-<protein>_<label>_M-<protein>_<label>_<condition>_<replicate>.tif`
    where R-/M- are the rabbit and mouse primary antibodies imaged in channel 0 and
    channel 1 respectively.

    Args:
        img_name: Original image name, with or without the `.tif` extension.

    Returns:
        Dict with 'protein_ch0', 'label_ch0', 'protein_ch1', 'label_ch1',
        'condition' and 'replicate', or an empty dict if the name does not match.
    """
    match = _IMAGE_NAME_PATTERN.match(os.path.splitext(img_name)[0])
    return match.groupdict() if match else {}


def match_annotation(annotations, img_name, channel, centroid, max_distance):
    """Find the per-object annotation record closest to `centroid`.

    `id_coord` in the dataset metadata is expressed in full-image coordinates (that
    is how `create_segmentation` slices it), so centroids can be matched directly.

    Args:
        annotations: Sequence of metadata dicts, e.g. `dataset.metadata`.
        img_name: Original image name to match on.
        channel: Image channel to match on.
        centroid: (row, col) of the object in full-image coordinates.
        max_distance: Maximum euclidean distance for a match, in pixels.

    Returns:
        Dict with 'cluster_id', 'class_majority', 'seg_majority',
        'class_agreement' (fraction of annotators voting the majority class) and
        'n_class_votes', or an empty dict when nothing is close enough.
    """
    candidates = [a for a in annotations if a["img_name"] == img_name and a["channel"] == channel]
    if not candidates:
        return {}

    coords = np.array([a["id_coord"] for a in candidates], dtype=float)
    distances = np.linalg.norm(coords - np.asarray(centroid, dtype=float), axis=1)
    best = int(np.argmin(distances))
    if distances[best] > max_distance:
        return {}

    annotation = candidates[best]
    votes = np.asarray(annotation["class_votes"], dtype=float)
    votes = votes[~np.isnan(votes)]
    majority = annotation["class_majority"]
    agreement = float(np.mean(votes == majority)) if votes.size else np.nan

    return {
        "cluster_id": annotation["cluster_id"],
        "class_majority": majority,
        "seg_majority": annotation["seg_majority"],
        "class_agreement": agreement,
        "n_class_votes": int(votes.size),
    }


def minmax_preprocessing_fn(image):
    """Per-crop min-max normalization to [0, 1], for PhenoMe's `preprocessing_fn`.

    Crops are stored as raw uint16 whose maxima sit far below the 16-bit range,
    while PhenoMe normalizes by the dtype scale. Pass this to
    `pheno.process_images(..., preprocessing_fn=minmax_preprocessing_fn)` to give
    the model and the intensity properties usable contrast.

    Args:
        image: Array of shape (H, W) or (H, W, C).

    Returns:
        float32 array of the same shape with values in [0, 1].
    """
    image = np.asarray(image, dtype=np.float32)
    minimum, maximum = float(image.min()), float(image.max())
    if maximum <= minimum:
        return np.zeros_like(image)
    return (image - minimum) / (maximum - minimum)


def _scale_image(image, intensity_mode, scale_percentile):
    """Apply `intensity_mode` to a full-resolution image channel before cropping."""
    if intensity_mode in ("raw", "crop_minmax"):
        # 'crop_minmax' is applied per crop by the caller
        return image
    if intensity_mode == "image_percentile":
        scale = np.percentile(image, scale_percentile)
        if scale <= 0:
            scale = max(float(image.max()), 1.0)
        return np.clip(image / scale, 0.0, 1.0).astype(np.float32)
    raise ValueError(
        f"intensity_mode must be 'raw', 'image_percentile' or 'crop_minmax', got: {intensity_mode}"
    )
