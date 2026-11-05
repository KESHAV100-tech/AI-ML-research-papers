# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

<div align="center">

[![Year](https://img.shields.io/badge/Year-2025-blue?style=for-the-badge)](https://arxiv.org/abs/2501.12948)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2501.12948)
[![arXiv](https://img.shields.io/badge/arXiv-2501.12948-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2501.12948)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2501.12948.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-R1)

</div>

---

### 📋 Paper Metadata

- **Authors:** DeepSeek-AI
- **Publication Year:** 2025
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2501.12948`](https://arxiv.org/abs/2501.12948)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2501.12948.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/deepseek-ai/DeepSeek-R1)

---

### 📖 Executive Abstract

> "We introduce our first-generation reasoning models, DeepSeek-R1-Zero and DeepSeek-R1. DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning without supervised fine-tuning (SFT) as a preliminary step, demonstrates remarkable reasoning capabilities. DeepSeek-R1 incorporates multi-stage training and cold-start data before RL, achieving performance on par with OpenAI-o1 across math, code, and reasoning tasks."

---

### 🎯 Core Problem & Motivation

Frontier reasoning capabilities were assumed to require massive human-annotated reasoning trace datasets ($100K+ SFT examples) and proprietary closed-source infrastructure.

---

### 💡 Key Innovations & Architecture

1. **Pure RL Emergence (R1-Zero)**: Showed that applying RL (Group Relative Policy Optimization - GRPO) directly onto a base model without SFT naturally elicits long chains of thought, self-reflection, and verification.
2. **Group Relative Policy Optimization (GRPO)**: Dispenses with the critic neural network, estimating baseline rewards from the mean and standard deviation of outputs within a sampled group.
3. **Knowledge Distillation into Small Dense Models**: Distilled R1 reasoning traces into Qwen and Llama models (1.5B to 70B), dramatically outperforming base open models on reasoning benchmarks.

---

### 📐 Mathematical Formulation

**GRPO Objective Function:**
$$\mathcal{J}_{\text{GRPO}}(\theta) = \mathbb{E} \left[ \frac{1}{G} \sum_{i=1}^G \min \left( \frac{\pi_\theta(o_i \mid q)}{\pi_{\theta_{\text{old}}}(o_i \mid q)} \hat{A}_i, \text{clip}\left( \frac{\pi_\theta(o_i \mid q)}{\pi_{\theta_{\text{old}}}(o_i \mid q)}, 1-\epsilon, 1+\epsilon \right) \hat{A}_i \right) - \beta D_{\text{KL}}(\pi_\theta \parallel \pi_{\text{ref}}) \right]$$
$$\text{where Advantage: } \hat{A}_i = \frac{r_i - \text{mean}(\{r_1, \dots, r_G\})}{\text{std}(\{r_1, \dots, r_G\})}$$

---

### 🌟 Significance & Industry Impact

Completely upended closed-source AI dominance in reasoning, matching OpenAI-o1 on AIME, MATH, and Codeforces while releasing open weights and full technical reproducibility.

---

### 📚 BibTeX Citation

```bibtex
@article{05_deepseek_r1_2025,
  title = {DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
  author = {DeepSeek-AI},
  journal = {arXiv preprint arXiv:2501.12948},
  year = {2025},
  url = {https://arxiv.org/abs/2501.12948}
}
```
