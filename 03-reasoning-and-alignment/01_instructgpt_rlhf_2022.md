# Training language models to follow instructions with human feedback (InstructGPT)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2203.02155)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2203.02155)
[![arXiv](https://img.shields.io/badge/arXiv-2203.02155-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2203.02155)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2203.02155.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/openai/following-instructions-human-feedback)

</div>

---

### 📋 Paper Metadata

- **Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe
- **Publication Year:** 2022
- **Venue:** NeurIPS 2022
- **Primary arXiv ID:** [`arXiv:2203.02155`](https://arxiv.org/abs/2203.02155)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2203.02155.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/openai/following-instructions-human-feedback)

---

### 📖 Executive Abstract

> "Making language models bigger does not inherently make them better at following a user's intent. In this work, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. We apply Reinforcement Learning from Human Feedback (RLHF) to fine-tune GPT-3 to follow a broad class of written instructions."

---

### 🎯 Core Problem & Motivation

Pre-trained language models optimize next-token prediction on internet text, causing them to generate toxic, mendacious, hallucinatory, or unhelpful answers when given direct user instructions.

---

### 💡 Key Innovations & Architecture

1. **Three-Step RLHF Pipeline**:
   - Step 1: Supervised Fine-Tuning (SFT) on human prompt-response demonstrations.
   - Step 2: Reward Model (RM) trained on pairwise human preference comparisons ($y_w \succ y_l$).
   - Step 3: Reinforcement Learning policy optimization via PPO with a KL-divergence penalty.
2. **Alignment Generalization**: InstructGPT 1.3B was preferred by human labelers over the raw 175B GPT-3 model despite having 100x fewer parameters.

---

### 📐 Mathematical Formulation

**Reward Model Loss:**
$$\text{loss}(\theta) = - \mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma(r_\theta(x, y_w) - r_\theta(x, y_l)) \right]$$

**PPO Objective with KL Penalty:**
$$\text{obj}(\phi) = \mathbb{E}_{(x, y)} [r_\theta(x, y) - \beta D_{\text{KL}}(\pi_\phi^{\text{RL}}(y \mid x) \parallel \pi^{\text{SFT}}(y \mid x))] + \gamma \mathbb{E}_x [\log \pi_\phi^{\text{RL}}(x)]$$

---

### 🌟 Significance & Industry Impact

Directly birthed **ChatGPT**, the fastest-growing consumer application in history, and established RLHF as the standard alignment technology for commercial AI.

---

### 📚 BibTeX Citation

```bibtex
@article{01_instructgpt_rlhf_2022,
  title = {Training language models to follow instructions with human feedback (InstructGPT)},
  author = {Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe},
  journal = {arXiv preprint arXiv:2203.02155},
  year = {2022},
  url = {https://arxiv.org/abs/2203.02155}
}
```
