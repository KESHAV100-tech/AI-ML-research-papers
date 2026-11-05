# Contributing to AI/ML Research Papers Hub

Thank you for your interest in contributing to this repository! We welcome additions of new landmark papers, improvements to mathematical derivations, and tooling enhancements.

---

## 📌 Guidelines for Adding a New Research Paper

When contributing a new paper, follow this standardized structure:

1. **Category Selection**: Place the markdown file in the appropriate domain folder:
   - `01-foundational-architectures/`
   - `02-large-language-models/`
   - `03-reasoning-and-alignment/`
   - `04-generative-and-diffusion/`
   - `05-efficient-ml-and-architectures/`
   - `06-multimodal-and-vision-language/`
   - `07-reinforcement-learning/`

2. **File Naming Convention**:
   Format: `<index>_<paper_slug>_<year>.md`
   Example: `07_deepseek_r1_2025.md`

3. **Required Sections**:
   - Header Badges (Year, Venue, arXiv, PDF, Code)
   - Paper Metadata (Authors, Publication Year, Venue, arXiv Link, Code Link)
   - Executive Abstract
   - Core Problem & Motivation
   - Key Innovations & Architecture
   - Mathematical Formulation (KaTeX formatted equations)
   - Significance & Industry Impact
   - BibTeX Citation

4. **Update Catalog & Citations**:
   - Add the paper entry to `PAPERS_CATALOG` in `scripts/paper_manager.py`.
   - Run `python scripts/paper_manager.py export-bib` to update `citations.bib`.
   - Add the paper to the master table in `README.md`.
