# Gemma: Open Models Based on Gemini Research and Technology

<div align="center">

[![Year](https://img.shields.io/badge/Year-2024-blue?style=for-the-badge)](https://arxiv.org/abs/2403.08295)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2403.08295)
[![arXiv](https://img.shields.io/badge/arXiv-2403.08295-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.08295)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2403.08295.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/google-deepmind/gemma)

</div>

---

### 📋 Paper Metadata

- **Authors:** Gemma Team, Google DeepMind
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2403.08295`](https://arxiv.org/abs/2403.08295)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2403.08295.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/google-deepmind/gemma)

---

### 📖 Executive Abstract

> "We present Gemma, a family of lightweight, state-of-the-art open models built from the same research and technology used to create the Gemini models. Gemma models demonstrate strong performance across academic benchmarks for language understanding, reasoning, and mathematics."

---

### 🎯 Core Problem & Motivation

Developers need lightweight, high-performance open models that can run locally on consumer workstations, laptops, or mobile devices while maintaining rigorous safety standards.

---

### 💡 Key Innovations & Architecture

1. **Gemini Architectural Lineage**: Multi-Query Attention (2B) and Multi-Head Attention (7B) with GeGLU non-linearities and normalized embeddings.
2. **Rigorous Data Curation**: Pre-trained on up to 6T tokens of primarily English web data, mathematics, and code with extensive filtering for safety and quality.
3. **Advanced Alignment**: Comprehensive RLHF alignment with dual reward models focused on factuality and instruction adherence.

---

### 📐 Mathematical Formulation

**GeGLU Activation:**
$$\text{GeGLU}(x, W, V) = \text{GELU}(x W) \otimes (x V)$$

---

### 🌟 Significance & Industry Impact

Provided academic researchers and edge-device developers with compact, safety-aligned models running seamlessly on consumer hardware, Google Colab, and mobile devices.

---

### 📚 BibTeX Citation

```bibtex
@article{06_gemma_models_2024,
  title = {Gemma: Open Models Based on Gemini Research and Technology},
  author = {Gemma Team, Google DeepMind},
  journal = {arXiv preprint arXiv:2403.08295},
  year = {2024},
  url = {https://arxiv.org/abs/2403.08295}
}
```
