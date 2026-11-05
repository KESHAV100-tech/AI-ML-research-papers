# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

<div align="center">

[![Year](https://img.shields.io/badge/Year-2023-blue?style=for-the-badge)](https://arxiv.org/abs/2312.00752)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2312.00752)
[![arXiv](https://img.shields.io/badge/arXiv-2312.00752-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.00752)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2312.00752.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/state-spaces/mamba)

</div>

---

### 📋 Paper Metadata

- **Authors:** Albert Gu, Tri Dao
- **Publication Year:** 2023
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2312.00752`](https://arxiv.org/abs/2312.00752)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2312.00752.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/state-spaces/mamba)

---

### 📖 Executive Abstract

> "Fundamental sequence models are dominated by the Transformer architecture, but they fail to scale linearly on long sequences due to quadratic attention. We introduce Mamba, a selective structured state space model (SSM) with a hardware-aware parallel algorithm that runs in linear time $O(N)$ and scales up to millions of tokens."

---

### 🎯 Core Problem & Motivation

Transformers suffer from $O(N^2)$ computational complexity and unbounded KV cache memory growth during autoregressive generation, limiting real-time long-context deployment.

---

### 💡 Key Innovations & Architecture

1. **Selective State Spaces**: Made SSM parameters $B, C, \Delta$ input-dependent functions, allowing the model to selectively remember or filter out information based on the current token.
2. **Hardware-Aware Parallel Scan**: Overcame recurrence sequential bottlenecks by fusing state transitions into GPU SRAM using associative parallel prefix scans.
3. **Linear Time & Constant Memory**: Operates in $O(N)$ time with $O(1)$ memory per step during autoregressive inference while matching Transformer quality.

---

### 📐 Mathematical Formulation

**Continuous State Space Model:**
$$h'(t) = A h(t) + B x(t), \quad y(t) = C h(t)$$
**Discretized Selective Scan:**
$$\bar{A} = \exp(\Delta A), \quad \bar{B} = (\Delta A)^{-1}(\exp(\Delta A) - I) \cdot \Delta B$$
$$h_t = \bar{A}_t h_{t-1} + \bar{B}_t x_t, \quad y_t = C_t h_t$$

---

### 🌟 Significance & Industry Impact

Proved that non-attention architectures could match Transformers at scale, inaugurating hybrid SSM-Transformer architectures and linear-time sequence modeling.

---

### 📚 BibTeX Citation

```bibtex
@article{04_mamba_selective_state_spaces_2023,
  title = {Mamba: Linear-Time Sequence Modeling with Selective State Spaces},
  author = {Albert Gu, Tri Dao},
  journal = {arXiv preprint arXiv:2312.00752},
  year = {2023},
  url = {https://arxiv.org/abs/2312.00752}
}
```
