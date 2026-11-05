# Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2023-blue?style=for-the-badge)](https://arxiv.org/abs/2305.18290)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2305.18290)
[![arXiv](https://img.shields.io/badge/arXiv-2305.18290-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.18290)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2305.18290.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/eric-mitchell/direct-preference-optimization)

</div>

---

### 📋 Paper Metadata

- **Authors:** Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn
- **Publication Year:** 2023
- **Venue:** NeurIPS 2023
- **Primary arXiv ID:** [`arXiv:2305.18290`](https://arxiv.org/abs/2305.18290)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2305.18290.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/eric-mitchell/direct-preference-optimization)

---

### 📖 Executive Abstract

> "While RLHF is a powerful approach, it is complex and often unstable, fitting a reward model that is then optimized with reinforcement learning. We propose Direct Preference Optimization (DPO), which implicitly optimizes the same objective as RLHF (reward maximization with a KL penalty) with a simple binary cross-entropy loss directly on policy parameters."

---

### 🎯 Core Problem & Motivation

RLHF with PPO is notoriously unstable, computationally expensive (requiring 4 simultaneous models in memory: actor, critic, reference, reward), and sensitive to hyperparameters.

---

### 💡 Key Innovations & Architecture

1. **Closed-Form Mapping**: Showed that the optimal policy under the Bradley-Terry preference model can be solved analytically for the implicit reward:
   $$r(x, y) = \beta \log \frac{\pi_\theta(y \mid x)}{\pi_{\text{ref}}(y \mid x)}$$
2. **Single-Stage Optimization**: Discarded the separate reward model and reinforcement learning loop entirely, training directly on preference pairs via binary cross-entropy.
3. **Stability & Simplicity**: Training is as simple and stable as standard supervised fine-tuning.

---

### 📐 Mathematical Formulation

**DPO Loss Function:**
$$\mathcal{L}_{\text{DPO}}(\pi_\theta; \pi_{\text{ref}}) = - \mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]$$

---

### 🌟 Significance & Industry Impact

DPO became the dominant alignment method across open-source and industrial AI labs (used extensively in Llama 3, Mistral, and Zephyr), democratizing model alignment without complex RL infrastructure.

---

### 📚 BibTeX Citation

```bibtex
@article{02_direct_preference_optimization_2023,
  title = {Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)},
  author = {Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn},
  journal = {arXiv preprint arXiv:2305.18290},
  year = {2023},
  url = {https://arxiv.org/abs/2305.18290}
}
```
