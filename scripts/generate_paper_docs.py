#!/usr/bin/env python3
"""
Generator for detailed Markdown notes for all seminal AI/ML papers.
"""
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent

PAPERS_DETAIL = [
    # --- 01 Foundational Architectures ---
    {
        "category": "01-foundational-architectures",
        "filename": "01_alexnet_2012.md",
        "title": "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)",
        "authors": "Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton",
        "year": "2012",
        "venue": "NeurIPS 2012",
        "arxiv_id": "1206.5538",
        "arxiv_url": "https://arxiv.org/abs/1206.5538",
        "pdf_url": "https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf",
        "code_url": "https://github.com/akrizhevsky/cuda-convnet2",
        "abstract": "We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art.",
        "problem": "Prior to 2012, visual recognition relied on hand-crafted feature extractors (SIFT, HOG) coupled with linear classifiers or SVMs. These methods hit a severe performance plateau on large-scale, diverse real-world images.",
        "innovations": """1. **GPU Acceleration**: Implemented highly optimized 2D convolutions on dual NVIDIA GTX 580 GPUs with cross-GPU communication.
2. **ReLU Non-Linearity**: Replaced standard sigmoid/tanh activations with Rectified Linear Units ($f(x) = \\max(0, x)$), speeding up convergence by 6x.
3. **Dropout Regularization**: Introduced 0.5 dropout probability in fully connected layers to prevent co-adaptation of features.
4. **Data Augmentation**: Applied real-time image translations, horizontal reflections, and PCA color jittering.""",
        "math": """**ReLU Activation Function:**
$$f(x) = \\max(0, x)$$

**Local Response Normalization (LRN):**
$$b_{x,y}^i = a_{x,y}^i / \\left( k + \\alpha \\sum_{j=\\max(0, i-n/2)}^{\\min(N-1, i+n/2)} (a_{x,y}^j)^2 \\right)^\\beta$$""",
        "impact": "AlexNet won ImageNet LSVRC-2012 by an unprecedented margin of 10.8 percentage points, convincing the entire AI community that deep neural networks trained on GPUs are the path forward. It triggered the modern Deep Learning revolution."
    },
    {
        "category": "01-foundational-architectures",
        "filename": "02_resnet_2015.md",
        "title": "Deep Residual Learning for Image Recognition (ResNet)",
        "authors": "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun",
        "year": "2015",
        "venue": "CVPR 2016 (Best Paper Award)",
        "arxiv_id": "1512.03385",
        "arxiv_url": "https://arxiv.org/abs/1512.03385",
        "pdf_url": "https://arxiv.org/pdf/1512.03385.pdf",
        "code_url": "https://github.com/KaimingHe/deep-residual-networks",
        "abstract": "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.",
        "problem": "As neural networks grew beyond 20-30 layers, training error worsened due to the 'degradation problem'—not simply vanishing/exploding gradients, but optimization difficulty where deeper networks failed to even learn identity mappings.",
        "innovations": """1. **Residual Shortcut Connections**: Formulated stacked layers to learn $F(x) = H(x) - x$ instead of direct mapping $H(x)$, allowing identity pass-through.
2. **Extreme Depth**: Successfully trained networks with 50, 101, and 152 layers (and explored up to 1202 layers on CIFAR).
3. **Bottleneck Block Design**: Used $1 \\times 1$, $3 \\times 3$, and $1 \\times 1$ convolutions to dramatically reduce parameter count and computational complexity while maintaining representational capacity.""",
        "math": """**Residual Mapping Formulation:**
$$y = \\mathcal{F}(x, \\{W_i\\}) + x$$
Where $x$ and $y$ are input and output vectors, and $\\mathcal{F}$ represents the residual function to be learned.

**Gradient Flow Backpropagation:**
$$\\frac{\\partial \\mathcal{E}}{\\partial x_l} = \\frac{\\partial \\mathcal{E}}{\\partial x_L} \\left( 1 + \\frac{\\partial}{\\partial x_l} \\sum_{i=l}^{L-1} \\mathcal{F}(x_i, W_i) \\right)$$
Notice the additive $+1$ term guarantees that gradients flow back directly to early layers without attenuation!""",
        "impact": "ResNet achieved a 3.57% top-5 error on ImageNet, surpassing human performance for the first time. Residual connections became an indispensable building block in almost every modern neural architecture, including Transformers."
    },
    {
        "category": "01-foundational-architectures",
        "filename": "03_attention_is_all_you_need_2017.md",
        "title": "Attention Is All You Need (Transformer)",
        "authors": "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin",
        "year": "2017",
        "venue": "NeurIPS 2017",
        "arxiv_id": "1706.03762",
        "arxiv_url": "https://arxiv.org/abs/1706.03762",
        "pdf_url": "https://arxiv.org/pdf/1706.03762.pdf",
        "code_url": "https://github.com/tensorflow/tensor2tensor",
        "abstract": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.",
        "problem": "Recurrent neural networks (RNNs, LSTMs, GRUs) process tokens sequentially, creating an inherently non-parallelizable bottleneck ($O(N)$ sequential operations) and struggling with long-range dependency retention due to gradient decay.",
        "innovations": """1. **Self-Attention Mechanism**: Direct $O(1)$ path length between any two tokens in a sequence regardless of distance.
2. **Multi-Head Attention**: Allows the model to jointly attend to information from different representation subspaces at different positions.
3. **Fully Parallelizable Training**: Entire sequences are processed simultaneously in matrix multiplications on GPUs/TPUs.
4. **Positional Encodings**: Injected sinusoids into embeddings to supply token order information.""",
        "math": """**Scaled Dot-Product Attention:**
$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left( \\frac{Q K^T}{\\sqrt{d_k}} \\right) V$$

**Multi-Head Attention:**
$$\\text{MultiHead}(Q, K, V) = \\text{Concat}(\\text{head}_1, \\dots, \\text{head}_h) W^O$$
$$\\text{where } \\text{head}_i = \\text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$""",
        "impact": "The Transformer is arguably the most influential AI architecture of the 21st century. It obsoleted recurrent models in NLP and became the universal backbone for GPT, BERT, Claude, Gemini, LLaMA, ViT, AlphaFold, and Sora."
    },
    {
        "category": "01-foundational-architectures",
        "filename": "04_bert_2018.md",
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "authors": "Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova",
        "year": "2018",
        "venue": "NAACL 2019 (Best Long Paper)",
        "arxiv_id": "1810.04805",
        "arxiv_url": "https://arxiv.org/abs/1810.04805",
        "pdf_url": "https://arxiv.org/pdf/1810.04805.pdf",
        "code_url": "https://github.com/google-research/bert",
        "abstract": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.",
        "problem": "Standard language models were unidirectional (left-to-right), which severely handicapped tasks requiring bidirectional context understanding (such as question answering, named entity recognition, and sentiment classification).",
        "innovations": """1. **Masked Language Modeling (MLM)**: Masking 15% of input tokens at random and training the model to predict the original tokens based on bidirectional context.
2. **Next Sentence Prediction (NSP)**: Binary classification task predicting whether sentence B logically follows sentence A.
3. **Fine-Tuning Paradigm**: A single pre-trained BERT model could be fine-tuned with just one additional output layer across 11 diverse NLP benchmarks.""",
        "math": """**Masked Token Prediction Loss:**
$$\\mathcal{L}_{\\text{MLM}}(\\theta) = - \\sum_{i \\in \\text{Masked}} \\log P(x_i \\mid X_{\\setminus i}; \\theta)$$

**Combined Pre-training Loss:**
$$\\mathcal{L} = \\mathcal{L}_{\\text{MLM}} + \\mathcal{L}_{\\text{NSP}}$$""",
        "impact": "Swept the GLUE benchmark with a score of 80.5% and SQuAD 1.1 with 93.2% accuracy. BERT established the 'pre-train then fine-tune' paradigm that powered enterprise search engines (including Google Search) and production NLP pipelines."
    },
    {
        "category": "01-foundational-architectures",
        "filename": "05_gpt3_2020.md",
        "title": "Language Models are Few-Shot Learners (GPT-3)",
        "authors": "Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei",
        "year": "2020",
        "venue": "NeurIPS 2020",
        "arxiv_id": "2005.14165",
        "arxiv_url": "https://arxiv.org/abs/2005.14165",
        "pdf_url": "https://arxiv.org/pdf/2005.14165.pdf",
        "code_url": "https://github.com/openai/gpt-3",
        "abstract": "We train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks specified purely via text interaction with the model.",
        "problem": "Fine-tuning models for each downstream task required thousands of labeled examples per domain, risking task-specific overfitting and poor generalization to unseen instructions.",
        "innovations": """1. **Massive Scale**: Scaled autoregressive dense transformers to 175 billion parameters across 96 layers and 96 attention heads.
2. **In-Context Learning (ICL)**: Discovered that model scale unlocks the ability to perform zero-shot, one-shot, and few-shot tasks without updating model weights.
3. **Diverse Pre-training Dataset**: Filtered Common Crawl combined with WebText2, Books1, Books2, and Wikipedia (300 billion tokens total).""",
        "math": """**Autoregressive Language Modeling Likelihood:**
$$\\mathcal{L}(\\theta) = - \\sum_{i=1}^n \\log P(x_i \\mid x_1, x_2, \\dots, x_{i-1}; \\theta)$$

**In-Context Prompting Conditioning:**
$$P(\\text{Target} \\mid \\text{Prompt}) = \\prod_{t=1}^T P(y_t \\mid x_{\\text{examples}}, x_{\\text{query}}, y_{<t})$$""",
        "impact": "Marked the paradigm shift from task-specific fine-tuning to unified prompt engineering and foundation models. Showed that language models are general-purpose computer programs that can be guided via natural language."
    },
    {
        "category": "01-foundational-architectures",
        "filename": "06_vision_transformer_vit_2020.md",
        "title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)",
        "authors": "Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby",
        "year": "2020",
        "venue": "ICLR 2021",
        "arxiv_id": "2010.11929",
        "arxiv_url": "https://arxiv.org/abs/2010.11929",
        "pdf_url": "https://arxiv.org/pdf/2010.11929.pdf",
        "code_url": "https://github.com/google-research/vision_transformer",
        "abstract": "While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks.",
        "problem": "Convolutions have strong built-in inductive biases (translation equivariance, locality). While helpful on small datasets, these biases limit peak capacity when massive amounts of training data are available.",
        "innovations": """1. **Patch Flattening & Embedding**: Sliced 2D images into non-overlapping $16 \\times 16$ or $14 \\times 14$ patches and flattened them into 1D token embeddings.
2. **Prepend Learnable [CLS] Token**: Added a learnable classification token whose state at the output serves as the image representation.
3. **Scale-Dependent Performance**: Demonstrated that while CNNs outperform ViT on small datasets (ImageNet-1K), ViT overtakes CNNs decisively when pre-trained on JFT-300M.""",
        "math": """**Linear Patch Projection:**
$$z_0 = [x_{\\text{class}}; x_p^1 E; x_p^2 E; \\dots; x_p^N E] + E_{\\text{pos}}$$
Where $x_p^i \\in \\mathbb{R}^{P^2 \\cdot C}$ is patch $i$, $E \\in \\mathbb{R}^{(P^2 C) \\times D}$ is the patch projection matrix, and $E_{\\text{pos}}$ is the 1D position embedding.""",
        "impact": "Eliminated the domain gap between computer vision and natural language processing, making Transformers the unified modality backbone across text, vision, audio, and multimodal foundation models."
    },

    # --- 02 Large Language Models & Scaling ---
    {
        "category": "02-large-language-models",
        "filename": "01_chinchilla_scaling_laws_2022.md",
        "title": "Training Compute-Optimal Large Language Models (Chinchilla)",
        "authors": "Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre",
        "year": "2022",
        "venue": "NeurIPS 2022",
        "arxiv_id": "2203.15556",
        "arxiv_url": "https://arxiv.org/abs/2203.15556",
        "pdf_url": "https://arxiv.org/pdf/2203.15556.pdf",
        "code_url": "https://github.com/google-deepmind",
        "abstract": "We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant.",
        "problem": "Earlier scaling laws (Kaplan et al., 2020) concluded that parameter count should scale much faster than dataset size ($N \\propto C^{0.73}$, $D \\propto C^{0.27}$), leading companies to train massive models (Gopher 280B, GPT-3 175B) on relatively small datasets (~300B tokens).",
        "innovations": """1. **Empirical Evaluation Over 400 Models**: Trained models from 70M to 16B parameters on varying token budgets.
2. **Compute-Optimal Ratio**: Proved that parameters and tokens should scale in **equal proportion**: $N \\propto C^{0.5}$ and $D \\propto C^{0.5}$.
3. **Chinchilla 70B**: Trained a 70B model on 1.4T tokens (4x more tokens than Gopher), outperforming Gopher (280B), GPT-3 (175B), and Jurassic-1 (178B) while slashing inference costs.""",
        "math": """**Compute Budget Constraint:**
$$C \\approx 6 N D$$
Where $C$ is total FLOPs, $N$ is parameter count, and $D$ is training token count.

**Loss Parametrization:**
$$\\hat{L}(N, D) = E + \\frac{A}{N^\\alpha} + \\frac{B}{D^\\beta}$$
Under optimal compute allocation:
$$N_{\\text{opt}} \\propto C^{\\frac{\\beta}{\\alpha + \\beta}}, \\quad D_{\\text{opt}} \\propto C^{\\frac{\\alpha}{\\alpha + \\beta}}$$
With empirical findings $\\alpha \\approx 0.34$, $\\beta \\approx 0.28$, yielding $N \\propto C^{0.5}$ and $D \\propto C^{0.5}$.""",
        "impact": "Completely redefined model pre-training strategy across the industry. LLaMA, Mistral, and subsequent open-source models followed Chinchilla's recipe: train smaller, denser models on trillions of tokens for optimal inference latency."
    },
    {
        "category": "02-large-language-models",
        "filename": "02_llama_2023.md",
        "title": "LLaMA: Open and Efficient Foundation Language Models",
        "authors": "Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample",
        "year": "2023",
        "venue": "arXiv Preprint",
        "arxiv_id": "2302.13971",
        "arxiv_url": "https://arxiv.org/abs/2302.13971",
        "pdf_url": "https://arxiv.org/pdf/2302.13971.pdf",
        "code_url": "https://github.com/meta-llama/llama",
        "abstract": "We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets.",
        "problem": "Frontier LLMs (GPT-3, PaLM, Chinchilla) were closed, proprietary, and inaccessible to researchers, stifling reproducible academic research into alignment, robustness, and interpretability.",
        "innovations": """1. **Pre-normalization with RMSNorm**: Replaced LayerNorm with Root Mean Square Normalization for stable gradient flow.
2. **SwiGLU Activation Function**: Substituted standard ReLU/GELU with Swish-Gated Linear Units.
3. **Rotary Embeddings (RoPE)**: Adopted RoPE at every layer for better relative positional encoding.
4. **Public Dataset Training**: Showed that 1.4 trillion publicly available tokens could train a 13B model that outperforms GPT-3 (175B).""",
        "math": """**RMSNorm Normalization:**
$$\\bar{a}_i = \\frac{a_i}{\\text{RMS}(a)} g_i, \\quad \\text{where } \\text{RMS}(a) = \\sqrt{\\frac{1}{d} \\sum_{i=1}^d a_i^2}$$

**SwiGLU Activation:**
$$\\text{SwiGLU}(x, W, V, b, c) = \\text{Swish}(x W + b) \\otimes (x V + c)$$""",
        "impact": "Sparked the open-source LLM explosion. LLaMA's weights became the foundation for thousands of fine-tunes (Alpaca, Vicuna, WizardLM) and local AI runtimes (llama.cpp, Ollama)."
    },
    {
        "category": "02-large-language-models",
        "filename": "03_llama_3_herd_2024.md",
        "title": "The Llama 3 Herd of Models",
        "authors": "Abhimanyu Dubey, Jiahui Yu, et al., Meta AI",
        "year": "2024",
        "venue": "arXiv Preprint",
        "arxiv_id": "2407.21783",
        "arxiv_url": "https://arxiv.org/abs/2407.21783",
        "pdf_url": "https://arxiv.org/pdf/2407.21783.pdf",
        "code_url": "https://github.com/meta-llama/llama3",
        "abstract": "We introduce Llama 3, a new herd of foundation language models that support multilinguality, coding, reasoning, and tool usage. Our largest model is a 405B parameter dense transformer with a context length of 128K tokens that performs comparably to leading frontier models such as GPT-4.",
        "problem": "Previous open models lagged closed frontier models (GPT-4, Claude 3 Opus) on complex reasoning, coding, long context, and multi-turn instruction following.",
        "innovations": """1. **Scale**: Pre-trained on over 15 trillion tokens with a 128,000-token context window across 8B, 70B, and 405B parameters.
2. **Grouped-Query Attention (GQA)**: Applied GQA across all model sizes to reduce KV cache memory footprints during long-context inference.
3. **Iterative Post-Training**: Combined multiple rounds of Direct Preference Optimization (DPO), Rejection Sampling, and Supervised Fine-Tuning (SFT) with synthetic data generation.""",
        "math": """**Grouped-Query Attention (GQA):**
$$\\text{Ratio} = \\frac{H_Q}{H_{KV}}$$
Where $H_Q$ query heads share $H_{KV}$ key-value heads ($H_{KV} \\ll H_Q$). For Llama 3, 8 key-value heads serve 64 query heads (8:1 ratio), slashing KV cache memory by 87.5%.""",
        "impact": "Llama 3 405B became the first open-weights model to achieve competitive parity with leading proprietary frontier models on key benchmarks (MMLU, MATH, HumanEval)."
    },
    {
        "category": "02-large-language-models",
        "filename": "04_mixtral_of_experts_2024.md",
        "title": "Mixtral of Experts",
        "authors": "Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Sandeep Subramanian, Sophia Yang, Szymon Antoniak, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed",
        "year": "2024",
        "venue": "arXiv Preprint",
        "arxiv_id": "2401.04088",
        "arxiv_url": "https://arxiv.org/abs/2401.04088",
        "pdf_url": "https://arxiv.org/pdf/2401.04088.pdf",
        "code_url": "https://github.com/mistralai/mistral-src",
        "abstract": "We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model. Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (experts). For every token, at each layer, a router network selects two experts to process the current state and combine their outputs additively.",
        "problem": "Scaling dense models increases compute cost linearly per token during both training and inference, making high-parameter models slow and expensive to serve.",
        "innovations": """1. **Sparse MoE Architecture**: 8 experts per layer with top-2 token routing, activating only 13B parameters out of 47B total per token.
2. **High Inference Throughput**: Achieved the inference speed and operational cost of a 13B dense model while matching or outperforming LLaMA 2 70B.
3. **Long Context Window**: Supported native 32K context windows with flawless retrieval.""",
        "math": """**Top-2 Routing Gating Equation:**
$$y = \\sum_{i=1}^n G(x)_i E_i(x)$$
$$\\text{where } G(x) = \\text{Softmax}(\\text{TopK}(x \\cdot W_g, k=2))$$
$$\\text{TopK}(v, k)_i = \\begin{cases} v_i & \\text{if } v_i \\text{ is in top } k \\\\ -\\infty & \\text{otherwise} \\end{cases}$$""",
        "impact": "Demonstrated that sparse MoE models could be stable, performant, and efficiently served on commodity hardware, setting off an industry-wide transition toward MoE foundation architectures."
    },
    {
        "category": "02-large-language-models",
        "filename": "05_deepseek_v3_2024.md",
        "title": "DeepSeek-V3 Technical Report",
        "authors": "DeepSeek-AI",
        "year": "2024",
        "venue": "arXiv Preprint",
        "arxiv_id": "2412.19437",
        "arxiv_url": "https://arxiv.org/abs/2412.19437",
        "pdf_url": "https://arxiv.org/pdf/2412.19437.pdf",
        "code_url": "https://github.com/deepseek-ai/DeepSeek-V3",
        "abstract": "We present DeepSeek-V3, a strong Mixture-of-Experts language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, and achieves state-of-the-art performance trained for just $6 million USD.",
        "problem": "Serving multi-hundred-billion parameter models incurs unsustainable memory bandwidth overhead (KV cache bottleneck) and requires millions of GPU hours for training.",
        "innovations": """1. **Multi-Head Latent Attention (MLA)**: Compresses key-value heads into a low-dimensional latent space, reducing KV cache memory by over 93%.
2. **DeepSeekMoE with Fine-Grained Experts**: Employs 256 routed experts + 1 shared expert with top-8 routing, allowing richer specialization.
3. **Auxiliary-Loss-Free Load Balancing**: Balanced expert load using dynamic bias adjustments rather than auxiliary routing losses that hurt model capability.
4. **FP8 Mixed Precision Framework**: End-to-end FP8 training and communication routines reducing memory traffic and training cost.""",
        "math": """**MLA Key-Value Low-Rank Compression:**
$$c_t^{KV} = W^{DKV} h_t \\in \\mathbb{R}^{d_c}$$
$$k_t^C = W^{UK} c_t^{KV}, \\quad v_t^C = W^{UV} c_t^{KV}$$
During generation, only $c_t^{KV}$ needs to be cached rather than full keys and values!""",
        "impact": "Shocked the global AI ecosystem by delivering frontier performance on par with proprietary commercial models at less than 1/10th of the training budget ($6M USD on 2,048 H800 GPUs)."
    },
    {
        "category": "02-large-language-models",
        "filename": "06_gemma_models_2024.md",
        "title": "Gemma: Open Models Based on Gemini Research and Technology",
        "authors": "Gemma Team, Google DeepMind",
        "year": "2024",
        "venue": "arXiv Preprint",
        "arxiv_id": "2403.08295",
        "arxiv_url": "https://arxiv.org/abs/2403.08295",
        "pdf_url": "https://arxiv.org/pdf/2403.08295.pdf",
        "code_url": "https://github.com/google-deepmind/gemma",
        "abstract": "We present Gemma, a family of lightweight, state-of-the-art open models built from the same research and technology used to create the Gemini models. Gemma models demonstrate strong performance across academic benchmarks for language understanding, reasoning, and mathematics.",
        "problem": "Developers need lightweight, high-performance open models that can run locally on consumer workstations, laptops, or mobile devices while maintaining rigorous safety standards.",
        "innovations": """1. **Gemini Architectural Lineage**: Multi-Query Attention (2B) and Multi-Head Attention (7B) with GeGLU non-linearities and normalized embeddings.
2. **Rigorous Data Curation**: Pre-trained on up to 6T tokens of primarily English web data, mathematics, and code with extensive filtering for safety and quality.
3. **Advanced Alignment**: Comprehensive RLHF alignment with dual reward models focused on factuality and instruction adherence.""",
        "math": """**GeGLU Activation:**
$$\\text{GeGLU}(x, W, V) = \\text{GELU}(x W) \\otimes (x V)$$""",
        "impact": "Provided academic researchers and edge-device developers with compact, safety-aligned models running seamlessly on consumer hardware, Google Colab, and mobile devices."
    },

    # --- 03 Reasoning, Post-Training & Alignment ---
    {
        "category": "03-reasoning-and-alignment",
        "filename": "01_instructgpt_rlhf_2022.md",
        "title": "Training language models to follow instructions with human feedback (InstructGPT)",
        "authors": "Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe",
        "year": "2022",
        "venue": "NeurIPS 2022",
        "arxiv_id": "2203.02155",
        "arxiv_url": "https://arxiv.org/abs/2203.02155",
        "pdf_url": "https://arxiv.org/pdf/2203.02155.pdf",
        "code_url": "https://github.com/openai/following-instructions-human-feedback",
        "abstract": "Making language models bigger does not inherently make them better at following a user's intent. In this work, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. We apply Reinforcement Learning from Human Feedback (RLHF) to fine-tune GPT-3 to follow a broad class of written instructions.",
        "problem": "Pre-trained language models optimize next-token prediction on internet text, causing them to generate toxic, mendacious, hallucinatory, or unhelpful answers when given direct user instructions.",
        "innovations": """1. **Three-Step RLHF Pipeline**:
   - Step 1: Supervised Fine-Tuning (SFT) on human prompt-response demonstrations.
   - Step 2: Reward Model (RM) trained on pairwise human preference comparisons ($y_w \\succ y_l$).
   - Step 3: Reinforcement Learning policy optimization via PPO with a KL-divergence penalty.
2. **Alignment Generalization**: InstructGPT 1.3B was preferred by human labelers over the raw 175B GPT-3 model despite having 100x fewer parameters.""",
        "math": """**Reward Model Loss:**
$$\\text{loss}(\\theta) = - \\mathbb{E}_{(x, y_w, y_l)} \\left[ \\log \\sigma(r_\\theta(x, y_w) - r_\\theta(x, y_l)) \\right]$$

**PPO Objective with KL Penalty:**
$$\\text{obj}(\\phi) = \\mathbb{E}_{(x, y)} [r_\\theta(x, y) - \\beta D_{\\text{KL}}(\\pi_\\phi^{\\text{RL}}(y \\mid x) \\parallel \\pi^{\\text{SFT}}(y \\mid x))] + \\gamma \\mathbb{E}_x [\\log \\pi_\\phi^{\\text{RL}}(x)]$$""",
        "impact": "Directly birthed **ChatGPT**, the fastest-growing consumer application in history, and established RLHF as the standard alignment technology for commercial AI."
    },
    {
        "category": "03-reasoning-and-alignment",
        "filename": "02_direct_preference_optimization_2023.md",
        "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)",
        "authors": "Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn",
        "year": "2023",
        "venue": "NeurIPS 2023",
        "arxiv_id": "2305.18290",
        "arxiv_url": "https://arxiv.org/abs/2305.18290",
        "pdf_url": "https://arxiv.org/pdf/2305.18290.pdf",
        "code_url": "https://github.com/eric-mitchell/direct-preference-optimization",
        "abstract": "While RLHF is a powerful approach, it is complex and often unstable, fitting a reward model that is then optimized with reinforcement learning. We propose Direct Preference Optimization (DPO), which implicitly optimizes the same objective as RLHF (reward maximization with a KL penalty) with a simple binary cross-entropy loss directly on policy parameters.",
        "problem": "RLHF with PPO is notoriously unstable, computationally expensive (requiring 4 simultaneous models in memory: actor, critic, reference, reward), and sensitive to hyperparameters.",
        "innovations": """1. **Closed-Form Mapping**: Showed that the optimal policy under the Bradley-Terry preference model can be solved analytically for the implicit reward:
   $$r(x, y) = \\beta \\log \\frac{\\pi_\\theta(y \\mid x)}{\\pi_{\\text{ref}}(y \\mid x)}$$
2. **Single-Stage Optimization**: Discarded the separate reward model and reinforcement learning loop entirely, training directly on preference pairs via binary cross-entropy.
3. **Stability & Simplicity**: Training is as simple and stable as standard supervised fine-tuning.""",
        "math": """**DPO Loss Function:**
$$\\mathcal{L}_{\\text{DPO}}(\\pi_\\theta; \\pi_{\\text{ref}}) = - \\mathbb{E}_{(x, y_w, y_l)} \\left[ \\log \\sigma \\left( \\beta \\log \\frac{\\pi_\\theta(y_w \\mid x)}{\\pi_{\\text{ref}}(y_w \\mid x)} - \\beta \\log \\frac{\\pi_\\theta(y_l \\mid x)}{\\pi_{\\text{ref}}(y_l \\mid x)} \\right) \\right]$$""",
        "impact": "DPO became the dominant alignment method across open-source and industrial AI labs (used extensively in Llama 3, Mistral, and Zephyr), democratizing model alignment without complex RL infrastructure."
    },
    {
        "category": "03-reasoning-and-alignment",
        "filename": "03_chain_of_thought_2022.md",
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "authors": "Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou",
        "year": "2022",
        "venue": "NeurIPS 2022",
        "arxiv_id": "2201.11903",
        "arxiv_url": "https://arxiv.org/abs/2201.11903",
        "pdf_url": "https://arxiv.org/pdf/2201.11903.pdf",
        "code_url": "https://github.com/jasonwei20/chain-of-thought-prompting",
        "abstract": "We explore how generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting.",
        "problem": "Standard zero-shot or few-shot prompting required models to output direct answers immediately, causing failure on multi-step reasoning tasks (grade-school math, symbolic logic, multi-hop QA).",
        "innovations": """1. **Step-by-Step Prompting**: Provided exemplars demonstrating step-by-step rationales leading to the final answer.
2. **Emergent Property of Scale**: Found that Chain-of-Thought provides minimal benefit for models $<10\\text{B}$ parameters, but yields massive performance leaps at $\\ge 100\\text{B}$ parameters.
3. **GSM8K Breakthrough**: Boosted PaLM 540B benchmark accuracy on GSM8K math reasoning from 17.9% to 56.9% without any parameter fine-tuning.""",
        "math": """**Standard Prediction vs CoT:**
$$\\text{Standard: } P(\\text{Answer} \\mid \\text{Question})$$
$$\\text{Chain-of-Thought: } P(\\text{Thought}_1, \\dots, \\text{Thought}_K, \\text{Answer} \\mid \\text{Question}) = \\left( \\prod_{k=1}^K P(T_k \\mid Q, T_{<k}) \\right) P(A \\mid Q, T)$$""",
        "impact": "Triggered the modern era of test-time compute scaling and reasoning models. Inspired 'Let's think step by step', scratchpads, and eventually OpenAI o1 and DeepSeek-R1."
    },
    {
        "category": "03-reasoning-and-alignment",
        "filename": "04_tree_of_thoughts_2023.md",
        "title": "Tree of Thoughts: Deliberate Problem Solving with Large Language Models",
        "authors": "Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan",
        "year": "2023",
        "venue": "NeurIPS 2023",
        "arxiv_id": "2305.10601",
        "arxiv_url": "https://arxiv.org/abs/2305.10601",
        "pdf_url": "https://arxiv.org/pdf/2305.10601.pdf",
        "code_url": "https://github.com/princeton-nlp/tree-of-thought-llm",
        "abstract": "Popular language models are confined to token-level, left-to-right decision-making processes during inference. We introduce Tree of Thoughts (ToT), which generalizes over Chain of Thought prompting and encourages exploration over thoughts that serve as intermediate steps toward problem solving.",
        "problem": "Chain-of-thought is linear and greedy; if an LLM makes an error early in the chain, it cannot backtrack, look ahead, or evaluate alternative paths.",
        "innovations": """1. **Tree Exploration**: Frames reasoning as search through a tree where each node is a coherent unit of thought (a sentence or equation).
2. **Search Algorithms**: Employs classical graph search algorithms (Breadth-First Search, Depth-First Search, A*) over thoughts.
3. **Self-Evaluation**: Uses the LLM itself as a heuristic evaluator to judge the promise of candidate thought states (e.g., 'sure', 'maybe', 'impossible').""",
        "math": """**ToT State Transition & Heuristic Value:**
$$s_{t+1} = [s_t, z^{(i)}], \\quad z^{(i)} \\sim \\text{LLM}(\\text{GenerateThoughts}(s_t))$$
$$V(s) = \\text{LLM}(\\text{EvaluateState}(s)) \\in [0, 1]$$""",
        "impact": "Formalized search and planning with LLMs, laying the groundwork for AI agents, Monte Carlo Tree Search (MCTS) reasoning frameworks, and test-time verification loops."
    },
    {
        "category": "03-reasoning-and-alignment",
        "filename": "05_deepseek_r1_2025.md",
        "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
        "authors": "DeepSeek-AI",
        "year": "2025",
        "venue": "arXiv Preprint",
        "arxiv_id": "2501.12948",
        "arxiv_url": "https://arxiv.org/abs/2501.12948",
        "pdf_url": "https://arxiv.org/pdf/2501.12948.pdf",
        "code_url": "https://github.com/deepseek-ai/DeepSeek-R1",
        "abstract": "We introduce our first-generation reasoning models, DeepSeek-R1-Zero and DeepSeek-R1. DeepSeek-R1-Zero, a model trained via large-scale reinforcement learning without supervised fine-tuning (SFT) as a preliminary step, demonstrates remarkable reasoning capabilities. DeepSeek-R1 incorporates multi-stage training and cold-start data before RL, achieving performance on par with OpenAI-o1 across math, code, and reasoning tasks.",
        "problem": "Frontier reasoning capabilities were assumed to require massive human-annotated reasoning trace datasets ($100K+ SFT examples) and proprietary closed-source infrastructure.",
        "innovations": """1. **Pure RL Emergence (R1-Zero)**: Showed that applying RL (Group Relative Policy Optimization - GRPO) directly onto a base model without SFT naturally elicits long chains of thought, self-reflection, and verification.
2. **Group Relative Policy Optimization (GRPO)**: Dispenses with the critic neural network, estimating baseline rewards from the mean and standard deviation of outputs within a sampled group.
3. **Knowledge Distillation into Small Dense Models**: Distilled R1 reasoning traces into Qwen and Llama models (1.5B to 70B), dramatically outperforming base open models on reasoning benchmarks.""",
        "math": """**GRPO Objective Function:**
$$\\mathcal{J}_{\\text{GRPO}}(\\theta) = \\mathbb{E} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\min \\left( \\frac{\\pi_\\theta(o_i \\mid q)}{\\pi_{\\theta_{\\text{old}}}(o_i \\mid q)} \\hat{A}_i, \\text{clip}\\left( \\frac{\\pi_\\theta(o_i \\mid q)}{\\pi_{\\theta_{\\text{old}}}(o_i \\mid q)}, 1-\\epsilon, 1+\\epsilon \\right) \\hat{A}_i \\right) - \\beta D_{\\text{KL}}(\\pi_\\theta \\parallel \\pi_{\\text{ref}}) \\right]$$
$$\\text{where Advantage: } \\hat{A}_i = \\frac{r_i - \\text{mean}(\\{r_1, \\dots, r_G\\})}{\\text{std}(\\{r_1, \\dots, r_G\\})}$$""",
        "impact": "Completely upended closed-source AI dominance in reasoning, matching OpenAI-o1 on AIME, MATH, and Codeforces while releasing open weights and full technical reproducibility."
    },
    {
        "category": "03-reasoning-and-alignment",
        "filename": "06_constitutional_ai_2022.md",
        "title": "Constitutional AI: Harmlessness from AI Feedback (RLAIF)",
        "authors": "Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, John Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Jared Kaplan, Christopher Berner",
        "year": "2022",
        "venue": "arXiv Preprint",
        "arxiv_id": "2212.08073",
        "arxiv_url": "https://arxiv.org/abs/2212.08073",
        "pdf_url": "https://arxiv.org/pdf/2212.08073.pdf",
        "code_url": "https://github.com/anthropics/constitutional-ai",
        "abstract": "We explore methods for training a harmless AI assistant through self-improvement, without any human feedback labels for harmfulness. The only human oversight is provided through a list of principles or instructions (a constitution). The process involves both a supervised learning phase (critique and revision) and a reinforcement learning phase (RL from AI Feedback - RLAIF).",
        "problem": "RLHF relies on human annotators reviewing hundreds of thousands of toxic, disturbing, or sensitive outputs, creating severe psychological distress for crowdworkers and high economic expense.",
        "innovations": """1. **Written Constitution**: Set of concise principles drawn from the Universal Declaration of Human Rights and safety guidelines.
2. **Critique and Revision (SL Phase)**: The model generates responses, critiques its own output against constitutional principles, and rewrites the response.
3. **RL from AI Feedback (RLAIF)**: Replaced human pairwise preference judges with a constitutional AI evaluator model.""",
        "math": """**Constitutional Critique Prompt:**
$$\\text{Response} \\xrightarrow{\\text{Principle } C_k} \\text{Critique} \\xrightarrow{\\text{Revision}} \\text{Revised Response}$$

**RLAIF Preference Scoring:**
$$P(y_1 \\succ y_2 \\mid x, C) = \\text{LLM}_{\\text{judge}}(\\text{Is } y_1 \\text{ more helpful/harmless according to } C?)$$""",
        "impact": "Serves as the foundational alignment methodology behind Anthropic's Claude series, proving that AI models can self-align toward safety without degrading helpfulness."
    },

    # --- 04 Generative Models & Diffusion ---
    {
        "category": "04-generative-and-diffusion",
        "filename": "01_generative_adversarial_nets_2014.md",
        "title": "Generative Adversarial Nets (GAN)",
        "authors": "Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio",
        "year": "2014",
        "venue": "NeurIPS 2014",
        "arxiv_id": "1406.2661",
        "arxiv_url": "https://arxiv.org/abs/1406.2661",
        "pdf_url": "https://arxiv.org/pdf/1406.2661.pdf",
        "code_url": "https://github.com/goodfeli/adversarial",
        "abstract": "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G.",
        "problem": "Generative modeling previously required intractable approximations to partition functions (Markov Chain Monte Carlo) or lower-bound relaxations that produced blurry samples.",
        "innovations": """1. **Two-Player Minimax Game**: Generator $G(z)$ creates synthetic candidates; Discriminator $D(x)$ distinguishes real data from generated counterfeits.
2. **Implicit Density Estimation**: $G$ learns to map noise vectors $z \\sim p_z$ to data distribution $p_{\\text{data}}$ without explicit likelihood formulation.
3. **Equilibrium at Jensen-Shannon Divergence**: At optimal discriminator $D^*$, the objective minimizes the Jensen-Shannon divergence between $p_{\\text{data}}$ and $p_g$.""",
        "math": """**Adversarial Minimax Objective:**
$$\\min_G \\max_D V(D, G) = \\mathbb{E}_{x \\sim p_{\\text{data}}(x)} [\\log D(x)] + \\mathbb{E}_{z \\sim p_z(z)} [\\log(1 - D(G(z)))]$$

**Optimal Discriminator Form:**
$$D^*(x) = \\frac{p_{\\text{data}}(x)}{p_{\\text{data}}(x) + p_g(x)}$$""",
        "impact": "Launched an explosion of generative vision research across StyleGAN, CycleGAN, BigGAN, and Pix2Pix, dominating image generation until diffusion models emerged in 2020."
    },
    {
        "category": "04-generative-and-diffusion",
        "filename": "02_variational_autoencoders_vae_2013.md",
        "title": "Auto-Encoding Variational Bayes (VAE)",
        "authors": "Diederik P. Kingma, Max Welling",
        "year": "2013",
        "venue": "ICLR 2014",
        "arxiv_id": "1312.6114",
        "arxiv_url": "https://arxiv.org/abs/1312.6114",
        "pdf_url": "https://arxiv.org/pdf/1312.6114.pdf",
        "code_url": "https://github.com/y0ast/VAE-TensorFlow",
        "abstract": "How can we perform efficient inference and learning in directed probabilistic models, in the presence of continuous latent variables with intractable posterior distributions, and large datasets? We introduce a stochastic variational inference and learning algorithm that scales to large datasets, based on the reparameterization trick.",
        "problem": "Continuous latent variable models have intractable true posterior distributions $p(z \\mid x)$, making standard Expectation-Maximization and variational inference computationally infeasible on large datasets.",
        "innovations": """1. **Reparameterization Trick**: Rewrote latent variable sampling as $z = g_\\phi(\\epsilon, x) = \\mu(x) + \\sigma(x) \\odot \\epsilon$ where $\\epsilon \\sim \\mathcal{N}(0, I)$, making stochastic sampling differentiable with backpropagation.
2. **Variational Autoencoder (VAE)**: Unified an encoder probabilistic network $q_\\phi(z \\mid x)$ and decoder generator network $p_\\theta(x \\mid z)$.
3. **ELBO Optimization**: Jointly maximized reconstruction quality while penalizing divergence from the prior distribution.""",
        "math": """**Evidence Lower Bound (ELBO):**
$$\\log p_\\theta(x) \\ge \\mathcal{L}(\\theta, \\phi; x) = \\mathbb{E}_{q_\\phi(z \\mid x)} [\\log p_\\theta(x \\mid z)] - D_{\\text{KL}}(q_\\phi(z \\mid x) \\parallel p(z))$$

**Gaussian KL Divergence in Closed Form:**
$$- D_{\\text{KL}}(q_\\phi(z \\mid x) \\parallel \\mathcal{N}(0, I)) = \\frac{1}{2} \\sum_{j=1}^J \\left( 1 + \\log(\\sigma_j^2) - \\mu_j^2 - \\sigma_j^2 \\right)$$""",
        "impact": "Fundamental contribution to probabilistic machine learning. VAEs provide the compressed latent space encoders used in modern Latent Diffusion Models (Stable Diffusion) and video generation architectures."
    },
    {
        "category": "04-generative-and-diffusion",
        "filename": "03_denoising_diffusion_ddpm_2020.md",
        "title": "Denoising Diffusion Probabilistic Models (DDPM)",
        "authors": "Jonathan Ho, Ajay Jain, Pieter Abbeel",
        "year": "2020",
        "venue": "NeurIPS 2020",
        "arxiv_id": "2006.11239",
        "arxiv_url": "https://arxiv.org/abs/2006.11239",
        "pdf_url": "https://arxiv.org/pdf/2006.11239.pdf",
        "code_url": "https://github.com/hojonathanho/diffusion",
        "abstract": "We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion models and denoising score matching.",
        "problem": "GANs suffer from mode collapse and training instability; VAEs produce blurry samples. Earlier diffusion models (Sohl-Dickstein 2015) were deemed too slow and computationally expensive.",
        "innovations": """1. **Simplified Loss Formulation**: Parameterized the reverse process to directly predict the injected Gaussian noise $\\epsilon$, dramatically simplifying the training objective.
2. **Equivalence to Score Matching**: Connected discrete-time Markov diffusion chains with continuous-time Langevin dynamics and score-based generative modeling.
3. **Superior Sample Quality**: Achieved an unprecedented FID score of 3.17 on CIFAR-10, demonstrating that diffusion models could match and exceed GAN quality.""",
        "math": """**Forward Noising Process (Closed-Form Jump):**
$$q(x_t \\mid x_0) = \\mathcal{N}(x_t; \\sqrt{\\bar{\\alpha}_t} x_0, (1 - \\bar{\\alpha}_t) I)$$

**Simplified Training Objective:**
$$L_{\\text{simple}}(\\theta) = \\mathbb{E}_{t, x_0, \\epsilon} \\left[ \\|\\epsilon - \\epsilon_\\theta(\\sqrt{\\bar{\\alpha}_t} x_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\epsilon, t)\\|^2 \\right]$$""",
        "impact": "Triggered the modern diffusion revolution, replacing GANs as the state-of-the-art methodology for generative modeling in computer vision, audio, biology, and 3D synthesis."
    },
    {
        "category": "04-generative-and-diffusion",
        "filename": "04_latent_diffusion_models_2021.md",
        "title": "High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)",
        "authors": "Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer",
        "year": "2021",
        "venue": "CVPR 2022",
        "arxiv_id": "2112.10752",
        "arxiv_url": "https://arxiv.org/abs/2112.10752",
        "pdf_url": "https://arxiv.org/pdf/2112.10752.pdf",
        "code_url": "https://github.com/CompVis/latent-diffusion",
        "abstract": "By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models achieve state-of-the-art synthesis results on image data. However, operating directly in the high-dimensional pixel space consumes immense computational resources. We apply them in the latent space of powerful pretrained autoencoders.",
        "problem": "Pixel-space diffusion models require iterating hundreds of denoising steps over full-resolution images ($512 \\times 512 \\times 3$), making training and inference prohibitively slow and expensive.",
        "innovations": """1. **Latent Space Compression**: Trained a high-fidelity autoencoder with perceptual and adversarial losses to compress images by 8x ($64 \\times 64 \\times 4$), removing imperceptible high-frequency noise.
2. **Cross-Attention Conditioning**: Added cross-attention layers into the U-Net backbone, allowing flexible conditioning on text prompts (via CLIP), layout masks, or depth maps.
3. **Consumer Hardware Feasibility**: Enabled 512x512 image synthesis on consumer GPUs with single-second inference latencies.""",
        "math": """**Latent Diffusion Training Loss:**
$$L_{\\text{LDM}} = \\mathbb{E}_{\\mathcal{E}(x), y, \\epsilon, t} \\left[ \\|\\epsilon - \\epsilon_\\theta(z_t, t, \\tau_\\theta(y))\\|^2 \\right]$$
Where $\\mathcal{E}$ is the encoder, $z_t$ is the noised latent, and $\\tau_\\theta(y)$ is the text conditioning encoder.""",
        "impact": "Released open-source as **Stable Diffusion**, sparking the democratized text-to-image boom, creative AI applications, ControlNet, LoRA image fine-tuning, and open creative tools."
    },
    {
        "category": "04-generative-and-diffusion",
        "filename": "05_diffusion_transformer_dit_2022.md",
        "title": "Scalable Diffusion Models with Transformers (DiT)",
        "authors": "William Peebles, Saining Xie",
        "year": "2022",
        "venue": "ICCV 2023",
        "arxiv_id": "2212.09748",
        "arxiv_url": "https://arxiv.org/abs/2212.09748",
        "pdf_url": "https://arxiv.org/pdf/2212.09748.pdf",
        "code_url": "https://github.com/facebookresearch/DiT",
        "abstract": "We explore a new class of diffusion models based on the Transformer architecture. We train Diffusion Transformers (DiTs), backing out the commonly-used U-Net backbone in favor of a transformer that operates on latent patches. We analyze the scalability of our DiTs through the lens of forward pass compute and FID.",
        "problem": "Standard diffusion models relied almost exclusively on convolutional U-Net backbones, which had complex downsampling/upsampling architectures and unknown scaling properties with compute.",
        "innovations": """1. **U-Net Replacement**: Completely replaced U-Nets with a standard ViT-style Transformer operating on spatial latent patches.
2. **Adaptive Layer Normalization (adaLN-Zero)**: Injected time-step $t$ and class label conditioning via scale and shift parameters initialized to zero.
3. **Predictable Scaling Laws**: Proved that higher model capacity and smaller patch sizes correlate monotonically with improved FID score.""",
        "math": """**Adaptive Layer Normalization (adaLN-Zero):**
$$\\text{adaLN}(h, y) = \\gamma(y) \\odot \\left( \\frac{h - \\mu}{\\sigma} \\right) + \\beta(y)$$
Modulation parameters $\\gamma, \\beta, \\alpha$ are regressed from the sum of time-step and conditioning embeddings.""",
        "impact": "DiT proved that Transformers scale gracefully in generative vision just as in NLP. It became the core architecture behind OpenAI's **Sora** video generation model and Stable Diffusion 3."
    },
    {
        "category": "04-generative-and-diffusion",
        "filename": "06_flow_matching_2022.md",
        "title": "Flow Matching for Generative Modeling",
        "authors": "Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nicklas, Matt Le",
        "year": "2022",
        "venue": "ICLR 2023",
        "arxiv_id": "2210.02747",
        "arxiv_url": "https://arxiv.org/abs/2210.02747",
        "pdf_url": "https://arxiv.org/pdf/2210.02747.pdf",
        "code_url": "https://github.com/facebookresearch/flow_matching",
        "abstract": "We introduce Flow Matching (FM), a new approach to training Continuous Normalizing Flow (CNF) models at scale. Flow Matching uses regression objectives on vector fields along probability paths without needing numerical ODE simulations during training, unlocking optimal transport displacement interpolation.",
        "problem": "Continuous Normalizing Flows (CNFs) had strong mathematical foundations but required slow, costly numerical ODE solvers during training. Standard diffusion models curved stochastic trajectories require many sampling steps.",
        "innovations": """1. **Simulation-Free Training**: Direct per-sample regression on target vector fields along conditional probability paths without solving ODEs at train time.
2. **Optimal Transport Paths**: Straightens probability flow trajectories between prior noise and data distributions, enabling straight-line particle trajectories.
3. **Fast Inference**: Requires as few as 4-10 integration steps to generate high-fidelity samples.""",
        "math": """**Flow Matching Objective:**
$$\\mathcal{L}_{\\text{CFM}}(\\theta) = \\mathbb{E}_{t, q(x_1), p_t(x \\mid x_1)} \\left[ \\|v_t(x) - u_t(x \\mid x_1)\\|^2 \\right]$$
**Optimal Transport Conditional Vector Field:**
$$\\psi_t(x_0) = (1 - t) x_0 + t x_1, \\quad u_t(x \\mid x_1, x_0) = x_1 - x_0$$""",
        "impact": "Established the mathematical framework adopted by modern state-of-the-art generative models including Flux.1, Stable Diffusion 3, and voice synthesis systems."
    },

    # --- 05 Efficient ML & Novel Architectures ---
    {
        "category": "05-efficient-ml-and-architectures",
        "filename": "01_lora_low_rank_adaptation_2021.md",
        "title": "LoRA: Low-Rank Adaptation of Large Language Models",
        "authors": "Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen",
        "year": "2021",
        "venue": "ICLR 2022",
        "arxiv_id": "2106.09685",
        "arxiv_url": "https://arxiv.org/abs/2106.09685",
        "pdf_url": "https://arxiv.org/pdf/2106.09685.pdf",
        "code_url": "https://github.com/microsoft/LoRA",
        "abstract": "An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks. However, as models grow larger, full fine-tuning becomes prohibitive. We propose Low-Rank Adaptation (LoRA), which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture.",
        "problem": "Full parameter fine-tuning of 175B LLMs required storing gigabytes of optimizer states per task and deploying completely separate model copies for each client application.",
        "innovations": """1. **Rank Decomposition Hypothesis**: Hypothesized that parameter updates $\\Delta W$ have a low 'intrinsic dimension' during task adaptation.
2. **Factorized Matrices**: Represented updates as $\\Delta W = B \\cdot A$ where $B \\in \\mathbb{R}^{d \\times r}$ and $A \\in \\mathbb{R}^{r \\times k}$ with rank $r \\ll \\min(d, k)$.
3. **Zero Inference Latency**: At deployment, $\\Delta W$ can be directly folded into base weights $W_0$, adding zero inference overhead.
4. **Vast Efficiency**: Reduced trainable parameters by 10,000x and GPU memory consumption by 3x.""",
        "math": """**Forward Pass with LoRA:**
$$h = W_0 x + \\Delta W x = W_0 x + \\frac{\\alpha}{r} B A x$$
Where $A \\sim \\mathcal{N}(0, \\sigma^2)$ and $B = 0$ at initialization, ensuring $\\Delta W = 0$ at step 0.""",
        "impact": "The standard fine-tuning method across all of machine learning. Enables individuals and enterprises to customize multi-billion parameter models on modest GPUs in hours."
    },
    {
        "category": "05-efficient-ml-and-architectures",
        "filename": "02_flash_attention_2022.md",
        "title": "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness",
        "authors": "Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré",
        "year": "2022",
        "venue": "NeurIPS 2022",
        "arxiv_id": "2205.14135",
        "arxiv_url": "https://arxiv.org/abs/2205.14135",
        "pdf_url": "https://arxiv.org/pdf/2205.14135.pdf",
        "code_url": "https://github.com/Dao-AILab/flash-attention",
        "abstract": "Transformers are slow and memory-hungry on long sequences, as the time and memory complexity of self-attention are quadratic in sequence length. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU High Bandwidth Memory (HBM) and on-chip SRAM.",
        "problem": "Standard attention implementations materialize the full $N \\times N$ attention matrix in GPU HBM, hitting a memory wall where execution is bottlenecked by memory transfer speeds rather than compute.",
        "innovations": """1. **Tiling & Online Softmax**: Computes softmax incrementally across blocks of Query, Key, and Value without ever storing the full $N \\times N$ attention matrix.
2. **Recomputation in Backward Pass**: Recomputes intermediate attention values on-chip during backpropagation rather than storing them from forward pass.
3. **Exact Output**: Unlike approximate attention methods, FlashAttention computes exact mathematical attention with 2-4x wall-clock speedup and linear $O(N)$ memory.""",
        "math": """**Online Softmax Algorithm:**
$$m(x) = \\max(m(x^{(1)}), m(x^{(2)})), \\quad d(x) = e^{m(x^{(1)}) - m(x)} d(x^{(1)}) + e^{m(x^{(2)}) - m(x)} d(x^{(2)})$$
$$\\text{softmax}(x) = \\frac{e^{x - m(x)}}{d(x)}$$""",
        "impact": "FlashAttention is integrated into PyTorch, Hugging Face, vLLM, and Triton, becoming the universal execution backend enabling 32K, 128K, and 1M token contexts."
    },
    {
        "category": "05-efficient-ml-and-architectures",
        "filename": "03_rope_rotary_position_embedding_2021.md",
        "title": "RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)",
        "authors": "Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu",
        "year": "2021",
        "venue": "Neurocomputing 2024",
        "arxiv_id": "2104.09864",
        "arxiv_url": "https://arxiv.org/abs/2104.09864",
        "pdf_url": "https://arxiv.org/pdf/2104.09864.pdf",
        "code_url": "https://github.com/ZhuiyiTechnology/roformer",
        "abstract": "Positional information is important in sequence modeling. In this work, we propose Rotary Position Embedding (RoPE) to effectively leverage positional information. Specifically, RoPE encodes the absolute position with a rotation matrix and naturally incorporates explicit relative position dependency in self-attention formulation.",
        "problem": "Absolute sinusoidal positional embeddings do not generalize well to sequences longer than those seen in training, while relative position embeddings added computational complexity to self-attention.",
        "innovations": """1. **Rotary Multiplier**: Multiplies query and key representations by orthogonal 2D rotation matrices based on position index $m$.
2. **Inner Product Preservation**: The inner product $\\langle R_m q, R_n k \\rangle$ depends solely on the relative difference $m - n$.
3. **Length Extrapolation**: Seamlessly extends to longer context lengths via interpolation techniques (YaRN, RoPE frequency scaling).""",
        "math": """**Rotary Matrix Operation:**
$$R_{\\Theta, m}^d = \\text{diag}\\left( R_{\\theta_1, m}, R_{\\theta_2, m}, \\dots, R_{\\theta_{d/2}, m} \\right)$$
$$\\text{where } R_{\\theta_i, m} = \\begin{pmatrix} \\cos(m \\theta_i) & -\\sin(m \\theta_i) \\\\ \\sin(m \\theta_i) & \\cos(m \\theta_i) \\end{pmatrix}$$""",
        "impact": "Adopted by virtually every modern frontier LLM (Llama, Mistral, Gemma, DeepSeek, Qwen) as the standard positional encoding architecture."
    },
    {
        "category": "05-efficient-ml-and-architectures",
        "filename": "04_mamba_selective_state_spaces_2023.md",
        "title": "Mamba: Linear-Time Sequence Modeling with Selective State Spaces",
        "authors": "Albert Gu, Tri Dao",
        "year": "2023",
        "venue": "arXiv Preprint",
        "arxiv_id": "2312.00752",
        "arxiv_url": "https://arxiv.org/abs/2312.00752",
        "pdf_url": "https://arxiv.org/pdf/2312.00752.pdf",
        "code_url": "https://github.com/state-spaces/mamba",
        "abstract": "Fundamental sequence models are dominated by the Transformer architecture, but they fail to scale linearly on long sequences due to quadratic attention. We introduce Mamba, a selective structured state space model (SSM) with a hardware-aware parallel algorithm that runs in linear time $O(N)$ and scales up to millions of tokens.",
        "problem": "Transformers suffer from $O(N^2)$ computational complexity and unbounded KV cache memory growth during autoregressive generation, limiting real-time long-context deployment.",
        "innovations": """1. **Selective State Spaces**: Made SSM parameters $B, C, \\Delta$ input-dependent functions, allowing the model to selectively remember or filter out information based on the current token.
2. **Hardware-Aware Parallel Scan**: Overcame recurrence sequential bottlenecks by fusing state transitions into GPU SRAM using associative parallel prefix scans.
3. **Linear Time & Constant Memory**: Operates in $O(N)$ time with $O(1)$ memory per step during autoregressive inference while matching Transformer quality.""",
        "math": """**Continuous State Space Model:**
$$h'(t) = A h(t) + B x(t), \\quad y(t) = C h(t)$$
**Discretized Selective Scan:**
$$\\bar{A} = \\exp(\\Delta A), \\quad \\bar{B} = (\\Delta A)^{-1}(\\exp(\\Delta A) - I) \\cdot \\Delta B$$
$$h_t = \\bar{A}_t h_{t-1} + \\bar{B}_t x_t, \\quad y_t = C_t h_t$$""",
        "impact": "Proved that non-attention architectures could match Transformers at scale, inaugurating hybrid SSM-Transformer architectures and linear-time sequence modeling."
    },
    {
        "category": "05-efficient-ml-and-architectures",
        "filename": "05_qlora_quantized_finetuning_2023.md",
        "title": "QLoRA: Efficient Finetuning of Quantized LLMs",
        "authors": "Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer",
        "year": "2023",
        "venue": "NeurIPS 2023",
        "arxiv_id": "2305.14314",
        "arxiv_url": "https://arxiv.org/abs/2305.14314",
        "pdf_url": "https://arxiv.org/pdf/2305.14314.pdf",
        "code_url": "https://github.com/artidoro/qlora",
        "abstract": "We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters.",
        "problem": "Finetuning large foundation models (65B) previously required multi-GPU server clusters with 80GB A100s, locking independent researchers and small labs out of fine-tuning.",
        "innovations": """1. **4-bit NormalFloat (NF4)**: An information-theoretically optimal quantile quantization data type for normally distributed neural weights.
2. **Double Quantization (DQ)**: Quantized the quantization constants themselves, saving 0.37 bits per parameter (~3GB for a 65B model).
3. **Paged Optimizers**: Used CUDA unified memory to manage memory spikes during activation gradient updates without out-of-memory crashes.""",
        "math": """**NF4 Quantization Form:**
$$q_i = \\text{sign}(w_i) \\cdot Q_X^{-1}\\left( \\frac{i}{2^k + 1} \\right)$$
Where $Q_X$ is the empirical cumulative distribution function of a standard normal distribution $\\mathcal{N}(0, 1)$.""",
        "impact": "Democratized state-of-the-art model tuning, allowing consumer-grade workstations (RTX 3090/4090) to fine-tune 70B models."
    },
    {
        "category": "05-efficient-ml-and-architectures",
        "filename": "06_sparse_mixture_of_experts_moe_2017.md",
        "title": "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer",
        "authors": "Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean",
        "year": "2017",
        "venue": "ICLR 2017",
        "arxiv_id": "1701.06538",
        "arxiv_url": "https://arxiv.org/abs/1701.06538",
        "pdf_url": "https://arxiv.org/pdf/1701.06538.pdf",
        "code_url": "https://github.com/tensorflow/tensor2tensor",
        "abstract": "The capacity of a neural network to absorb information is limited by its number of parameters. In this work, we address this limitation by introducing a Sparsely-Gated Mixture-of-Experts Layer, realizing over 1000x improvements in model capacity with only minor increases in computational cost.",
        "problem": "Dense networks activate all parameters for every input token, forcing a strict trade-off where increasing parameter capacity dramatically inflates compute FLOPs.",
        "innovations": """1. **Sparsely-Gated MoE**: Introduced thousands of feed-forward expert subnetworks, activating only a small chosen subset ($k \\ll n$) per token.
2. **Noisy Top-K Gating**: Injected Gaussian noise into gating logits to ensure balanced expert utilization and continuous exploration.
3. **Sub-linear Scaling**: Scaled model capacity past 137 billion parameters on language translation benchmarks with sub-linear compute overhead.""",
        "math": """**Noisy Top-K Gating Formulation:**
$$G(x) = \\text{Softmax}(\\text{KeepTopK}(H(x), k))$$
$$H(x)_i = (x \\cdot W_g)_i + \\text{StandardNormal}() \\cdot \\text{Softplus}((x \\cdot W_{\\text{noise}})_i)$$""",
        "impact": "Pioneered conditional computation in modern deep learning, serving as the direct intellectual predecessor to Switch Transformer, Mixtral, and DeepSeek-V3."
    },

    # --- 06 Multimodal & Vision-Language ---
    {
        "category": "06-multimodal-and-vision-language",
        "filename": "01_clip_contrastive_vision_language_2021.md",
        "title": "Learning Transferable Visual Models From Natural Language Supervision (CLIP)",
        "authors": "Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever",
        "year": "2021",
        "venue": "ICML 2021",
        "arxiv_id": "2103.00020",
        "arxiv_url": "https://arxiv.org/abs/2103.00020",
        "pdf_url": "https://arxiv.org/pdf/2103.00020.pdf",
        "code_url": "https://github.com/openai/CLIP",
        "abstract": "State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. In this work, we demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs.",
        "problem": "Visual recognition models were bound to fixed 1,000-class taxonomies (like ImageNet-1K), preventing them from recognizing novel objects or understanding open-world concepts.",
        "innovations": """1. **Dual-Encoder Architecture**: Separate vision encoder (ResNet or ViT) and text encoder (Transformer) projecting into a shared multimodal latent space.
2. **Symmetric Contrastive Loss**: InfoNCE objective maximizing cosine similarity of $N$ correct (image, text) pairs while minimizing $N^2 - N$ incorrect pairs in a batch.
3. **Zero-Shot Classification**: Formulated zero-shot classification by computing cosine similarity between an image embedding and prompt embeddings like 'a photo of a {label}'.""",
        "math": """**Symmetric InfoNCE Loss:**
$$\\mathcal{L} = \\frac{1}{2} (\\mathcal{L}_{\\text{image}} + \\mathcal{L}_{\\text{text}})$$
$$\\mathcal{L}_{\\text{image}} = - \\frac{1}{N} \\sum_{i=1}^N \\log \\frac{\\exp(\\text{sim}(I_i, T_i) / \\tau)}{\\sum_{j=1}^N \\exp(\\text{sim}(I_i, T_j) / \\tau)}$$""",
        "impact": "Became the universal visual-semantic bridge across modern AI, serving as the text-image aligner for Stable Diffusion, DALL-E 2, Midjourney, and zero-shot search engines."
    },
    {
        "category": "06-multimodal-and-vision-language",
        "filename": "02_llava_visual_instruction_tuning_2023.md",
        "title": "Visual Instruction Tuning (LLaVA)",
        "authors": "Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee",
        "year": "2023",
        "venue": "NeurIPS 2023",
        "arxiv_id": "2304.08485",
        "arxiv_url": "https://arxiv.org/abs/2304.08485",
        "pdf_url": "https://arxiv.org/pdf/2304.08485.pdf",
        "code_url": "https://github.com/haotian-liu/LLaVA",
        "abstract": "Instruction tuning large language models (LLMs) has shown promising results in boosting their zero-shot capabilities on new tasks. We present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on this generated data, we introduce LLaVA (Large Language and Vision Assistant).",
        "problem": "Vision-language models were trained primarily on simple captioning or VQA benchmarks, failing to follow complex, conversational visual instructions.",
        "innovations": """1. **Synthetic Multimodal Data Pipeline**: Leveraged GPT-4 with symbolic bounding box prompts to synthesize 158K conversational visual instruction pairs.
2. **Elegant Projection Architecture**: Linked a frozen CLIP ViT-L/14 visual encoder to an autoregressive Vicuna/LLaMA decoder via a single linear projection matrix.
3. **End-to-End Fine-Tuning**: Froze the vision encoder while fine-tuning the projection layer and language model on multimodal conversations.""",
        "math": """**Multimodal Token Concatenation:**
$$H_v = W \\cdot Z_v, \\quad \\text{where } Z_v = g(X_v)$$
$$P(Y \\mid X_v, X_q) = \\prod_{i=1}^L P(y_i \\mid H_v, X_{q,<i}, Y_{<i})$$""",
        "impact": "Provided the foundational architecture and training recipe for modern open-source Vision-Language Models (VLMs), enabling visual chatting, document analysis, and GUI automation."
    },
    {
        "category": "06-multimodal-and-vision-language",
        "filename": "03_flamingo_visual_language_model_2022.md",
        "title": "Flamingo: a Visual Language Model for Few-Shot Learning",
        "authors": "Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol Vinyals, Andrew Zisserman, Karen Simonyan",
        "year": "2022",
        "venue": "NeurIPS 2022",
        "arxiv_id": "2204.14198",
        "arxiv_url": "https://arxiv.org/abs/2204.14198",
        "pdf_url": "https://arxiv.org/pdf/2204.14198.pdf",
        "code_url": "https://github.com/lucidrains/flamingo-pytorch",
        "abstract": "We introduce Flamingo, a family of Visual Language Models (VLM) with state-of-the-art few-shot learning capabilities on a wide range of open-ended multimodal tasks. Flamingo models accept interleaved sequences of visual data (images and videos) and text as input and generate text in an autoregressive fashion.",
        "problem": "Models could not seamlessly handle interleaved sequences of multiple images, videos, and text prompts in an open-ended dialogue setting.",
        "innovations": """1. **Perceiver Resampler**: Transformed variable-sized visual features from arbitrary image/video sequences into a fixed number of 64 visual tokens.
2. **Gated Cross-Attention Dense Layers**: Interleaved cross-attention blocks into frozen pre-trained LM layers initialized with tanh-gating to preserve pre-trained knowledge.
3. **Interleaved Multimodal Pre-training**: Trained on billions of web pages containing interleaved text and images (M3W dataset).""",
        "math": """**Tanh-Gated Cross-Attention:**
$$y = x + \\tanh(\\alpha) \\cdot \\text{CrossAttention}(x, \\text{VisualTokens})$$
At initialization $\\alpha = 0$, guaranteeing identity mapping so the LM retains full text capabilities initially.""",
        "impact": "Set the gold standard for few-shot multimodal learning and influenced the multi-image architecture used in Gemini and GPT-4V."
    },
    {
        "category": "06-multimodal-and-vision-language",
        "filename": "04_whisper_speech_recognition_2022.md",
        "title": "Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)",
        "authors": "Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever",
        "year": "2022",
        "venue": "ICML 2023",
        "arxiv_id": "2212.04356",
        "arxiv_url": "https://arxiv.org/abs/2212.04356",
        "pdf_url": "https://arxiv.org/pdf/2212.04356.pdf",
        "code_url": "https://github.com/openai/whisper",
        "abstract": "We study the robustness of speech recognition systems trained simply to predict large amounts of transcripts of audio on the internet. By scaling weakly supervised speech recognition to 680,000 hours of labeled audio data, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results.",
        "problem": "Speech recognition models trained on supervised academic datasets (LibriSpeech) failed drastically when faced with real-world accents, background noise, and colloquial speech.",
        "innovations": """1. **Weak Supervision at Scale**: Trained an encoder-decoder Transformer on 680,000 hours of diverse multilingual audio scraped from the web.
2. **Multitask Sequence Format**: Expressed voice activity detection, language identification, timestamp estimation, and translation into English as a unified autoregressive token prediction task.
3. **Out-of-the-Box Zero-Shot Robustness**: Achieved near-human speech recognition accuracy across noisy, conversational environments without dataset fine-tuning.""",
        "math": """**Whisper Multitask Token Target:**
$$\\text{Target} = [\\langle|\\text{startoftranscript}|\\rangle, \\langle|\\text{language}|\\rangle, \\langle|\\text{transcribe}|\\rangle, \\langle|\\text{notimestamps}|\\rangle, \\text{Tokens}\\dots, \\langle|\\text{endoftranscript}|\\rangle]$$""",
        "impact": "Became the world standard speech-to-text model, powering transcription in millions of consumer, medical, and developer applications."
    },

    # --- 07 Reinforcement Learning & Game Intelligence ---
    {
        "category": "07-reinforcement-learning",
        "filename": "01_deep_q_networks_dqn_2013.md",
        "title": "Playing Atari with Deep Reinforcement Learning (DQN)",
        "authors": "Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller",
        "year": "2013",
        "venue": "NeurIPS Workshop 2013 / Nature 2015",
        "arxiv_id": "1312.5602",
        "arxiv_url": "https://arxiv.org/abs/1312.5602",
        "pdf_url": "https://arxiv.org/pdf/1312.5602.pdf",
        "code_url": "https://github.com/deepmind/dqn",
        "abstract": "We present the first deep learning model to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning. The model is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards.",
        "problem": "Traditional RL relied on hand-engineered state features and was unstable when combined with non-linear function approximators due to correlated state transitions and non-stationary targets.",
        "innovations": """1. **Experience Replay Buffer**: Stored past transitions $(s_t, a_t, r_t, s_{t+1})$ and sampled random minibatches, breaking temporal correlations and stabilizing gradient descent.
2. **Target Network**: Maintained a separate frozen target network $\\theta^-$ updated periodically, preventing runaway feedback loops during Bellman updates.
3. **End-to-End Pixel-to-Action Learning**: Processed 4 consecutive raw video frames to infer velocity and mastered 49 Atari games.""",
        "math": """**DQN Bellman Loss:**
$$L_i(\\theta_i) = \\mathbb{E}_{(s, a, r, s') \\sim U(D)} \\left[ \\left( r + \\gamma \\max_{a'} Q(s', a'; \\theta_i^-) - Q(s, a; \\theta_i) \\right)^2 \\right]$$""",
        "impact": "First demonstration that a single neural network architecture could learn human-level control policies across diverse tasks directly from visual perceptions, launching Deep Reinforcement Learning as a field."
    },
    {
        "category": "07-reinforcement-learning",
        "filename": "02_proximal_policy_optimization_ppo_2017.md",
        "title": "Proximal Policy Optimization Algorithms (PPO)",
        "authors": "John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov",
        "year": "2017",
        "venue": "arXiv Preprint",
        "arxiv_id": "1707.06347",
        "arxiv_url": "https://arxiv.org/abs/1707.06347",
        "pdf_url": "https://arxiv.org/pdf/1707.06347.pdf",
        "code_url": "https://github.com/openai/baselines",
        "abstract": "We propose a new family of policy gradient methods for reinforcement learning, which alternate between sampling data through interaction with the environment, and optimizing a 'surrogate' objective function using stochastic gradient ascent. PPO proposes a novel clipped probability ratio objective that provides monotonic policy improvement.",
        "problem": "Standard policy gradient methods (REINFORCE) had catastrophic step instability; Trust Region Policy Optimization (TRPO) was stable but mathematically complex and computationally expensive (second-order conjugate gradients).",
        "innovations": """1. **Clipped Surrogate Objective**: Clips the probability ratio $r_t(\\theta) = \\frac{\\pi_\\theta(a_t \\mid s_t)}{\\pi_{\\theta_{\\text{old}}}(a_t \\mid s_t)}$ to $[1 - \\epsilon, 1 + \\epsilon]$, discouraging excessively large policy updates.
2. **First-Order Optimization**: Computes updates using standard first-order optimizers (Adam) rather than second-order Hessian inversions.
3. **Sample Efficiency**: Allows multiple epochs of minibatch updates on gathered rollout trajectories.""",
        "math": """**PPO Clipped Surrogate Loss:**
$$L^{\\text{CLIP}}(\\theta) = \\hat{\\mathbb{E}}_t \\left[ \\min(r_t(\\theta) \\hat{A}_t, \\text{clip}(r_t(\\theta), 1-\\epsilon, 1+\\epsilon) \\hat{A}_t) \\right]$$
$$\\text{where } r_t(\\theta) = \\frac{\\pi_\\theta(a_t \\mid s_t)}{\\pi_{\\theta_{\\text{old}}}(a_t \\mid s_t)}$$""",
        "impact": "The undisputed workhorse algorithm of modern reinforcement learning. Used in OpenAI Five (Dota 2), robotic manipulation, and as the core RL optimizer in RLHF for ChatGPT."
    },
    {
        "category": "07-reinforcement-learning",
        "filename": "03_alphazero_game_intelligence_2017.md",
        "title": "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (AlphaZero)",
        "authors": "David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, Demis Hassabis",
        "year": "2017",
        "venue": "Science 2018 / arXiv:1712.01815",
        "arxiv_id": "1712.01815",
        "arxiv_url": "https://arxiv.org/abs/1712.01815",
        "pdf_url": "https://arxiv.org/pdf/1712.01815.pdf",
        "code_url": "https://github.com/deepmind/alphazero",
        "abstract": "The game of chess is the longest-standing testbed in artificial intelligence history. We present AlphaZero, a generic algorithm that masters chess, shogi, and Go from scratch without domain knowledge beyond the basic game rules, defeating world-champion programs (Stockfish, Elmo, AlphaGo Zero) after just hours of self-play.",
        "problem": "Traditional chess programs (Stockfish, Deep Blue) relied on decades of human-crafted heuristics, opening books, and endgame tables that failed to generalize across different board games.",
        "innovations": """1. **Tabula Rasa Learning**: Zero human training data; learns purely from self-play games given only the basic rules of the game.
2. **Unified Policy & Value Network**: A single deep residual neural network $(p, v) = f_\\theta(s)$ predicting move probabilities $p$ and position outcome $v \\in [-1, 1]$.
3. **MCTS Integration**: Guided Monte Carlo Tree Search (MCTS) where the neural network replaces rollouts with direct value evaluation and policy priors.""",
        "math": """**Loss Function for Joint Policy and Value Training:**
$$l = (z - v)^2 - \\pi^T \\log p + c \\|\\theta\\|^2$$
Where $z \\in \\{-1, 0, 1\\}$ is the actual self-play game winner, and $\\pi$ is the MCTS visit probability distribution vector.""",
        "impact": "Considered one of AI's crowning milestones. AlphaZero introduced dynamic, long-term strategic moves that revolutionized grandmaster chess understanding and inspired structural biology breakthroughs like AlphaFold."
    },
    {
        "category": "07-reinforcement-learning",
        "filename": "04_decision_transformer_2021.md",
        "title": "Decision Transformer: Reinforcement Learning via Sequence Modeling",
        "authors": "Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Michael Laskin, Pieter Abbeel, Aravind Srinivas, Igor Mordatch",
        "year": "2021",
        "venue": "NeurIPS 2021",
        "arxiv_id": "2106.01345",
        "arxiv_url": "https://arxiv.org/abs/2106.01345",
        "pdf_url": "https://arxiv.org/pdf/2106.01345.pdf",
        "code_url": "https://github.com/kzl/decision-transformer",
        "abstract": "We introduce Decision Transformer, an architecture that casts the problem of Reinforcement Learning (RL) as conditional sequence modeling. By conditioning an autoregressive model on desired return (reward), past states, and actions, our Decision Transformer model can output actions that achieve target returns.",
        "problem": "Traditional offline RL algorithms (CQL, BEAR) rely on dynamic programming and TD-learning, which suffer from bootstrapping error, value overestimation, and training instability.",
        "innovations": """1. **RL as Sequence Prediction**: Completely discarded Bellman backups and value functions, framing policy execution as autoregressive token generation.
2. **Return-to-Go Conditioning**: Tokens are fed as triplets: $\\tau = (\\hat{R}_1, s_1, a_1, \\hat{R}_2, s_2, a_2, \\dots)$ where $\\hat{R}_t = \\sum_{t'=t}^T r_{t'}$.
3. **Test-Time Return Steering**: At inference time, setting $\\hat{R}_1$ to a high desired return prompts the model to generate high-performing actions.""",
        "math": """**Trajectory Sequence Representation:**
$$\\tau = (\\hat{R}_1, s_1, a_1, \\hat{R}_2, s_2, a_2, \\dots, \\hat{R}_T, s_T, a_T)$$
**Autoregressive Cross-Entropy / MSE Action Loss:**
$$\\mathcal{L}_{\\text{DT}}(\\theta) = \\mathbb{E}_{\\tau \\sim \\mathcal{D}} \\left[ \\sum_{t=1}^T \\|a_t - f_\\theta(s_{\\le t}, a_{<t}, \\hat{R}_{\\le t})\\|^2 \\right]$$""",
        "impact": "Bridged modern generative Transformers and Reinforcement Learning, inspiring subsequent work in robotics foundation models (RT-1, RT-2) and trajectory-level agent planning."
    }
]

def generate_paper_markdown(p):
    return f"""# {p['title']}

<div align="center">

[![Year](https://img.shields.io/badge/Year-{p['year']}-blue?style=for-the-badge)](https://arxiv.org/abs/{p['arxiv_id']})
[![Venue](https://img.shields.io/badge/Venue-{p['venue'].replace(' ', '%20')}-purple?style=for-the-badge)](https://arxiv.org/abs/{p['arxiv_id']})
[![arXiv](https://img.shields.io/badge/arXiv-{p['arxiv_id']}-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)]({p['arxiv_url']})
[![PDF](https://img.shields.io/badge/Download-PDF-red?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)]({p['pdf_url']})
[![Code](https://img.shields.io/badge/Code-Repository-181717?style=for-the-badge&logo=github&logoColor=white)]({p['code_url']})

</div>

---

### 📋 Paper Metadata

- **Authors:** {p['authors']}
- **Publication Year:** {p['year']}
- **Venue:** {p['venue']}
- **Primary arXiv ID:** [`arXiv:{p['arxiv_id']}`]({p['arxiv_url']})
- **PDF Direct Download:** [Click to Read Official PDF]({p['pdf_url']})
- **Reference Implementation:** [GitHub Repository]({p['code_url']})

---

### 📖 Executive Abstract

> "{p['abstract']}"

---

### 🎯 Core Problem & Motivation

{p['problem']}

---

### 💡 Key Innovations & Architecture

{p['innovations']}

---

### 📐 Mathematical Formulation

{p['math']}

---

### 🌟 Significance & Industry Impact

{p['impact']}

---

### 📚 BibTeX Citation

```bibtex
@article{{{p['filename'].replace('.md', '')},
  title = {{{p['title']}}},
  author = {{{p['authors']}}},
  journal = {{arXiv preprint arXiv:{p['arxiv_id']}}},
  year = {{{p['year']}}},
  url = {{{p['arxiv_url']}}}
}}
```
"""

def main():
    print(f"[*] Generating {len(PAPERS_DETAIL)} comprehensive paper dossiers...")
    for p in PAPERS_DETAIL:
        target_dir = REPO_ROOT / p["category"]
        target_dir.mkdir(parents=True, exist_ok=True)
        file_path = target_dir / p["filename"]
        content = generate_paper_markdown(p)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[✓] Written: {p['category']}/{p['filename']}")
    print("[✓] All 38 paper dossiers generated successfully!")

if __name__ == "__main__":
    main()
