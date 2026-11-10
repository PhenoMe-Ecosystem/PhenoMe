<div align="center">
  <img src="docs/assets/logo.png" alt="PhenoMe logo" width="360"/>
  <p>A modular, <b>dataset-agnostic</b> and <b>model-agnostic</b> framework for phenotyping analysis, combining deep learning embeddings and image properties.</p>
    <p>
    <a href="https://pypi.org/project/phenome/"><img alt="PyPI" src="https://img.shields.io/pypi/v/phenome?label=PyPI"></a>
    <a href="https://phenome-ecosystem.github.io/PhenoMe/getting-started/"><img alt="Python 3.12+" src="https://img.shields.io/badge/python-3.12%2B-3776AB"></a>
    <a href="https://phenome-ecosystem.github.io/PhenoMe/"><img alt="Documentation" src="https://img.shields.io/badge/docs-website-blue"></a>
    <a href="https://napari-hub.org/plugins/phenome-gui"><img alt="napari hub" src="https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/phenome-gui"></a>
    <a href="https://doi.org/10.64898/2026.10.29.762637"><img alt="bioRxiv preprint" src="https://img.shields.io/badge/bioRxiv-preprint-b31b1b"></a>
    <a href="https://github.com/PhenoMe-Ecosystem/PhenoMe/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-green"></a>
  </p>
</div>

---

### 🗺️ Navigation

**[✨ Features](#-features)** | **[🚀 Quick Start](#-quick-start)** | **[📦 Installation](#-installation)** | **[📄 Paper reproducibility](#-paper-reproducibility)** | **[📖 Documentation](https://phenome-ecosystem.github.io/PhenoMe/)** | **[📜 Citation](#-publication)**

---

<div align="center">
    <video src="https://github.com/user-attachments/assets/690cd235-8188-425b-b270-4dfdc869f758"></video>
</div>

---

## ✨ Features

- 🧠 **Model Agnostic**: Extract embeddings using DINOv2 or any custom vision model (PyTorch, TensorFlow, Keras, etc.).
- 📂 **Dataset Agnostic**: Works with any image dataset structure with customizable metadata extraction.
- 🛠️ **Analysis Toolkit**: Distance quantification, anomaly detection, property extraction, and correlation analysis.
- 📊 **Interactive Visualizations**: High-performance Plotly-based PCA, t-SNE, and UMAP plots.
- 📑 **Automated Reporting**: Generate comprehensive standalone HTML reports.

---

## 🚀 Quick Start

Try the no-code experience with the **[Interactive Quickstart Notebook](Notebooks/tutorials/01_interactive_quickstart.ipynb)** or launch instantly in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PhenoMe-Ecosystem/PhenoMe/blob/main/Notebooks/tutorials/01_interactive_quickstart.ipynb)

---

## 📦 Installation

### Create a conda environment

1. Open the terminal and clone the repository with git. 

```bash
git clone https://github.com/PhenoMe-Ecosystem/PhenoMe.git
cd PhenoMe
```
If you don't have git installed, please download this GitHub repository, unzip the folder and open a terminal window already pointing to the PhenoMe folder containing this code (right-click on the folder and choose "New Terminal at Folder").

2. Create a conda environment from the terminal:

**GPU**
```bash
conda env create -f envs/environment-gpu.yml
conda activate phenome-gpu
```
PyTorch is included. An NVIDIA GPU is used when CUDA is available; the same install runs on CPU.


**CPU**
```bash
conda env create -f envs/environment-cpu.yml
conda activate phenome-cpu
```
### Install PhenoMe directly from pip within an existing environment

Using the terminal, install the package:

```bash
pip install phenome
```

PyTorch and the Jupyter packages used by the notebooks are included.

> **💡 Full instructions, verification, and troubleshooting:**
> See the [Getting started](https://phenome-ecosystem.github.io/PhenoMe/getting-started/) guide for install details, verification commands, and first-analysis walkthroughs.

---

## 📄 Paper reproducibility

To reproduce the analyses in the paper, check out the [Paper reproducibility](https://phenome-ecosystem.github.io/PhenoMe/paper-reproducibility/) guide.

---

## 📖 Documentation

**Explore the [Full Documentation](https://phenome-ecosystem.github.io/PhenoMe/)** for detailed guides, API references, and tutorials.

| Step | Resource |
| ---- | -------- |
| 1️⃣ **Install** | [Getting started](https://phenome-ecosystem.github.io/PhenoMe/getting-started/) |
| 2️⃣ **Set up your data** | [Data setup](https://phenome-ecosystem.github.io/PhenoMe/guides/data-setup/) · [Experiment details](https://phenome-ecosystem.github.io/PhenoMe/guides/experiment-details/) |
| 3️⃣ **Tutorials** | [Notebooks/tutorials/](Notebooks/tutorials/) |
| 4️⃣ **Examples** | [Notebooks/examples/](Notebooks/examples/) |

**Learn More:** [Core concepts](https://phenome-ecosystem.github.io/PhenoMe/concepts/) · [Workflows](https://phenome-ecosystem.github.io/PhenoMe/workflows/) · [FAQ](https://phenome-ecosystem.github.io/PhenoMe/faq/) · [Glossary](https://phenome-ecosystem.github.io/PhenoMe/glossary/)

Coding agents must read and follow [AGENTS.md](AGENTS.md) before writing code.

---

## 📜 Publication

[<img width="1084" height="545" alt="Screenshot 2026-11-05 at 15 17 53" src="https://github.com/user-attachments/assets/e4c932f2-d88c-4d4c-988a-777a55770474" />](https://www.biorxiv.org/content/10.64898/2026.10.29.762637v1)

If you use PhenoMe, please cite our work:

```bibtex
@article{Gonzalez-Marfil2026phenome,
  author = {González-Marfil, Aitor and Backová, Lenka and Bernatchez, Renaud and Hidalgo-Cenalmor, Iván and Dufour, Antoine and Jacquemet, Guillaume and Lavoie-Cardinal, Flavie and Arganda-Carreras, Ignacio and Gómez-de-Mariscal, Estibaliz},
  title = {PhenoMe: An interactive AI framework for interpretable, microscopy-driven phenotyping},
  journal = {bioRxiv},
  year = {2026},
  publisher = {Cold Spring Harbor Laboratory},
  doi = {10.64898/2026.10.29.762637},
  url = {https://doi.org/10.64898/2026.10.29.762637}
}
```


