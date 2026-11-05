# Scalable Diffusion Models with Transformers (DiT)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2212.09748)
[![Venue](https://img.shields.io/badge/Venue-ICCV%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2212.09748)
[![arXiv](https://img.shields.io/badge/arXiv-2212.09748-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2212.09748)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2212.09748.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/facebookresearch/DiT)

</div>

---

### 📋 Paper Metadata

- **Authors:** William Peebles, Saining Xie
- **Publication Year:** 2022
- **Venue:** ICCV 2023
- **Primary arXiv ID:** [`arXiv:2212.09748`](https://arxiv.org/abs/2212.09748)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2212.09748.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/facebookresearch/DiT)

---

### 📖 Executive Abstract

> "We explore a new class of diffusion models based on the Transformer architecture. We train Diffusion Transformers (DiTs), backing out the commonly-used U-Net backbone in favor of a transformer that operates on latent patches. We analyze the scalability of our DiTs through the lens of forward pass compute and FID."

---

### 🎯 Core Problem & Motivation

Standard diffusion models relied almost exclusively on convolutional U-Net backbones, which had complex downsampling/upsampling architectures and unknown scaling properties with compute.

---

### 💡 Key Innovations & Architecture

1. **U-Net Replacement**: Completely replaced U-Nets with a standard ViT-style Transformer operating on spatial latent patches.
2. **Adaptive Layer Normalization (adaLN-Zero)**: Injected time-step $t$ and class label conditioning via scale and shift parameters initialized to zero.
3. **Predictable Scaling Laws**: Proved that higher model capacity and smaller patch sizes correlate monotonically with improved FID score.

---

### 📐 Mathematical Formulation

**Adaptive Layer Normalization (adaLN-Zero):**
$$\text{adaLN}(h, y) = \gamma(y) \odot \left( \frac{h - \mu}{\sigma} \right) + \beta(y)$$
Modulation parameters $\gamma, \beta, \alpha$ are regressed from the sum of time-step and conditioning embeddings.

---

### 🌟 Significance & Industry Impact

DiT proved that Transformers scale gracefully in generative vision just as in NLP. It became the core architecture behind OpenAI's **Sora** video generation model and Stable Diffusion 3.

---

### 📚 BibTeX Citation

```bibtex
@article{05_diffusion_transformer_dit_2022,
  title = {Scalable Diffusion Models with Transformers (DiT)},
  author = {William Peebles, Saining Xie},
  journal = {arXiv preprint arXiv:2212.09748},
  year = {2022},
  url = {https://arxiv.org/abs/2212.09748}
}
```
