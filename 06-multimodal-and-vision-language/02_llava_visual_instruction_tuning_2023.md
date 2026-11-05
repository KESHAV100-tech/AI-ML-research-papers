# Visual Instruction Tuning (LLaVA)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2023-blue?style=for-the-badge)](https://arxiv.org/abs/2304.08485)
[![Venue](https://img.shields.io/badge/Venue-NeurIPS%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2304.08485)
[![arXiv](https://img.shields.io/badge/arXiv-2304.08485-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2304.08485)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2304.08485.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/haotian-liu/LLaVA)

</div>

---

### 📋 Paper Metadata

- **Authors:** Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee
- **Publication Year:** 2023
- **Venue:** NeurIPS 2023
- **Primary arXiv ID:** [`arXiv:2304.08485`](https://arxiv.org/abs/2304.08485)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2304.08485.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/haotian-liu/LLaVA)

---

### 📖 Executive Abstract

> "Instruction tuning large language models (LLMs) has shown promising results in boosting their zero-shot capabilities on new tasks. We present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on this generated data, we introduce LLaVA (Large Language and Vision Assistant)."

---

### 🎯 Core Problem & Motivation

Vision-language models were trained primarily on simple captioning or VQA benchmarks, failing to follow complex, conversational visual instructions.

---

### 💡 Key Innovations & Architecture

1. **Synthetic Multimodal Data Pipeline**: Leveraged GPT-4 with symbolic bounding box prompts to synthesize 158K conversational visual instruction pairs.
2. **Elegant Projection Architecture**: Linked a frozen CLIP ViT-L/14 visual encoder to an autoregressive Vicuna/LLaMA decoder via a single linear projection matrix.
3. **End-to-End Fine-Tuning**: Froze the vision encoder while fine-tuning the projection layer and language model on multimodal conversations.

---

### 📐 Mathematical Formulation

**Multimodal Token Concatenation:**
$$H_v = W \cdot Z_v, \quad \text{where } Z_v = g(X_v)$$
$$P(Y \mid X_v, X_q) = \prod_{i=1}^L P(y_i \mid H_v, X_{q,<i}, Y_{<i})$$

---

### 🌟 Significance & Industry Impact

Provided the foundational architecture and training recipe for modern open-source Vision-Language Models (VLMs), enabling visual chatting, document analysis, and GUI automation.

---

### 📚 BibTeX Citation

```bibtex
@article{02_llava_visual_instruction_tuning_2023,
  title = {Visual Instruction Tuning (LLaVA)},
  author = {Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee},
  journal = {arXiv preprint arXiv:2304.08485},
  year = {2023},
  url = {https://arxiv.org/abs/2304.08485}
}
```
