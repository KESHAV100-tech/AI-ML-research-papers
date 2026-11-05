# Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (AlphaZero)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2017-blue?style=for-the-badge)](https://arxiv.org/abs/1712.01815)
[![Venue](https://img.shields.io/badge/Venue-Science%202018%20/%20arXiv:1712.01815-purple?style=for-the-badge)](https://arxiv.org/abs/1712.01815)
[![arXiv](https://img.shields.io/badge/arXiv-1712.01815-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/1712.01815)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/1712.01815.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/deepmind/alphazero)

</div>

---

### 📋 Paper Metadata

- **Authors:** David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, Demis Hassabis
- **Publication Year:** 2017
- **Venue:** Science 2018 / arXiv:1712.01815
- **Primary arXiv ID:** [`arXiv:1712.01815`](https://arxiv.org/abs/1712.01815)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/1712.01815.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/deepmind/alphazero)

---

### 📖 Executive Abstract

> "The game of chess is the longest-standing testbed in artificial intelligence history. We present AlphaZero, a generic algorithm that masters chess, shogi, and Go from scratch without domain knowledge beyond the basic game rules, defeating world-champion programs (Stockfish, Elmo, AlphaGo Zero) after just hours of self-play."

---

### 🎯 Core Problem & Motivation

Traditional chess programs (Stockfish, Deep Blue) relied on decades of human-crafted heuristics, opening books, and endgame tables that failed to generalize across different board games.

---

### 💡 Key Innovations & Architecture

1. **Tabula Rasa Learning**: Zero human training data; learns purely from self-play games given only the basic rules of the game.
2. **Unified Policy & Value Network**: A single deep residual neural network $(p, v) = f_\theta(s)$ predicting move probabilities $p$ and position outcome $v \in [-1, 1]$.
3. **MCTS Integration**: Guided Monte Carlo Tree Search (MCTS) where the neural network replaces rollouts with direct value evaluation and policy priors.

---

### 📐 Mathematical Formulation

**Loss Function for Joint Policy and Value Training:**
$$l = (z - v)^2 - \pi^T \log p + c \|\theta\|^2$$
Where $z \in \{-1, 0, 1\}$ is the actual self-play game winner, and $\pi$ is the MCTS visit probability distribution vector.

---

### 🌟 Significance & Industry Impact

Considered one of AI's crowning milestones. AlphaZero introduced dynamic, long-term strategic moves that revolutionized grandmaster chess understanding and inspired structural biology breakthroughs like AlphaFold.

---

### 📚 BibTeX Citation

```bibtex
@article{03_alphazero_game_intelligence_2017,
  title = {Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (AlphaZero)},
  author = {David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, Demis Hassabis},
  journal = {arXiv preprint arXiv:1712.01815},
  year = {2017},
  url = {https://arxiv.org/abs/1712.01815}
}
```
