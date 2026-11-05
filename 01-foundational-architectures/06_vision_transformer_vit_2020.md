# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2020-blue?style=for-the-badge)](https://arxiv.org/abs/2010.11929)
[![Venue](https://img.shields.io/badge/Venue-ICLR%202021-purple?style=for-the-badge)](https://arxiv.org/abs/2010.11929)
[![arXiv](https://img.shields.io/badge/arXiv-2010.11929-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2010.11929)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2010.11929.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/google-research/vision_transformer)

</div>

---

### 📋 Paper Metadata

- **Authors:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby
- **Publication Year:** 2020
- **Venue:** ICLR 2021
- **Primary arXiv ID:** [`arXiv:2010.11929`](https://arxiv.org/abs/2010.11929)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2010.11929.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/google-research/vision_transformer)

---

### 📖 Executive Abstract

> "While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks."

---

### 🎯 Core Problem & Motivation

Convolutions have strong built-in inductive biases (translation equivariance, locality). While helpful on small datasets, these biases limit peak capacity when massive amounts of training data are available.

---

### 💡 Key Innovations & Architecture

1. **Patch Flattening & Embedding**: Sliced 2D images into non-overlapping $16 \times 16$ or $14 \times 14$ patches and flattened them into 1D token embeddings.
2. **Prepend Learnable [CLS] Token**: Added a learnable classification token whose state at the output serves as the image representation.
3. **Scale-Dependent Performance**: Demonstrated that while CNNs outperform ViT on small datasets (ImageNet-1K), ViT overtakes CNNs decisively when pre-trained on JFT-300M.

---

### 📐 Mathematical Formulation

**Linear Patch Projection:**
$$z_0 = [x_{\text{class}}; x_p^1 E; x_p^2 E; \dots; x_p^N E] + E_{\text{pos}}$$
Where $x_p^i \in \mathbb{R}^{P^2 \cdot C}$ is patch $i$, $E \in \mathbb{R}^{(P^2 C) \times D}$ is the patch projection matrix, and $E_{\text{pos}}$ is the 1D position embedding.

---

### 🌟 Significance & Industry Impact

Eliminated the domain gap between computer vision and natural language processing, making Transformers the unified modality backbone across text, vision, audio, and multimodal foundation models.

---

### 📚 BibTeX Citation

```bibtex
@article{06_vision_transformer_vit_2020,
  title = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)},
  author = {Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby},
  journal = {arXiv preprint arXiv:2010.11929},
  year = {2020},
  url = {https://arxiv.org/abs/2010.11929}
}
```
