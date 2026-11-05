# ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2012-blue?style=for-the-badge)](https://arxiv.org/abs/1206.5538)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202012-purple?style=for-the-badge)](https://arxiv.org/abs/1206.5538)
[![arXiv](https://img.shields.io/badge/arXiv-1206.5538-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1206.5538)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/akrizhevsky/cuda-convnet2)

</div>

---

### 📋 Paper Metadata

- **Authors:** Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
- **Publication Year:** 2012
- **Venue:** NeurIPS 2012
- **Primary arXiv ID:** [`arXiv:1206.5538`](https://arxiv.org/abs/1206.5538)
- **PDF Direct Download:** [Click to Read Official PDF](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/akrizhevsky/cuda-convnet2)

---

### 📖 Executive Abstract

> "We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art."

---

### 🎯 Core Problem & Motivation

Prior to 2012, visual recognition relied on hand-crafted feature extractors (SIFT, HOG) coupled with linear classifiers or SVMs. These methods hit a severe performance plateau on large-scale, diverse real-world images.

---

### 💡 Key Innovations & Architecture

1. **GPU Acceleration**: Implemented highly optimized 2D convolutions on dual NVIDIA GTX 580 GPUs with cross-GPU communication.
2. **ReLU Non-Linearity**: Replaced standard sigmoid/tanh activations with Rectified Linear Units ($f(x) = \max(0, x)$), speeding up convergence by 6x.
3. **Dropout Regularization**: Introduced 0.5 dropout probability in fully connected layers to prevent co-adaptation of features.
4. **Data Augmentation**: Applied real-time image translations, horizontal reflections, and PCA color jittering.

---

### 📐 Mathematical Formulation

**ReLU Activation Function:**
$$f(x) = \max(0, x)$$

**Local Response Normalization (LRN):**
$$b_{x,y}^i = a_{x,y}^i / \left( k + \alpha \sum_{j=\max(0, i-n/2)}^{\min(N-1, i+n/2)} (a_{x,y}^j)^2 \right)^\beta$$

---

### 🌟 Significance & Industry Impact

AlexNet won ImageNet LSVRC-2012 by an unprecedented margin of 10.8 percentage points, convincing the entire AI community that deep neural networks trained on GPUs are the path forward. It triggered the modern Deep Learning revolution.

---

### 📚 BibTeX Citation

```bibtex
@article{01_alexnet_2012,
  title = {ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)},
  author = {Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton},
  journal = {arXiv preprint arXiv:1206.5538},
  year = {2012},
  url = {https://arxiv.org/abs/1206.5538}
}
```
