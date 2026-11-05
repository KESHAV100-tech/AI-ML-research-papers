# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2201.11903)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2201.11903)
[![arXiv](https://img.shields.io/badge/arXiv-2201.11903-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2201.11903)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2201.11903.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jasonwei20/chain-of-thought-prompting)

</div>

---

### 📋 Paper Metadata

- **Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou
- **Publication Year:** 2022
- **Venue:** NeurIPS 2022
- **Primary arXiv ID:** [`arXiv:2201.11903`](https://arxiv.org/abs/2201.11903)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2201.11903.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/jasonwei20/chain-of-thought-prompting)

---

### 📖 Executive Abstract

> "We explore how generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting."

---

### 🎯 Core Problem & Motivation

Standard zero-shot or few-shot prompting required models to output direct answers immediately, causing failure on multi-step reasoning tasks (grade-school math, symbolic logic, multi-hop QA).

---

### 💡 Key Innovations & Architecture

1. **Step-by-Step Prompting**: Provided exemplars demonstrating step-by-step rationales leading to the final answer.
2. **Emergent Property of Scale**: Found that Chain-of-Thought provides minimal benefit for models $<10\text{B}$ parameters, but yields massive performance leaps at $\ge 100\text{B}$ parameters.
3. **GSM8K Breakthrough**: Boosted PaLM 540B benchmark accuracy on GSM8K math reasoning from 17.9% to 56.9% without any parameter fine-tuning.

---

### 📐 Mathematical Formulation

**Standard Prediction vs CoT:**
$$\text{Standard: } P(\text{Answer} \mid \text{Question})$$
$$\text{Chain-of-Thought: } P(\text{Thought}_1, \dots, \text{Thought}_K, \text{Answer} \mid \text{Question}) = \left( \prod_{k=1}^K P(T_k \mid Q, T_{<k}) \right) P(A \mid Q, T)$$

---

### 🌟 Significance & Industry Impact

Triggered the modern era of test-time compute scaling and reasoning models. Inspired 'Let's think step by step', scratchpads, and eventually OpenAI o1 and DeepSeek-R1.

---

### 📚 BibTeX Citation

```bibtex
@article{03_chain_of_thought_2022,
  title = {Chain-of-Thought Prompting Elicits Reasoning in Large Language Models},
  author = {Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou},
  journal = {arXiv preprint arXiv:2201.11903},
  year = {2022},
  url = {https://arxiv.org/abs/2201.11903}
}
```
