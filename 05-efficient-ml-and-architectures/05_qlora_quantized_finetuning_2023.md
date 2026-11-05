# QLoRA: Efficient Finetuning of Quantized LLMs

<div align="center">

[![Year](https://img.shields.io/badge/Year-2023-blue?style=for-the-badge)](https://arxiv.org/abs/2305.14314)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2305.14314)
[![arXiv](https://img.shields.io/badge/arXiv-2305.14314-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.14314)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2305.14314.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/artidoro/qlora)

</div>

---

### 📋 Paper Metadata

- **Authors:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- **Publication Year:** 2023
- **Venue:** NeurIPS 2023
- **Primary arXiv ID:** [`arXiv:2305.14314`](https://arxiv.org/abs/2305.14314)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2305.14314.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/artidoro/qlora)

---

### 📖 Executive Abstract

> "We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters."

---

### 🎯 Core Problem & Motivation

Finetuning large foundation models (65B) previously required multi-GPU server clusters with 80GB A100s, locking independent researchers and small labs out of fine-tuning.

---

### 💡 Key Innovations & Architecture

1. **4-bit NormalFloat (NF4)**: An information-theoretically optimal quantile quantization data type for normally distributed neural weights.
2. **Double Quantization (DQ)**: Quantized the quantization constants themselves, saving 0.37 bits per parameter (~3GB for a 65B model).
3. **Paged Optimizers**: Used CUDA unified memory to manage memory spikes during activation gradient updates without out-of-memory crashes.

---

### 📐 Mathematical Formulation

**NF4 Quantization Form:**
$$q_i = \text{sign}(w_i) \cdot Q_X^{-1}\left( \frac{i}{2^k + 1} \right)$$
Where $Q_X$ is the empirical cumulative distribution function of a standard normal distribution $\mathcal{N}(0, 1)$.

---

### 🌟 Significance & Industry Impact

Democratized state-of-the-art model tuning, allowing consumer-grade workstations (RTX 3090/4090) to fine-tune 70B models.

---

### 📚 BibTeX Citation

```bibtex
@article{05_qlora_quantized_finetuning_2023,
  title = {QLoRA: Efficient Finetuning of Quantized LLMs},
  author = {Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer},
  journal = {arXiv preprint arXiv:2305.14314},
  year = {2023},
  url = {https://arxiv.org/abs/2305.14314}
}
```
