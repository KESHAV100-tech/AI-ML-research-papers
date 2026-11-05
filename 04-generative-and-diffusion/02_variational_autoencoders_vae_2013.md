# Auto-Encoding Variational Bayes (VAE)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2013-blue?style=for-the-badge)](https://arxiv.org/abs/1312.6114)
[![Venue](https://img.shields.io/badge/Venue-ICLR%202014-purple?style=for-the-badge)](https://arxiv.org/abs/1312.6114)
[![arXiv](https://img.shields.io/badge/arXiv-1312.6114-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1312.6114)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/1312.6114.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/y0ast/VAE-TensorFlow)

</div>

---

### 📋 Paper Metadata

- **Authors:** Diederik P. Kingma, Max Welling
- **Publication Year:** 2013
- **Venue:** ICLR 2014
- **Primary arXiv ID:** [`arXiv:1312.6114`](https://arxiv.org/abs/1312.6114)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/1312.6114.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/y0ast/VAE-TensorFlow)

---

### 📖 Executive Abstract

> "How can we perform efficient inference and learning in directed probabilistic models, in the presence of continuous latent variables with intractable posterior distributions, and large datasets? We introduce a stochastic variational inference and learning algorithm that scales to large datasets, based on the reparameterization trick."

---

### 🎯 Core Problem & Motivation

Continuous latent variable models have intractable true posterior distributions $p(z \mid x)$, making standard Expectation-Maximization and variational inference computationally infeasible on large datasets.

---

### 💡 Key Innovations & Architecture

1. **Reparameterization Trick**: Rewrote latent variable sampling as $z = g_\phi(\epsilon, x) = \mu(x) + \sigma(x) \odot \epsilon$ where $\epsilon \sim \mathcal{N}(0, I)$, making stochastic sampling differentiable with backpropagation.
2. **Variational Autoencoder (VAE)**: Unified an encoder probabilistic network $q_\phi(z \mid x)$ and decoder generator network $p_\theta(x \mid z)$.
3. **ELBO Optimization**: Jointly maximized reconstruction quality while penalizing divergence from the prior distribution.

---

### 📐 Mathematical Formulation

**Evidence Lower Bound (ELBO):**
$$\log p_\theta(x) \ge \mathcal{L}(\theta, \phi; x) = \mathbb{E}_{q_\phi(z \mid x)} [\log p_\theta(x \mid z)] - D_{\text{KL}}(q_\phi(z \mid x) \parallel p(z))$$

**Gaussian KL Divergence in Closed Form:**
$$- D_{\text{KL}}(q_\phi(z \mid x) \parallel \mathcal{N}(0, I)) = \frac{1}{2} \sum_{j=1}^J \left( 1 + \log(\sigma_j^2) - \mu_j^2 - \sigma_j^2 \right)$$

---

### 🌟 Significance & Industry Impact

Fundamental contribution to probabilistic machine learning. VAEs provide the compressed latent space encoders used in modern Latent Diffusion Models (Stable Diffusion) and video generation architectures.

---

### 📚 BibTeX Citation

```bibtex
@article{02_variational_autoencoders_vae_2013,
  title = {Auto-Encoding Variational Bayes (VAE)},
  author = {Diederik P. Kingma, Max Welling},
  journal = {arXiv preprint arXiv:1312.6114},
  year = {2013},
  url = {https://arxiv.org/abs/1312.6114}
}
```
