# Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)

<div align="center">

[![Year](https://img.shields.io/badge/Year-2022-blue?style=for-the-badge)](https://arxiv.org/abs/2212.04356)
[![Venue](https://img.shields.io/badge/Venue-ICML%202023-purple?style=for-the-badge)](https://arxiv.org/abs/2212.04356)
[![arXiv](https://img.shields.io/badge/arXiv-2212.04356-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2212.04356)
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2212.04356.pdf)
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/openai/whisper)

</div>

---

### 📋 Paper Metadata

- **Authors:** Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever
- **Publication Year:** 2022
- **Venue:** ICML 2023
- **Primary arXiv ID:** [`arXiv:2212.04356`](https://arxiv.org/abs/2212.04356)
- **PDF Direct Download:** [Click to Read Official PDF](https://arxiv.org/pdf/2212.04356.pdf)
- **Reference Implementation:** [GitHub Repository](https://github.com/openai/whisper)

---

### 📖 Executive Abstract

> "We study the robustness of speech recognition systems trained simply to predict large amounts of transcripts of audio on the internet. By scaling weakly supervised speech recognition to 680,000 hours of labeled audio data, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results."

---

### 🎯 Core Problem & Motivation

Speech recognition models trained on supervised academic datasets (LibriSpeech) failed drastically when faced with real-world accents, background noise, and colloquial speech.

---

### 💡 Key Innovations & Architecture

1. **Weak Supervision at Scale**: Trained an encoder-decoder Transformer on 680,000 hours of diverse multilingual audio scraped from the web.
2. **Multitask Sequence Format**: Expressed voice activity detection, language identification, timestamp estimation, and translation into English as a unified autoregressive token prediction task.
3. **Out-of-the-Box Zero-Shot Robustness**: Achieved near-human speech recognition accuracy across noisy, conversational environments without dataset fine-tuning.

---

### 📐 Mathematical Formulation

**Whisper Multitask Token Target:**
$$\text{Target} = [\langle|\text{startoftranscript}|\rangle, \langle|\text{language}|\rangle, \langle|\text{transcribe}|\rangle, \langle|\text{notimestamps}|\rangle, \text{Tokens}\dots, \langle|\text{endoftranscript}|\rangle]$$

---

### 🌟 Significance & Industry Impact

Became the world standard speech-to-text model, powering transcription in millions of consumer, medical, and developer applications.

---

### 📚 BibTeX Citation

```bibtex
@article{04_whisper_speech_recognition_2022,
  title = {Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)},
  author = {Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever},
  journal = {arXiv preprint arXiv:2212.04356},
  year = {2022},
  url = {https://arxiv.org/abs/2212.04356}
}
```
