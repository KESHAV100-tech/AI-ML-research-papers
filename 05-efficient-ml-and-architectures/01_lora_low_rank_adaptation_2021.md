# LoRA: Low-Rank Adaptation of Large Language Models

<div align="center">

[![Year](https://img.shields.io/badge/Year-2021-blue?style=for-the-badge)](https://arxiv.org/abs/2106.09685)
[![Venue](https://img.shields.io/badge/Venue-ICLR%202022-purple?style=for-the-badge)](https://arxiv.org/abs/2106.09685)
[![arXiv](https://img.shields.io/badge/arXiv-2106.09685-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2106.09685)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2106.09685.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/microsoft/LoRA)

</div>

---

### 📋 Paper Metadata

- **Authors:** Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen
- **Publication Year:** 2021
- **Venue:** ICLR 2022
- **Primary arXiv ID:** [`arXiv:2106.09685`](https://arxiv.org/abs/2106.09685)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2106.09685.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/microsoft/LoRA)

---

### 📖 Executive Abstract

> "An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks. However, as models grow larger, full fine-tuning becomes prohibitive. We propose Low-Rank Adaptation (LoRA), which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture."

---

### 🎯 Core Problem & Motivation

Full parameter fine-tuning of 175B LLMs required storing gigabytes of optimizer states per task and deploying completely separate model copies for each client application.

---

### 💡 Key Innovations & Architecture

1. **Rank Decomposition Hypothesis**: Hypothesized that parameter updates $\Delta W$ have a low 'intrinsic dimension' during task adaptation.
2. **Factorized Matrices**: Represented updates as $\Delta W = B \cdot A$ where $B \in \mathbb{R}^{d \times r}$ and $A \in \mathbb{R}^{r \times k}$ with rank $r \ll \min(d, k)$.
3. **Zero Inference Latency**: At deployment, $\Delta W$ can be directly folded into base weights $W_0$, adding zero inference overhead.
4. **Vast Efficiency**: Reduced trainable parameters by 10,000x and GPU memory consumption by 3x.

---

### 📐 Mathematical Formulation

**Forward Pass with LoRA:**
$$h = W_0 x + \Delta W x = W_0 x + \frac{\alpha}{r} B A x$$
Where $A \sim \mathcal{N}(0, \sigma^2)$ and $B = 0$ at initialization, ensuring $\Delta W = 0$ at step 0.

---

### 🌟 Significance & Industry Impact

The standard fine-tuning method across all of machine learning. Enables individuals and enterprises to customize multi-billion parameter models on modest GPUs in hours.

---

### 📚 BibTeX Citation

```bibtex
@article{01_lora_low_rank_adaptation_2021,
  title = {LoRA: Low-Rank Adaptation of Large Language Models},
  author = {Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen},
  journal = {arXiv preprint arXiv:2106.09685},
  year = {2021},
  url = {https://arxiv.org/abs/2106.09685}
}
```
