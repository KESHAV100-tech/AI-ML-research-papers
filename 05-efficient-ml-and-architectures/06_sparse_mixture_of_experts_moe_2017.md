# Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

<div align="center">

[![Year](https://img.shields.io/badge/Year-2017-blue?style=for-the-badge)](https://arxiv.org/abs/1701.06538)
[![Venue](https://img.shields.io/badge/Venue-ICLR%202017-purple?style=for-the-badge)](https://arxiv.org/abs/1701.06538)
[![arXiv](https://img.shields.io/badge/arXiv-1701.06538-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1701.06538)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/1701.06538.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tensorflow/tensor2tensor)

</div>

---

### 📋 Paper Metadata

- **Authors:** Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean
- **Publication Year:** 2017
- **Venue:** ICLR 2017
- **Primary arXiv ID:** [`arXiv:1701.06538`](https://arxiv.org/abs/1701.06538)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/1701.06538.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/tensorflow/tensor2tensor)

---

### 📖 Executive Abstract

> "The capacity of a neural network to absorb information is limited by its number of parameters. In this work, we address this limitation by introducing a Sparsely-Gated Mixture-of-Experts Layer, realizing over 1000x improvements in model capacity with only minor increases in computational cost."

---

### 🎯 Core Problem & Motivation

Dense networks activate all parameters for every input token, forcing a strict trade-off where increasing parameter capacity dramatically inflates compute FLOPs.

---

### 💡 Key Innovations & Architecture

1. **Sparsely-Gated MoE**: Introduced thousands of feed-forward expert subnetworks, activating only a small chosen subset ($k \ll n$) per token.
2. **Noisy Top-K Gating**: Injected Gaussian noise into gating logits to ensure balanced expert utilization and continuous exploration.
3. **Sub-linear Scaling**: Scaled model capacity past 137 billion parameters on language translation benchmarks with sub-linear compute overhead.

---

### 📐 Mathematical Formulation

**Noisy Top-K Gating Formulation:**
$$G(x) = \text{Softmax}(\text{KeepTopK}(H(x), k))$$
$$H(x)_i = (x \cdot W_g)_i + \text{StandardNormal}() \cdot \text{Softplus}((x \cdot W_{\text{noise}})_i)$$

---

### 🌟 Significance & Industry Impact

Pioneered conditional computation in modern deep learning, serving as the direct intellectual predecessor to Switch Transformer, Mixtral, and DeepSeek-V3.

---

### 📚 BibTeX Citation

```bibtex
@article{06_sparse_mixture_of_experts_moe_2017,
  title = {Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer},
  author = {Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean},
  journal = {arXiv preprint arXiv:1701.06538},
  year = {2017},
  url = {https://arxiv.org/abs/1701.06538}
}
```
