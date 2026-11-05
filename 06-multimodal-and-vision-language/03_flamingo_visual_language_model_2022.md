# Flamingo: a Visual Language Model for Few-Shot Learning

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2204.14198)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2204.14198)
[![arXiv](https://img.shields.io/badge/arXiv-2204.14198-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2204.14198)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2204.14198.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lucidrains/flamingo-pytorch)

</div>

---

### 📋 Paper Metadata

- **Authors:** Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, Karen Simonyan
- **Publication Year:** 2022
- **Venue:** NeurIPS 2022
- **Primary arXiv ID:** [`arXiv:2204.14198`](https://arxiv.org/abs/2204.14198)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2204.14198.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/lucidrains/flamingo-pytorch)

---

### 📖 Executive Abstract

> "We introduce Flamingo, a family of Visual Language Models (VLM) with state-of-the-art few-shot learning capabilities on a wide range of open-ended multimodal tasks. Flamingo models accept interleaved sequences of visual data (images and videos) and text as input and generate text in an autoregressive fashion."

---

### 🎯 Core Problem & Motivation

Models could not seamlessly handle interleaved sequences of multiple images, videos, and text prompts in an open-ended dialogue setting.

---

### 💡 Key Innovations & Architecture

1. **Perceiver Resampler**: Transformed variable-sized visual features from arbitrary image/video sequences into a fixed number of 64 visual tokens.
2. **Gated Cross-Attention Dense Layers**: Interleaved cross-attention blocks into frozen pre-trained LM layers initialized with tanh-gating to preserve pre-trained knowledge.
3. **Interleaved Multimodal Pre-training**: Trained on billions of web pages containing interleaved text and images (M3W dataset).

---

### 📐 Mathematical Formulation

**Tanh-Gated Cross-Attention:**
$$y = x + \tanh(\alpha) \cdot \text{CrossAttention}(x, \text{VisualTokens})$$
At initialization $\alpha = 0$, guaranteeing identity mapping so the LM retains full text capabilities initially.

---

### 🌟 Significance & Industry Impact

Set the gold standard for few-shot multimodal learning and influenced the multi-image architecture used in Gemini and GPT-4V.

---

### 📚 BibTeX Citation

```bibtex
@article{03_flamingo_visual_language_model_2022,
  title = {Flamingo: a Visual Language Model for Few-Shot Learning},
  author = {Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, Karen Simonyan},
  journal = {arXiv preprint arXiv:2204.14198},
  year = {2022},
  url = {https://arxiv.org/abs/2204.14198}
}
```
