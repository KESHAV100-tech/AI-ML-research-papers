# Learning Transferable Visual Models From Natural Language Supervision (CLIP)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2021-blue?style=for-the-badge)](https://arxiv.org/abs/2103.00020)
[![Venue](https://img.shields.io/badge/Venue-ICML%202021-purple?style=for-the-badge)](https://arxiv.org/abs/2103.00020)
[![arXiv](https://img.shields.io/badge/arXiv-2103.00020-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2103.00020)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2103.00020.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/openai/CLIP)

</div>

---

### 📋 Paper Metadata

- **Authors:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever
- **Publication Year:** 2021
- **Venue:** ICML 2021
- **Primary arXiv ID:** [`arXiv:2103.00020`](https://arxiv.org/abs/2103.00020)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2103.00020.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/openai/CLIP)

---

### 📖 Executive Abstract

> "State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. In this work, we demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs."

---

### 🎯 Core Problem & Motivation

Visual recognition models were bound to fixed 1,000-class taxonomies (like ImageNet-1K), preventing them from recognizing novel objects or understanding open-world concepts.

---

### 💡 Key Innovations & Architecture

1. **Dual-Encoder Architecture**: Separate vision encoder (ResNet or ViT) and text encoder (Transformer) projecting into a shared multimodal latent space.
2. **Symmetric Contrastive Loss**: InfoNCE objective maximizing cosine similarity of $N$ correct (image, text) pairs while minimizing $N^2 - N$ incorrect pairs in a batch.
3. **Zero-Shot Classification**: Formulated zero-shot classification by computing cosine similarity between an image embedding and prompt embeddings like 'a photo of a {label}'.

---

### 📐 Mathematical Formulation

**Symmetric InfoNCE Loss:**
$$\mathcal{L} = \frac{1}{2} (\mathcal{L}_{\text{image}} + \mathcal{L}_{\text{text}})$$
$$\mathcal{L}_{\text{image}} = - \frac{1}{N} \sum_{i=1}^N \log \frac{\exp(\text{sim}(I_i, T_i) / \tau)}{\sum_{j=1}^N \exp(\text{sim}(I_i, T_j) / \tau)}$$

---

### 🌟 Significance & Industry Impact

Became the universal visual-semantic bridge across modern AI, serving as the text-image aligner for Stable Diffusion, DALL-E 2, Midjourney, and zero-shot search engines.

---

### 📚 BibTeX Citation

```bibtex
@article{01_clip_contrastive_vision_language_2021,
  title = {Learning Transferable Visual Models From Natural Language Supervision (CLIP)},
  author = {Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever},
  journal = {arXiv preprint arXiv:2103.00020},
  year = {2021},
  url = {https://arxiv.org/abs/2103.00020}
}
```
