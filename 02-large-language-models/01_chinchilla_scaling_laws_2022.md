# Training Compute-Optimal Large Language Models (Chinchilla)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2203.15556)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2203.15556)
[![arXiv](https://img.shields.io/badge/arXiv-2203.15556-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.15556)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2203.15556.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/google-deepmind)

</div>

---

### 📋 Paper Metadata

- **Authors:** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre
- **Publication Year:** 2022
- **Venue:** NeurIPS 2022
- **Primary arXiv ID:** [`arXiv:2203.15556`](https://arxiv.org/abs/2203.15556)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2203.15556.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/google-deepmind)

---

### 📖 Executive Abstract

> "We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant."

---

### 🎯 Core Problem & Motivation

Earlier scaling laws (Kaplan et al., 2020) concluded that parameter count should scale much faster than dataset size ($N \propto C^{0.73}$, $D \propto C^{0.27}$), leading companies to train massive models (Gopher 280B, GPT-3 175B) on relatively small datasets (~300B tokens).

---

### 💡 Key Innovations & Architecture

1. **Empirical Evaluation Over 400 Models**: Trained models from 70M to 16B parameters on varying token budgets.
2. **Compute-Optimal Ratio**: Proved that parameters and tokens should scale in **equal proportion**: $N \propto C^{0.5}$ and $D \propto C^{0.5}$.
3. **Chinchilla 70B**: Trained a 70B model on 1.4T tokens (4x more tokens than Gopher), outperforming Gopher (280B), GPT-3 (175B), and Jurassic-1 (178B) while slashing inference costs.

---

### 📐 Mathematical Formulation

**Compute Budget Constraint:**
$$C \approx 6 N D$$
Where $C$ is total FLOPs, $N$ is parameter count, and $D$ is training token count.

**Loss Parametrization:**
$$\hat{L}(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}$$
Under optimal compute allocation:
$$N_{\text{opt}} \propto C^{\frac{\beta}{\alpha + \beta}}, \quad D_{\text{opt}} \propto C^{\frac{\alpha}{\alpha + \beta}}$$
With empirical findings $\alpha \approx 0.34$, $\beta \approx 0.28$, yielding $N \propto C^{0.5}$ and $D \propto C^{0.5}$.

---

### 🌟 Significance & Industry Impact

Completely redefined model pre-training strategy across the industry. LLaMA, Mistral, and subsequent open-source models followed Chinchilla's recipe: train smaller, denser models on trillions of tokens for optimal inference latency.

---

### 📚 BibTeX Citation

```bibtex
@article{01_chinchilla_scaling_laws_2022,
  title = {Training Compute-Optimal Large Language Models (Chinchilla)},
  author = {Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre},
  journal = {arXiv preprint arXiv:2203.15556},
  year = {2022},
  url = {https://arxiv.org/abs/2203.15556}
}
```
