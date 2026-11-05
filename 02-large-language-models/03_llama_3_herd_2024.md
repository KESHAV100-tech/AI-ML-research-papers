# The Llama 3 Herd of Models

<div align="center">

[![Year](https://img.shields.io/badge/Year-2024-blue?style=for-the-badge)](https://arxiv.org/abs/2407.21783)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2407.21783)
[![arXiv](https://img.shields.io/badge/arXiv-2407.21783-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2407.21783)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2407.21783.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/meta-llama/llama3)

</div>

---

### 📋 Paper Metadata

- **Authors:** Abhimanyu Dubey, Jiahui Yu, et al., Meta AI
- **Publication Year:** 2024
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2407.21783`](https://arxiv.org/abs/2407.21783)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2407.21783.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/meta-llama/llama3)

---

### 📖 Executive Abstract

> "We introduce Llama 3, a new herd of foundation language models that support multilinguality, coding, reasoning, and tool usage. Our largest model is a 405B parameter dense transformer with a context length of 128K tokens that performs comparably to leading frontier models such as GPT-4."

---

### 🎯 Core Problem & Motivation

Previous open models lagged closed frontier models (GPT-4, Claude 3 Opus) on complex reasoning, coding, long context, and multi-turn instruction following.

---

### 💡 Key Innovations & Architecture

1. **Scale**: Pre-trained on over 15 trillion tokens with a 128,000-token context window across 8B, 70B, and 405B parameters.
2. **Grouped-Query Attention (GQA)**: Applied GQA across all model sizes to reduce KV cache memory footprints during long-context inference.
3. **Iterative Post-Training**: Combined multiple rounds of Direct Preference Optimization (DPO), Rejection Sampling, and Supervised Fine-Tuning (SFT) with synthetic data generation.

---

### 📐 Mathematical Formulation

**Grouped-Query Attention (GQA):**
$$\text{Ratio} = \frac{H_Q}{H_{KV}}$$
Where $H_Q$ query heads share $H_{KV}$ key-value heads ($H_{KV} \ll H_Q$). For Llama 3, 8 key-value heads serve 64 query heads (8:1 ratio), slashing KV cache memory by 87.5%.

---

### 🌟 Significance & Industry Impact

Llama 3 405B became the first open-weights model to achieve competitive parity with leading proprietary frontier models on key benchmarks (MMLU, MATH, HumanEval).

---

### 📚 BibTeX Citation

```bibtex
@article{03_llama_3_herd_2024,
  title = {The Llama 3 Herd of Models},
  author = {Abhimanyu Dubey, Jiahui Yu, et al., Meta AI},
  journal = {arXiv preprint arXiv:2407.21783},
  year = {2024},
  url = {https://arxiv.org/abs/2407.21783}
}
```
