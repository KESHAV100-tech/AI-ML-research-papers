# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

<div align="center">

[![Year](https://img.shields.io/badge/Year-2023-blue?style=for-the-badge)](https://arxiv.org/abs/2305.10601)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2305.10601)
[![arXiv](https://img.shields.io/badge/arXiv-2305.10601-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.10601)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2305.10601.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/princeton-nlp/tree-of-thought-llm)

</div>

---

### 📋 Paper Metadata

- **Authors:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- **Publication Year:** 2023
- **Venue:** NeurIPS 2023
- **Primary arXiv ID:** [`arXiv:2305.10601`](https://arxiv.org/abs/2305.10601)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2305.10601.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/princeton-nlp/tree-of-thought-llm)

---

### 📖 Executive Abstract

> "Popular language models are confined to token-level, left-to-right decision-making processes during inference. We introduce Tree of Thoughts (ToT), which generalizes over Chain of Thought prompting and encourages exploration over thoughts that serve as intermediate steps toward problem solving."

---

### 🎯 Core Problem & Motivation

Chain-of-thought is linear and greedy; if an LLM makes an error early in the chain, it cannot backtrack, look ahead, or evaluate alternative paths.

---

### 💡 Key Innovations & Architecture

1. **Tree Exploration**: Frames reasoning as search through a tree where each node is a coherent unit of thought (a sentence or equation).
2. **Search Algorithms**: Employs classical graph search algorithms (Breadth-First Search, Depth-First Search, A*) over thoughts.
3. **Self-Evaluation**: Uses the LLM itself as a heuristic evaluator to judge the promise of candidate thought states (e.g., 'sure', 'maybe', 'impossible').

---

### 📐 Mathematical Formulation

**ToT State Transition & Heuristic Value:**
$$s_{t+1} = [s_t, z^{(i)}], \quad z^{(i)} \sim \text{LLM}(\text{GenerateThoughts}(s_t))$$
$$V(s) = \text{LLM}(\text{EvaluateState}(s)) \in [0, 1]$$

---

### 🌟 Significance & Industry Impact

Formalized search and planning with LLMs, laying the groundwork for AI agents, Monte Carlo Tree Search (MCTS) reasoning frameworks, and test-time verification loops.

---

### 📚 BibTeX Citation

```bibtex
@article{04_tree_of_thoughts_2023,
  title = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  author = {Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan},
  journal = {arXiv preprint arXiv:2305.10601},
  year = {2023},
  url = {https://arxiv.org/abs/2305.10601}
}
```
