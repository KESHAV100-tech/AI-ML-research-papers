# Mixtral of Experts

<div align="center">

[![Year](https://img.shields.io/badge/Year-2024-blue?style=for-the-badge)](https://arxiv.org/abs/2401.04088)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2401.04088)
[![arXiv](https://img.shields.io/badge/arXiv-2401.04088-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2401.04088)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2401.04088.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mistralai/mistral-src)

</div>

---

### 📋 Paper Metadata

- **Authors:** Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2401.04088`](https://arxiv.org/abs/2401.04088)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2401.04088.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/mistralai/mistral-src)

---

### 📖 Executive Abstract

> "We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model. Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (experts). For every token, at each layer, a router network selects two experts to process the current state and combine their outputs additively."

---

### 🎯 Core Problem & Motivation

Scaling dense models increases compute cost linearly per token during both training and inference, making high-parameter models slow and expensive to serve.

---

### 💡 Key Innovations & Architecture

1. **Sparse MoE Architecture**: 8 experts per layer with top-2 token routing, activating only 13B parameters out of 47B total per token.
2. **High Inference Throughput**: Achieved the inference speed and operational cost of a 13B dense model while matching or outperforming LLaMA 2 70B.
3. **Long Context Window**: Supported native 32K context windows with flawless retrieval.

---

### 📐 Mathematical Formulation

**Top-2 Routing Gating Equation:**
$$y = \sum_{i=1}^n G(x)_i E_i(x)$$
$$\text{where } G(x) = \text{Softmax}(\text{TopK}(x \cdot W_g, k=2))$$
$$\text{TopK}(v, k)_i = \begin{cases} v_i & \text{if } v_i \text{ is in top } k \\ -\infty & \text{otherwise} \end{cases}$$

---

### 🌟 Significance & Industry Impact

Demonstrated that sparse MoE models could be stable, performant, and efficiently served on commodity hardware, setting off an industry-wide transition toward MoE foundation architectures.

---

### 📚 BibTeX Citation

```bibtex
@article{04_mixtral_of_experts_2024,
  title = {Mixtral of Experts},
  author = {Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed},
  journal = {arXiv preprint arXiv:2401.04088},
  year = {2024},
  url = {https://arxiv.org/abs/2401.04088}
}
```
