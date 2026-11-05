# Playing Atari with Deep Reinforcement Learning (DQN)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2013-blue?style=for-the-badge)](https://arxiv.org/abs/1312.5602)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%20Workshop%202013%20/%20Nature%202015-purple?style=for-the-badge)](https://arxiv.org/abs/1312.5602)
[![arXiv](https://img.shields.io/badge/arXiv-1312.5602-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1312.5602)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/1312.5602.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/deepmind/dqn)

</div>

---

### 📋 Paper Metadata

- **Authors:** Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller
- **Publication Year:** 2013
- **Venue:** NeurIPS Workshop 2013 / Nature 2015
- **Primary arXiv ID:** [`arXiv:1312.5602`](https://arxiv.org/abs/1312.5602)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/1312.5602.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/deepmind/dqn)

---

### 📖 Executive Abstract

> "We present the first deep learning model to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning. The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards."

---

### 🎯 Core Problem & Motivation

Traditional RL relied on hand-engineered state features and was unstable when combined with non-linear function approximators due to correlated state transitions and non-stationary targets.

---

### 💡 Key Innovations & Architecture

1. **Experience Replay Buffer**: Stored past transitions $(s_t, a_t, r_t, s_{t+1})$ and sampled random minibatches, breaking temporal correlations and stabilizing gradient descent.
2. **Target Network**: Maintained a separate frozen target network $\theta^-$ updated periodically, preventing runaway feedback loops during Bellman updates.
3. **End-to-End Pixel-to-Action Learning**: Processed 4 consecutive raw video frames to infer velocity and mastered 49 Atari games.

---

### 📐 Mathematical Formulation

**DQN Bellman Loss:**
$$L_i(\theta_i) = \mathbb{E}_{(s, a, r, s') \sim U(D)} \left[ \left( r + \gamma \max_{a'} Q(s', a'; \theta_i^-) - Q(s, a; \theta_i) \right)^2 \right]$$

---

### 🌟 Significance & Industry Impact

First demonstration that a single neural network architecture could learn human-level control policies across diverse tasks directly from visual perceptions, launching Deep Reinforcement Learning as a field.

---

### 📚 BibTeX Citation

```bibtex
@article{01_deep_q_networks_dqn_2013,
  title = {Playing Atari with Deep Reinforcement Learning (DQN)},
  author = {Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller},
  journal = {arXiv preprint arXiv:1312.5602},
  year = {2013},
  url = {https://arxiv.org/abs/1312.5602}
}
```
