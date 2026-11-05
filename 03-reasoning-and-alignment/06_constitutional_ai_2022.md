# Constitutional AI: Harmlessness from AI Feedback (RLAIF)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2212.08073)
[![Venue](https://img.shields.io/badge/Venue-arXiv%20Preprint-purple?style=for-the-badge)](https://arxiv.org/abs/2212.08073)
[![arXiv](https://img.shields.io/badge/arXiv-2212.08073-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2212.08073)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2212.08073.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/anthropics/constitutional-ai)

</div>

---

### 📋 Paper Metadata

- **Authors:** Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, John Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Jared Kaplan, Christopher Berner
- **Publication Year:** 2022
- **Venue:** arXiv Preprint
- **Primary arXiv ID:** [`arXiv:2212.08073`](https://arxiv.org/abs/2212.08073)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2212.08073.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/anthropics/constitutional-ai)

---

### 📖 Executive Abstract

> "We explore methods for training a harmless AI assistant through self-improvement, without any human feedback labels for harmfulness. The only human oversight is provided through a list of principles or instructions (a constitution). The process involves both a supervised learning phase (critique and revision) and a reinforcement learning phase (RL from AI Feedback - RLAIF)."

---

### 🎯 Core Problem & Motivation

RLHF relies on human annotators reviewing hundreds of thousands of toxic, disturbing, or sensitive outputs, creating severe psychological distress for crowdworkers and high economic expense.

---

### 💡 Key Innovations & Architecture

1. **Written Constitution**: Set of concise principles drawn from the Universal Declaration of Human Rights and safety guidelines.
2. **Critique and Revision (SL Phase)**: The model generates responses, critiques its own output against constitutional principles, and rewrites the response.
3. **RL from AI Feedback (RLAIF)**: Replaced human pairwise preference judges with a constitutional AI evaluator model.

---

### 📐 Mathematical Formulation

**Constitutional Critique Prompt:**
$$\text{Response} \xrightarrow{\text{Principle } C_k} \text{Critique} \xrightarrow{\text{Revision}} \text{Revised Response}$$

**RLAIF Preference Scoring:**
$$P(y_1 \succ y_2 \mid x, C) = \text{LLM}_{\text{judge}}(\text{Is } y_1 \text{ more helpful/harmless according to } C?)$$

---

### 🌟 Significance & Industry Impact

Serves as the foundational alignment methodology behind Anthropic's Claude series, proving that AI models can self-align toward safety without degrading helpfulness.

---

### 📚 BibTeX Citation

```bibtex
@article{06_constitutional_ai_2022,
  title = {Constitutional AI: Harmlessness from AI Feedback (RLAIF)},
  author = {Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, John Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Jared Kaplan, Christopher Berner},
  journal = {arXiv preprint arXiv:2212.08073},
  year = {2022},
  url = {https://arxiv.org/abs/2212.08073}
}
```
