# DeepSeek-V3 Technical Report

<div align="center">

[![Year](https://img.shields.io/badge/Year-2024-blue?style=for-the-badge)](https://arxiv.org/abs/2412.19437)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2412.19437)
[![arXiv](https://img.shields.io/badge/arXiv-2412.19437-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2412.19437)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2412.19437.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-V3)

</div>

---

### 📋 Paper Metadata

- **Authors:** DeepSeek-AI
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2412.19437`](https://arxiv.org/abs/2412.19437)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2412.19437.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/deepseek-ai/DeepSeek-V3)

---

### 📖 Executive Abstract

> "We present DeepSeek-V3, a strong Mixture-of-Experts language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, and achieves state-of-the-art performance trained for just $6 million USD."

---

### 🎯 Core Problem & Motivation

Serving multi-hundred-billion parameter models incurs unsustainable memory bandwidth overhead (KV cache bottleneck) and requires millions of GPU hours for training.

---

### 💡 Key Innovations & Architecture

1. **Multi-Head Latent Attention (MLA)**: Compresses key-value heads into a low-dimensional latent space, reducing KV cache memory by over 93%.
2. **DeepSeekMoE with Fine-Grained Experts**: Employs 256 routed experts + 1 shared expert with top-8 routing, allowing richer specialization.
3. **Auxiliary-Loss-Free Load Balancing**: Balanced expert load using dynamic bias adjustments rather than auxiliary routing losses that hurt model capability.
4. **FP8 Mixed Precision Framework**: End-to-end FP8 training and communication routines reducing memory traffic and training cost.

---

### 📐 Mathematical Formulation

**MLA Key-Value Low-Rank Compression:**
$$c_t^{KV} = W^{DKV} h_t \in \mathbb{R}^{d_c}$$
$$k_t^C = W^{UK} c_t^{KV}, \quad v_t^C = W^{UV} c_t^{KV}$$
During generation, only $c_t^{KV}$ needs to be cached rather than full keys and values!

---

### 🌟 Significance & Industry Impact

Shocked the global AI ecosystem by delivering frontier performance on par with proprietary commercial models at less than 1/10th of the training budget ($6M USD on 2,048 H800 GPUs).

---

### 📚 BibTeX Citation

```bibtex
@article{05_deepseek_v3_2024,
  title = {DeepSeek-V3 Technical Report},
  author = {DeepSeek-AI},
  journal = {arXiv preprint arXiv:2412.19437},
  year = {2024},
  url = {https://arxiv.org/abs/2412.19437}
}
```
