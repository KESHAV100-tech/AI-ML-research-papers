# Attention Is All You Need (Transformer)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2017-blue?style=for-the-badge)](https://arxiv.org/abs/1706.03762)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202017-purple?style=for-the-badge)](https://arxiv.org/abs/1706.03762)
[![arXiv](https://img.shields.io/badge/arXiv-1706.03762-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1706.03762)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/1706.03762.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tensorflow/tensor2tensor)

</div>

---

### 📋 Paper Metadata

- **Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
- **Publication Year:** 2017
- **Venue:** NeurIPS 2017
- **Primary arXiv ID:** [`arXiv:1706.03762`](https://arxiv.org/abs/1706.03762)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/1706.03762.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/tensorflow/tensor2tensor)

---

### 📖 Executive Abstract

> "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."

---

### 🎯 Core Problem & Motivation

Recurrent neural networks (RNNs, LSTMs, GRUs) process tokens sequentially, creating an inherently non-parallelizable bottleneck ($O(N)$ sequential operations) and struggling with long-range dependency retention due to gradient decay.

---

### 💡 Key Innovations & Architecture

1. **Self-Attention Mechanism**: Direct $O(1)$ path length between any two tokens in a sequence regardless of distance.
2. **Multi-Head Attention**: Allows the model to jointly attend to information from different representation subspaces at different positions.
3. **Fully Parallelizable Training**: Entire sequences are processed simultaneously in matrix multiplications on GPUs/TPUs.
4. **Positional Encodings**: Injected sinusoids into embeddings to supply token order information.

---

### 📐 Mathematical Formulation

**Scaled Dot-Product Attention:**
$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$$

**Multi-Head Attention:**
$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W^O$$
$$\text{where } \text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$

---

### 🌟 Significance & Industry Impact

The Transformer is arguably the most influential AI architecture of the 21st century. It obsoleted recurrent models in NLP and became the universal backbone for GPT, BERT, Claude, Gemini, LLaMA, ViT, AlphaFold, and Sora.

---

### 📚 BibTeX Citation

```bibtex
@article{03_attention_is_all_you_need_2017,
  title = {Attention Is All You Need (Transformer)},
  author = {Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin},
  journal = {arXiv preprint arXiv:1706.03762},
  year = {2017},
  url = {https://arxiv.org/abs/1706.03762}
}
```
