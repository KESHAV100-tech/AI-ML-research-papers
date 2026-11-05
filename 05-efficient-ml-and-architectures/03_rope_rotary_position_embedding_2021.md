# RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2021-blue?style=for-the-badge)](https://arxiv.org/abs/2104.09864)
[![Venue](https://img.shields.io/badge/Venue-Neurocomputing%202024-purple?style=for-the-badge)](https://arxiv.org/abs/2104.09864)
[![arXiv](https://img.shields.io/badge/arXiv-2104.09864-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2104.09864)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2104.09864.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ZhuiyiTechnology/roformer)

</div>

---

### 📋 Paper Metadata

- **Authors:** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu
- **Publication Year:** 2021
- **Venue:** Neurocomputing 2024
- **Primary arXiv ID:** [`arXiv:2104.09864`](https://arxiv.org/abs/2104.09864)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2104.09864.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/ZhuiyiTechnology/roformer)

---

### 📖 Executive Abstract

> "Positional information is important in sequence modeling. In this work, we propose Rotary Position Embedding (RoPE) to effectively leverage positional information. Specifically, RoPE encodes the absolute position with a rotation matrix and naturally incorporates explicit relative position dependency in self-attention formulation."

---

### 🎯 Core Problem & Motivation

Absolute sinusoidal positional embeddings do not generalize well to sequences longer than those seen in training, while relative position embeddings added computational complexity to self-attention.

---

### 💡 Key Innovations & Architecture

1. **Rotary Multiplier**: Multiplies query and key representations by orthogonal 2D rotation matrices based on position index $m$.
2. **Inner Product Preservation**: The inner product $\langle R_m q, R_n k \rangle$ depends solely on the relative difference $m - n$.
3. **Length Extrapolation**: Seamlessly extends to longer context lengths via interpolation techniques (YaRN, RoPE frequency scaling).

---

### 📐 Mathematical Formulation

**Rotary Matrix Operation:**
$$R_{\Theta, m}^d = \text{diag}\left( R_{\theta_1, m}, R_{\theta_2, m}, \dots, R_{\theta_{d/2}, m} \right)$$
$$\text{where } R_{\theta_i, m} = \begin{pmatrix} \cos(m \theta_i) & -\sin(m \theta_i) \\ \sin(m \theta_i) & \cos(m \theta_i) \end{pmatrix}$$

---

### 🌟 Significance & Industry Impact

Adopted by virtually every modern frontier LLM (Llama, Mistral, Gemma, DeepSeek, Qwen) as the standard positional encoding architecture.

---

### 📚 BibTeX Citation

```bibtex
@article{03_rope_rotary_position_embedding_2021,
  title = {RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)},
  author = {Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu},
  journal = {arXiv preprint arXiv:2104.09864},
  year = {2021},
  url = {https://arxiv.org/abs/2104.09864}
}
```
