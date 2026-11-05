# Decision Transformer: Reinforcement Learning via Sequence Modeling

<div align="center">

[![Year](https://img.shields.io/badge/Year-2021-blue?style=for-the-badge)](https://arxiv.org/abs/2106.01345)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202021-purple?style=for-the-badge)](https://arxiv.org/abs/2106.01345)
[![arXiv](https://img.shields.io/badge/arXiv-2106.01345-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.01345)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2106.01345.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kzl/decision-transformer)

</div>

---

### 📋 Paper Metadata

- **Authors:** Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas, Igor Mordatch
- **Publication Year:** 2021
- **Venue:** NeurIPS 2021
- **Primary arXiv ID:** [`arXiv:2106.01345`](https://arxiv.org/abs/2106.01345)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2106.01345.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/kzl/decision-transformer)

---

### 📖 Executive Abstract

> "We introduce Decision Transformer, an architecture that casts the problem of Reinforcement Learning (RL) as conditional sequence modeling. By conditioning an autoregressive model on desired return (reward), past states, and actions, our Decision Transformer model can output actions that achieve target returns."

---

### 🎯 Core Problem & Motivation

Traditional offline RL algorithms (CQL, BEAR) rely on dynamic programming and TD-learning, which suffer from bootstrapping error, value overestimation, and training instability.

---

### 💡 Key Innovations & Architecture

1. **RL as Sequence Prediction**: Completely discarded Bellman backups and value functions, framing policy execution as autoregressive token generation.
2. **Return-to-Go Conditioning**: Tokens are fed as triplets: $\tau = (\hat{R}_1, s_1, a_1, \hat{R}_2, s_2, a_2, \dots)$ where $\hat{R}_t = \sum_{t'=t}^T r_{t'}$.
3. **Test-Time Return Steering**: At inference time, setting $\hat{R}_1$ to a high desired return prompts the model to generate high-performing actions.

---

### 📐 Mathematical Formulation

**Trajectory Sequence Representation:**
$$\tau = (\hat{R}_1, s_1, a_1, \hat{R}_2, s_2, a_2, \dots, \hat{R}_T, s_T, a_T)$$
**Autoregressive Cross-Entropy / MSE Action Loss:**
$$\mathcal{L}_{\text{DT}}(\theta) = \mathbb{E}_{\tau \sim \mathcal{D}} \left[ \sum_{t=1}^T \|a_t - f_\theta(s_{\le t}, a_{<t}, \hat{R}_{\le t})\|^2 \right]$$

---

### 🌟 Significance & Industry Impact

Bridged modern generative Transformers and Reinforcement Learning, inspiring subsequent work in robotics foundation models (RT-1, RT-2) and trajectory-level agent planning.

---

### 📚 BibTeX Citation

```bibtex
@article{04_decision_transformer_2021,
  title = {Decision Transformer: Reinforcement Learning via Sequence Modeling},
  author = {Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas, Igor Mordatch},
  journal = {arXiv preprint arXiv:2106.01345},
  year = {2021},
  url = {https://arxiv.org/abs/2106.01345}
}
```
