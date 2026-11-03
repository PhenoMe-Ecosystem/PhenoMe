---
title: "Paper reproducibility"
description: Conda environments for regenerating the analyses in the paper. Separate from the pip install.
sidebar:
  order: 2
---

The analyses in the paper were run with Python 3.12 and PyTorch 2.12, and with `PhenoMe(seed=42)`. Those versions are the conda environments in this repository, not the pip install.

GPU, which is the setup used for those analyses:

```bash
git clone https://github.com/PhenoMe-Ecosystem/PhenoMe.git
cd PhenoMe
conda env create -f envs/environment-gpu.yml
conda activate phenome-gpu
```

The same PyTorch pin on CPU:

```bash
conda env create -f envs/environment-cpu.yml
conda activate phenome-cpu
```

The notebooks used for the analyses, were you can reproduce the figures are in `Notebooks/examples/`.
