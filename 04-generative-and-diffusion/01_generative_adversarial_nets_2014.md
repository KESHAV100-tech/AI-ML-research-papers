# Generative Adversarial Nets (GAN)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2014-blue?style=for-the-badge)](https://arxiv.org/abs/1406.2661)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202014-purple?style=for-the-badge)](https://arxiv.org/abs/1406.2661)
[![arXiv](https://img.shields.io/badge/arXiv-1406.2661-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1406.2661)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/1406.2661.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/goodfeli/adversarial)

</div>

---

### 📋 Paper Metadata

- **Authors:** Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio
- **Publication Year:** 2014
- **Venue:** NeurIPS 2014
- **Primary arXiv ID:** [`arXiv:1406.2661`](https://arxiv.org/abs/1406.2661)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/1406.2661.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/goodfeli/adversarial)

---

### 📖 Executive Abstract

> "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G."

---

### 🎯 Core Problem & Motivation

Generative modeling previously required intractable approximations to partition functions (Markov Chain Monte Carlo) or lower-bound relaxations that produced blurry samples.

---

### 💡 Key Innovations & Architecture

1. **Two-Player Minimax Game**: Generator $G(z)$ creates synthetic candidates; Discriminator $D(x)$ distinguishes real data from generated counterfeits.
2. **Implicit Density Estimation**: $G$ learns to map noise vectors $z \sim p_z$ to data distribution $p_{\text{data}}$ without explicit likelihood formulation.
3. **Equilibrium at Jensen-Shannon Divergence**: At optimal discriminator $D^*$, the objective minimizes the Jensen-Shannon divergence between $p_{\text{data}}$ and $p_g$.

---

### 📐 Mathematical Formulation

**Adversarial Minimax Objective:**
$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)} [\log D(x)] + \mathbb{E}_{z \sim p_z(z)} [\log(1 - D(G(z)))]$$

**Optimal Discriminator Form:**
$$D^*(x) = \frac{p_{\text{data}}(x)}{p_{\text{data}}(x) + p_g(x)}$$

---

### 🌟 Significance & Industry Impact

Launched an explosion of generative vision research across StyleGAN, CycleGAN, BigGAN, and Pix2Pix, dominating image generation until diffusion models emerged in 2020.

---

### 📚 BibTeX Citation

```bibtex
@article{01_generative_adversarial_nets_2014,
  title = {Generative Adversarial Nets (GAN)},
  author = {Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio},
  journal = {arXiv preprint arXiv:1406.2661},
  year = {2014},
  url = {https://arxiv.org/abs/1406.2661}
}
```
