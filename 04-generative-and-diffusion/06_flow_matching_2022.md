# Flow Matching for Generative Modeling

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2210.02747)
[![Venue](https://img.shields.io/badge/Venue-ICLR%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2210.02747)
[![arXiv](https://img.shields.io/badge/arXiv-2210.02747-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2210.02747)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2210.02747.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/facebookresearch/flow_matching)

</div>

---

### 📋 Paper Metadata

- **Authors:** Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nicklas, Matt Le
- **Publication Year:** 2022
- **Venue:** ICLR 2023
- **Primary arXiv ID:** [`arXiv:2210.02747`](https://arxiv.org/abs/2210.02747)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2210.02747.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/facebookresearch/flow_matching)

---

### 📖 Executive Abstract

> "We introduce Flow Matching (FM), a new approach to training Continuous Normalizing Flow (CNF) models at scale. Flow Matching uses regression objectives on vector fields along probability paths without needing numerical ODE simulations during training, unlocking optimal transport displacement interpolation."

---

### 🎯 Core Problem & Motivation

Continuous Normalizing Flows (CNFs) had strong mathematical foundations but required slow, costly numerical ODE solvers during training. Standard diffusion models curved stochastic trajectories require many sampling steps.

---

### 💡 Key Innovations & Architecture

1. **Simulation-Free Training**: Direct per-sample regression on target vector fields along conditional probability paths without solving ODEs at train time.
2. **Optimal Transport Paths**: Straightens probability flow trajectories between prior noise and data distributions, enabling straight-line particle trajectories.
3. **Fast Inference**: Requires as few as 4-10 integration steps to generate high-fidelity samples.

---

### 📐 Mathematical Formulation

**Flow Matching Objective:**
$$\mathcal{L}_{\text{CFM}}(\theta) = \mathbb{E}_{t, q(x_1), p_t(x \mid x_1)} \left[ \|v_t(x) - u_t(x \mid x_1)\|^2 \right]$$
**Optimal Transport Conditional Vector Field:**
$$\psi_t(x_0) = (1 - t) x_0 + t x_1, \quad u_t(x \mid x_1, x_0) = x_1 - x_0$$

---

### 🌟 Significance & Industry Impact

Established the mathematical framework adopted by modern state-of-the-art generative models including Flux.1, Stable Diffusion 3, and voice synthesis systems.

---

### 📚 BibTeX Citation

```bibtex
@article{06_flow_matching_2022,
  title = {Flow Matching for Generative Modeling},
  author = {Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nicklas, Matt Le},
  journal = {arXiv preprint arXiv:2210.02747},
  year = {2022},
  url = {https://arxiv.org/abs/2210.02747}
}
```
