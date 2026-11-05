# Denoising Diffusion Probabilistic Models (DDPM)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2020-blue?style=for-the-badge)](https://arxiv.org/abs/2006.11239)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202020-purple?style=for-the-badge)](https://arxiv.org/abs/2006.11239)
[![arXiv](https://img.shields.io/badge/arXiv-2006.11239-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2006.11239)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2006.11239.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hojonathanho/diffusion)

</div>

---

### 📋 Paper Metadata

- **Authors:** Jonathan Ho, Ajay Jain, Pieter Abbeel
- **Publication Year:** 2020
- **Venue:** NeurIPS 2020
- **Primary arXiv ID:** [`arXiv:2006.11239`](https://arxiv.org/abs/2006.11239)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2006.11239.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/hojonathanho/diffusion)

---

### 📖 Executive Abstract

> "We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion models and denoising score matching."

---

### 🎯 Core Problem & Motivation

GANs suffer from mode collapse and training instability; VAEs produce blurry samples. Earlier diffusion models (Sohl-Dickstein 2015) were deemed too slow and computationally expensive.

---

### 💡 Key Innovations & Architecture

1. **Simplified Loss Formulation**: Parameterized the reverse process to directly predict the injected Gaussian noise $\epsilon$, dramatically simplifying the training objective.
2. **Equivalence to Score Matching**: Connected discrete-time Markov diffusion chains with continuous-time Langevin dynamics and score-based generative modeling.
3. **Superior Sample Quality**: Achieved an unprecedented FID score of 3.17 on CIFAR-10, demonstrating that diffusion models could match and exceed GAN quality.

---

### 📐 Mathematical Formulation

**Forward Noising Process (Closed-Form Jump):**
$$q(x_t \mid x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1 - \bar{\alpha}_t) I)$$

**Simplified Training Objective:**
$$L_{\text{simple}}(\theta) = \mathbb{E}_{t, x_0, \epsilon} \left[ \|\epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon, t)\|^2 \right]$$

---

### 🌟 Significance & Industry Impact

Triggered the modern diffusion revolution, replacing GANs as the state-of-the-art methodology for generative modeling in computer vision, audio, biology, and 3D synthesis.

---

### 📚 BibTeX Citation

```bibtex
@article{03_denoising_diffusion_ddpm_2020,
  title = {Denoising Diffusion Probabilistic Models (DDPM)},
  author = {Jonathan Ho, Ajay Jain, Pieter Abbeel},
  journal = {arXiv preprint arXiv:2006.11239},
  year = {2020},
  url = {https://arxiv.org/abs/2006.11239}
}
```
