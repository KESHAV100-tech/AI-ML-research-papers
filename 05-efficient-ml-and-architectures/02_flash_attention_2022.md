# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2205.14135)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2205.14135)
[![arXiv](https://img.shields.io/badge/arXiv-2205.14135-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2205.14135)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2205.14135.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dao-AILab/flash-attention)

</div>

---

### 📋 Paper Metadata

- **Authors:** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré
- **Publication Year:** 2022
- **Venue:** NeurIPS 2022
- **Primary arXiv ID:** [`arXiv:2205.14135`](https://arxiv.org/abs/2205.14135)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2205.14135.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/Dao-AILab/flash-attention)

---

### 📖 Executive Abstract

> "Transformers are slow and memory-hungry on long sequences, as the time and memory complexity of self-attention are quadratic in sequence length. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU High Bandwidth Memory (HBM) and on-chip SRAM."

---

### 🎯 Core Problem & Motivation

Standard attention implementations materialize the full $N \times N$ attention matrix in GPU HBM, hitting a memory wall where execution is bottlenecked by memory transfer speeds rather than compute.

---

### 💡 Key Innovations & Architecture

1. **Tiling & Online Softmax**: Computes softmax incrementally across blocks of Query, Key, and Value without ever storing the full $N \times N$ attention matrix.
2. **Recomputation in Backward Pass**: Recomputes intermediate attention values on-chip during backpropagation rather than storing them from forward pass.
3. **Exact Output**: Unlike approximate attention methods, FlashAttention computes exact mathematical attention with 2-4x wall-clock speedup and linear $O(N)$ memory.

---

### 📐 Mathematical Formulation

**Online Softmax Algorithm:**
$$m(x) = \max(m(x^{(1)}), m(x^{(2)})), \quad d(x) = e^{m(x^{(1)}) - m(x)} d(x^{(1)}) + e^{m(x^{(2)}) - m(x)} d(x^{(2)})$$
$$\text{softmax}(x) = \frac{e^{x - m(x)}}{d(x)}$$

---

### 🌟 Significance & Industry Impact

FlashAttention is integrated into PyTorch, Hugging Face, vLLM, and Triton, becoming the universal execution backend enabling 32K, 128K, and 1M token contexts.

---

### 📚 BibTeX Citation

```bibtex
@article{02_flash_attention_2022,
  title = {FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness},
  author = {Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré},
  journal = {arXiv preprint arXiv:2205.14135},
  year = {2022},
  url = {https://arxiv.org/abs/2205.14135}
}
```
