# STED-FM example helpers

Scripts used by [`sted_fm_synaptic_proteins.ipynb`](../sted_fm_synaptic_proteins.ipynb). They download the NAS, Optim, Zooniverse, and actin STED datasets and write each one in the folder layout PhenoMe expects: `images/`, optional `masks/`, and `metadata.csv`.

These scripts are not part of the `phenome` package. The notebook adds `Notebooks/examples` to `sys.path` and imports `download_dataset` and `transform_dataset` from this folder.

NAS and Optim are read with loaders from [STED-FM](https://github.com/FLClab/STED-FM). Install that package, and `requests`, in the same environment before running the notebook. The notebook has the install commands.
