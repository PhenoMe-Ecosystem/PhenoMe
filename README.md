<div align="center">
  <img src="docs/assets/logo.png" alt="PhenoMe logo" width="360"/>
  <p>A modular, <b>dataset-agnostic</b> and <b>model-agnostic</b> framework for phenotyping analysis, combining deep learning embeddings and image properties.</p>
</div>

---

### 🗺️ Navigation

**[✨ Features](#-features)** | **[🚀 Quick Start](#-quick-start)** | **[📦 Installation](#-installation)** | **[📄 Paper reproducibility](#-paper-reproducibility)** | **[📖 Documentation](https://phenome-ecosystem.github.io/PhenoMe/)** | **[📜 Citation](#-citation)**

---

<div align="center">
    <video src="https://github.com/user-attachments/assets/644e18f6-02a7-4700-bec2-9fcf11bde3c6"></video>
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

## 📜 Citation

If you use PhenoMe in your research, please cite:

```bibtex
@software{phenome,
  author = {Aitor González-Marfil},
  title = {PhenoMe: Interactive AI framework for image representation analysis},
  year = {2026},
  url = {https://github.com/PhenoMe-Ecosystem/PhenoMe}
}
```
