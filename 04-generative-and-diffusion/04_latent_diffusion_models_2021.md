# High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2021-blue?style=for-the-badge)](https://arxiv.org/abs/2112.10752)
[![Venue](https://img.shields.io/badge/Venue-CVPR%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2112.10752)
[![arXiv](https://img.shields.io/badge/arXiv-2112.10752-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2112.10752)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2112.10752.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/CompVis/latent-diffusion)

</div>

---

### 📋 Paper Metadata

- **Authors:** Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer
- **Publication Year:** 2021
- **Venue:** CVPR 2022
- **Primary arXiv ID:** [`arXiv:2112.10752`](https://arxiv.org/abs/2112.10752)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2112.10752.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/CompVis/latent-diffusion)

---

### 📖 Executive Abstract

> "By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models achieve state-of-the-art synthesis results on image data. However, operating directly in the high-dimensional pixel space consumes immense computational resources. We apply them in the latent space of powerful pretrained autoencoders."

---

### 🎯 Core Problem & Motivation

Pixel-space diffusion models require iterating hundreds of denoising steps over full-resolution images ($512 \times 512 \times 3$), making training and inference prohibitively slow and expensive.

---

### 💡 Key Innovations & Architecture

1. **Latent Space Compression**: Trained a high-fidelity autoencoder with perceptual and adversarial losses to compress images by 8x ($64 \times 64 \times 4$), removing imperceptible high-frequency noise.
2. **Cross-Attention Conditioning**: Added cross-attention layers into the U-Net backbone, allowing flexible conditioning on text prompts (via CLIP), layout masks, or depth maps.
3. **Consumer Hardware Feasibility**: Enabled 512x512 image synthesis on consumer GPUs with single-second inference latencies.

---

### 📐 Mathematical Formulation

**Latent Diffusion Training Loss:**
$$L_{\text{LDM}} = \mathbb{E}_{\mathcal{E}(x), y, \epsilon, t} \left[ \|\epsilon - \epsilon_\theta(z_t, t, \tau_\theta(y))\|^2 \right]$$
Where $\mathcal{E}$ is the encoder, $z_t$ is the noised latent, and $\tau_\theta(y)$ is the text conditioning encoder.

---

### 🌟 Significance & Industry Impact

Released open-source as **Stable Diffusion**, sparking the democratized text-to-image boom, creative AI applications, ControlNet, LoRA image fine-tuning, and open creative tools.

---

### 📚 BibTeX Citation

```bibtex
@article{04_latent_diffusion_models_2021,
  title = {High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)},
  author = {Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer},
  journal = {arXiv preprint arXiv:2112.10752},
  year = {2021},
  url = {https://arxiv.org/abs/2112.10752}
}
```
