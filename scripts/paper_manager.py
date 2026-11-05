#!/usr/bin/env python3
"""
AI/ML Research Papers Repository Manager
Automated utility to search arXiv, download PDF papers, export BibTeX citations,
and maintain the repository's research index.
"""

import os
import sys
import time
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

# Fix Windows console encoding for UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = REPO_ROOT / "papers_pdf"
CITATIONS_FILE = REPO_ROOT / "citations.bib"

# Curated catalog of seminal & state-of-the-art AI/ML papers
PAPERS_CATALOG = [
    # 01 Foundational Architectures
    {
        "id": "1206.5538",
        "title": "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)",
        "authors": ["Alex Krizhevsky", "Ilya Sutskever", "Geoffrey E. Hinton"],
        "year": 2012,
        "category": "01-foundational-architectures",
        "slug": "01_alexnet_2012",
        "arxiv_id": "1206.5538", # or NIPS 2012
        "venue": "NeurIPS 2012",
        "summary": "Introduced deep convolutional neural networks with ReLU, Dropout, and GPU acceleration, winning ImageNet 2012 and sparking modern Deep Learning.",
    },
    {
        "id": "1512.03385",
        "title": "Deep Residual Learning for Image Recognition (ResNet)",
        "authors": ["Kaiming He", "Xiangyu Zhang", "Shaoqing Ren", "Jian Sun"],
        "year": 2015,
        "category": "01-foundational-architectures",
        "slug": "02_resnet_2015",
        "arxiv_id": "1512.03385",
        "venue": "CVPR 2016 (Best Paper)",
        "summary": "Introduced identity shortcut connections (residual learning) allowing training of networks up to 152 layers and mitigating vanishing gradients.",
    },
    {
        "id": "1706.03762",
        "title": "Attention Is All You Need (Transformer)",
        "authors": ["Ashish Vaswani", "Noam Shazeer", "Niki Parmar", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Lukasz Kaiser", "Illia Polosukhin"],
        "year": 2017,
        "category": "01-foundational-architectures",
        "slug": "03_attention_is_all_you_need_2017",
        "arxiv_id": "1706.03762",
        "venue": "NeurIPS 2017",
        "summary": "Replaced recurrence and convolutions with Multi-Head Self-Attention, establishing the foundational architecture for modern LLMs and Multimodal AI.",
    },
    {
        "id": "1810.04805",
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "authors": ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"],
        "year": 2018,
        "category": "01-foundational-architectures",
        "slug": "04_bert_2018",
        "arxiv_id": "1810.04805",
        "venue": "NAACL 2019 (Best Long Paper)",
        "summary": "Introduced Masked Language Modeling (MLM) and Next Sentence Prediction (NSP) for pre-training bidirectional representations across NLP.",
    },
    {
        "id": "2005.14165",
        "title": "Language Models are Few-Shot Learners (GPT-3)",
        "authors": ["Tom B. Brown et al.", "OpenAI"],
        "year": 2020,
        "category": "01-foundational-architectures",
        "slug": "05_gpt3_2020",
        "arxiv_id": "2005.14165",
        "venue": "NeurIPS 2020",
        "summary": "Demonstrated that scaling autoregressive transformers to 175B parameters unlocks emergent in-context few-shot learning without fine-tuning.",
    },
    {
        "id": "2010.11929",
        "title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)",
        "authors": ["Alexey Dosovitskiy et al.", "Google Research"],
        "year": 2020,
        "category": "01-foundational-architectures",
        "slug": "06_vision_transformer_vit_2020",
        "arxiv_id": "2010.11929",
        "venue": "ICLR 2021",
        "summary": "Demonstrated that pure transformers applied directly to sequences of flattened image patches outperform CNNs when pre-trained on large-scale datasets.",
    },

    # 02 Large Language Models & Scaling
    {
        "id": "2203.15556",
        "title": "Training Compute-Optimal Large Language Models (Chinchilla)",
        "authors": ["Jordan Hoffmann et al.", "DeepMind"],
        "year": 2022,
        "category": "02-large-language-models",
        "slug": "01_chinchilla_scaling_laws_2022",
        "arxiv_id": "2203.15556",
        "venue": "NeurIPS 2022",
        "summary": "Established compute-optimal scaling laws showing tokens and model parameters should be scaled in equal proportion, disproving previous Kaplan scaling.",
    },
    {
        "id": "2302.13971",
        "title": "LLaMA: Open and Efficient Foundation Language Models",
        "authors": ["Hugo Touvron et al.", "Meta AI"],
        "year": 2023,
        "category": "02-large-language-models",
        "slug": "02_llama_2023",
        "arxiv_id": "2302.13971",
        "venue": "arXiv Preprint",
        "summary": "Democratized foundation models by releasing highly-performant open models (7B-65B) trained exclusively on publicly available datasets with RMSNorm, SwiGLU, and RoPE.",
    },
    {
        "id": "2407.21783",
        "title": "The Llama 3 Herd of Models",
        "authors": ["Abhimanyu Dubey et al.", "Meta AI"],
        "year": 2024,
        "category": "02-large-language-models",
        "slug": "03_llama_3_herd_2024",
        "arxiv_id": "2407.21783",
        "venue": "arXiv Preprint",
        "summary": "Detailed technical report of Llama 3 (8B, 70B, 405B) pre-trained on 15T+ tokens with GQA, 128k context, and multi-round iterative RLHF/DPO post-training.",
    },
    {
        "id": "2401.04088",
        "title": "Mixtral of Experts",
        "authors": ["Albert Q. Jiang et al.", "Mistral AI"],
        "year": 2024,
        "category": "02-large-language-models",
        "slug": "04_mixtral_of_experts_2024",
        "arxiv_id": "2401.04088",
        "venue": "arXiv Preprint",
        "summary": "Introduced an 8x7B sparse mixture-of-experts model matching or exceeding LLaMA 2 70B on most benchmarks with 6x faster inference (routing 2 experts per token).",
    },
    {
        "id": "2412.19437",
        "title": "DeepSeek-V3 Technical Report",
        "authors": ["DeepSeek-AI"],
        "year": 2024,
        "category": "02-large-language-models",
        "slug": "05_deepseek_v3_2024",
        "arxiv_id": "2412.19437",
        "venue": "arXiv Preprint",
        "summary": "A 671B MoE model (37B active) featuring Multi-Head Latent Attention (MLA), DeepSeekMoE architecture, auxiliary-loss-free load balancing, and FP8 mixed precision training.",
    },
    {
        "id": "2403.08295",
        "title": "Gemma: Open Models Based on Gemini Research and Technology",
        "authors": ["Gemma Team", "Google DeepMind"],
        "year": 2024,
        "category": "02-large-language-models",
        "slug": "06_gemma_models_2024",
        "arxiv_id": "2403.08295",
        "venue": "arXiv Preprint",
        "summary": "State-of-the-art lightweight open models (2B, 7B) built on Gemini research, featuring GeGLU activations, RMSNorm, and extensive RLHF safety alignment.",
    },

    # 03 Reasoning, Post-Training & Alignment
    {
        "id": "2203.02155",
        "title": "Training language models to follow instructions with human feedback (InstructGPT)",
        "authors": ["Long Ouyang et al.", "OpenAI"],
        "year": 2022,
        "category": "03-reasoning-and-alignment",
        "slug": "01_instructgpt_rlhf_2022",
        "arxiv_id": "2203.02155",
        "venue": "NeurIPS 2022",
        "summary": "Pioneered Reinforcement Learning from Human Feedback (RLHF) with PPO and reward models to align LLMs with user intent, reducing toxicity and hallucinations.",
    },
    {
        "id": "2305.18290",
        "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)",
        "authors": ["Rafael Rafailov", "Archit Sharma", "Eric Mitchell", "Stefano Ermon", "Christopher D. Manning", "Chelsea Finn"],
        "year": 2023,
        "category": "03-reasoning-and-alignment",
        "slug": "02_direct_preference_optimization_2023",
        "arxiv_id": "2305.18290",
        "venue": "NeurIPS 2023",
        "summary": "Eliminated explicit reward modeling and reinforcement learning loops in alignment by analytically optimizing policy directly over human preference pairs.",
    },
    {
        "id": "2201.11903",
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "authors": ["Jason Wei", "Xuezhi Wang", "Dale Schuurmans", "Maarten Bosma", "Brian Ichter", "Fei Xia", "Ed H. Chi", "Quoc V. Le", "Denny Zhou"],
        "year": 2022,
        "category": "03-reasoning-and-alignment",
        "slug": "03_chain_of_thought_2022",
        "arxiv_id": "2201.11903",
        "venue": "NeurIPS 2022",
        "summary": "Showed that prompting LLMs to generate intermediate reasoning steps drastically improves multi-step arithmetic, commonsense, and symbolic reasoning.",
    },
    {
        "id": "2305.10601",
        "title": "Tree of Thoughts: Deliberate Problem Solving with Large Language Models",
        "authors": ["Shunyu Yao", "Dian Yu", "Jeffrey Zhao", "Izhak Shafran", "Thomas L. Griffiths", "Yuan Cao", "Karthik Narasimhan"],
        "year": 2023,
        "category": "03-reasoning-and-alignment",
        "slug": "04_tree_of_thoughts_2023",
        "arxiv_id": "2305.10601",
        "venue": "NeurIPS 2023",
        "summary": "Generalizes Chain-of-Thought to exploration over trees of coherent thoughts with BFS/DFS search, lookahead, and backtracking for non-trivial problem solving.",
    },
    {
        "id": "2501.12948",
        "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
        "authors": ["DeepSeek-AI"],
        "year": 2025,
        "category": "03-reasoning-and-alignment",
        "slug": "05_deepseek_r1_2025",
        "arxiv_id": "2501.12948",
        "venue": "arXiv Preprint",
        "summary": "Introduced pure large-scale RL (DeepSeek-R1-Zero) and multi-stage distillation with GRPO to induce reasoning, self-reflection, and test-time verification without supervised warm-up.",
    },
    {
        "id": "2212.08073",
        "title": "Constitutional AI: Harmlessness from AI Feedback (RLAIF)",
        "authors": ["Yuntao Bai et al.", "Anthropic"],
        "year": 2022,
        "category": "03-reasoning-and-alignment",
        "slug": "06_constitutional_ai_2022",
        "arxiv_id": "2212.08073",
        "venue": "arXiv Preprint",
        "summary": "Proposed self-supervised alignment using a set of written principles ('constitution') and AI-generated critiques, replacing human crowdworkers in RL feedback.",
    },

    # 04 Generative Models & Diffusion
    {
        "id": "1406.2661",
        "title": "Generative Adversarial Nets (GAN)",
        "authors": ["Ian J. Goodfellow et al."],
        "year": 2014,
        "category": "04-generative-and-diffusion",
        "slug": "01_generative_adversarial_nets_2014",
        "arxiv_id": "1406.2661",
        "venue": "NeurIPS 2014",
        "summary": "Pioneered adversarial minimax game framework pitting a generator against a discriminator, initiating modern photorealistic deep generative modeling.",
    },
    {
        "id": "1312.6114",
        "title": "Auto-Encoding Variational Bayes (VAE)",
        "authors": ["Diederik P. Kingma", "Max Welling"],
        "year": 2013,
        "category": "04-generative-and-diffusion",
        "slug": "02_variational_autoencoders_vae_2013",
        "arxiv_id": "1312.6114",
        "venue": "ICLR 2014",
        "summary": "Introduced the reparameterization trick and variational inference for deep latent variable models, maximizing the Evidence Lower Bound (ELBO).",
    },
    {
        "id": "2006.11239",
        "title": "Denoising Diffusion Probabilistic Models (DDPM)",
        "authors": ["Jonathan Ho", "Ajay Jain", "Pieter Abbeel"],
        "year": 2020,
        "category": "04-generative-and-diffusion",
        "slug": "03_denoising_diffusion_ddpm_2020",
        "arxiv_id": "2006.11239",
        "venue": "NeurIPS 2020",
        "summary": "Bridged non-equilibrium thermodynamics and score-based matching with parameterized Markov reverse chains, proving diffusion beats GANs in image fidelity.",
    },
    {
        "id": "2112.10752",
        "title": "High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)",
        "authors": ["Robin Rombach", "Andreas Blattmann", "Dominik Lorenz", "Patrick Esser", "Björn Ommer"],
        "year": 2021,
        "category": "04-generative-and-diffusion",
        "slug": "04_latent_diffusion_models_2021",
        "arxiv_id": "2112.10752",
        "venue": "CVPR 2022",
        "summary": "Applied diffusion processes inside the latent space of pre-trained autoencoders, drastically reducing compute costs and enabling text-to-image synthesis.",
    },
    {
        "id": "2212.09748",
        "title": "Scalable Diffusion Models with Transformers (DiT)",
        "authors": ["William Peebles", "Saining Xie"],
        "year": 2022,
        "category": "04-generative-and-diffusion",
        "slug": "05_diffusion_transformer_dit_2022",
        "arxiv_id": "2212.09748",
        "venue": "ICCV 2023",
        "summary": "Replaced traditional U-Nets with Transformer backbones for diffusion models, laying the architectural foundation for video models like Sora.",
    },
    {
        "id": "2210.02747",
        "title": "Flow Matching for Generative Modeling",
        "authors": ["Yaron Lipman", "Ricky T. Q. Chen", "Heli Ben-Hamu", "Maximilian Nicklas", "Matt Le"],
        "year": 2022,
        "category": "04-generative-and-diffusion",
        "slug": "06_flow_matching_2022",
        "arxiv_id": "2210.02747",
        "venue": "ICLR 2023",
        "summary": "A simulation-free approach for training continuous normalizing flows (CNFs) using optimal transport probability paths, enabling faster and straighter sampling.",
    },

    # 05 Efficient ML, Inference & Novel Architectures
    {
        "id": "2106.09685",
        "title": "LoRA: Low-Rank Adaptation of Large Language Models",
        "authors": ["Edward J. Hu et al.", "Microsoft"],
        "year": 2021,
        "category": "05-efficient-ml-and-architectures",
        "slug": "01_lora_low_rank_adaptation_2021",
        "arxiv_id": "2106.09685",
        "venue": "ICLR 2022",
        "summary": "Froze pre-trained weights and injected trainable rank decomposition matrices into Transformer attention layers, reducing fine-tuning memory by 3x and parameters by 10,000x.",
    },
    {
        "id": "2205.14135",
        "title": "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness",
        "authors": ["Tri Dao", "Daniel Y. Fu", "Stefano Ermon", "Atri Rudra", "Christopher Ré"],
        "year": 2022,
        "category": "05-efficient-ml-and-architectures",
        "slug": "02_flash_attention_2022",
        "arxiv_id": "2205.14135",
        "venue": "NeurIPS 2022",
        "summary": "An IO-aware exact attention algorithm leveraging GPU SRAM tiling and online softmax to eliminate HBM read/writes, speeding up training 3-5x with linear memory.",
    },
    {
        "id": "2104.09864",
        "title": "RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)",
        "authors": ["Jianlin Su", "Yu Lu", "Shengfeng Pan", "Ahmed Murtadha", "Bo Wen", "Yunfeng Liu"],
        "year": 2021,
        "category": "05-efficient-ml-and-architectures",
        "slug": "03_rope_rotary_position_embedding_2021",
        "arxiv_id": "2104.09864",
        "venue": "Neurocomputing 2024",
        "summary": "Encoded relative position information into query and key representations via complex 2D rotation matrices, becoming the universal positional encoding in Llama and modern LLMs.",
    },
    {
        "id": "2312.00752",
        "title": "Mamba: Linear-Time Sequence Modeling with Selective State Spaces",
        "authors": ["Albert Gu", "Tri Dao"],
        "year": 2023,
        "category": "05-efficient-ml-and-architectures",
        "slug": "04_mamba_selective_state_spaces_2023",
        "arxiv_id": "2312.00752",
        "venue": "arXiv Preprint",
        "summary": "Introduced selective state space models (SSMs) with hardware-aware scan algorithms that run in linear time O(N) while matching or beating Transformer performance.",
    },
    {
        "id": "2305.14314",
        "title": "QLoRA: Efficient Finetuning of Quantized LLMs",
        "authors": ["Tim Dettmers", "Artidoro Pagnoni", "Ari Holtzman", "Luke Zettlemoyer"],
        "year": 2023,
        "category": "05-efficient-ml-and-architectures",
        "slug": "05_qlora_quantized_finetuning_2023",
        "arxiv_id": "2305.14314",
        "venue": "NeurIPS 2023",
        "summary": "Enabled fine-tuning a 65B parameter model on a single 48GB GPU using 4-bit NormalFloat (NF4), double quantization, and paged optimizers without degradation.",
    },
    {
        "id": "1701.06538",
        "title": "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer",
        "authors": ["Noam Shazeer et al.", "Google Brain"],
        "year": 2017,
        "category": "05-efficient-ml-and-architectures",
        "slug": "06_sparse_mixture_of_experts_moe_2017",
        "arxiv_id": "1701.06538",
        "venue": "ICLR 2017",
        "summary": "Pioneered conditional computation and sparse gating networks in deep learning, enabling capacity scaling to 1000x parameters with sub-linear compute.",
    },

    # 06 Multimodal & Vision-Language
    {
        "id": "2103.00020",
        "title": "Learning Transferable Visual Models From Natural Language Supervision (CLIP)",
        "authors": ["Alec Radford et al.", "OpenAI"],
        "year": 2021,
        "category": "06-multimodal-and-vision-language",
        "slug": "01_clip_contrastive_vision_language_2021",
        "arxiv_id": "2103.00020",
        "venue": "ICML 2021",
        "summary": "Trained dual visual and text encoders on 400M internet image-caption pairs using InfoNCE contrastive loss, unlocking zero-shot visual classification and cross-modal search.",
    },
    {
        "id": "2304.08485",
        "title": "Visual Instruction Tuning (LLaVA)",
        "authors": ["Haotian Liu", "Chunyuan Li", "Qingyang Wu", "Yong Jae Lee"],
        "year": 2023,
        "category": "06-multimodal-and-vision-language",
        "slug": "02_llava_visual_instruction_tuning_2023",
        "arxiv_id": "2304.08485",
        "venue": "NeurIPS 2023",
        "summary": "Connected a vision encoder (CLIP ViT) with an autoregressive language decoder (LLaMA) via a simple projection matrix, creating high-capability open multimodal assistants.",
    },
    {
        "id": "2204.14198",
        "title": "Flamingo: a Visual Language Model for Few-Shot Learning",
        "authors": ["Jean-Baptiste Alayrac et al.", "DeepMind"],
        "year": 2022,
        "category": "06-multimodal-and-vision-language",
        "slug": "03_flamingo_visual_language_model_2022",
        "arxiv_id": "2204.14198",
        "venue": "NeurIPS 2022",
        "summary": "Bridged powerful pre-trained vision-only and language-only models using Perceiver Resamplers and gated cross-attention layers, demonstrating rapid in-context multimodal learning.",
    },
    {
        "id": "2212.04356",
        "title": "Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)",
        "authors": ["Alec Radford et al.", "OpenAI"],
        "year": 2022,
        "category": "06-multimodal-and-vision-language",
        "slug": "04_whisper_speech_recognition_2022",
        "arxiv_id": "2212.04356",
        "venue": "ICML 2023",
        "summary": "Trained an encoder-decoder Transformer on 680,000 hours of multilingual internet audio, achieving human-level zero-shot robustness in speech transcription and translation.",
    },

    # 07 Reinforcement Learning & Game Intelligence
    {
        "id": "1312.5602",
        "title": "Playing Atari with Deep Reinforcement Learning (DQN)",
        "authors": ["Volodymyr Mnih et al.", "DeepMind"],
        "year": 2013,
        "category": "07-reinforcement-learning",
        "slug": "01_deep_q_networks_dqn_2013",
        "arxiv_id": "1312.5602",
        "venue": "NeurIPS Workshop 2013 / Nature 2015",
        "summary": "Combined Q-learning with deep convolutional neural networks and experience replay buffers to directly master Atari 2600 video games from raw pixels.",
    },
    {
        "id": "1707.06347",
        "title": "Proximal Policy Optimization Algorithms (PPO)",
        "authors": ["John Schulman", "Filip Wolski", "Prafulla Dhariwal", "Alec Radford", "Oleg Klimov"],
        "year": 2017,
        "category": "07-reinforcement-learning",
        "slug": "02_proximal_policy_optimization_ppo_2017",
        "arxiv_id": "1707.06347",
        "venue": "arXiv Preprint",
        "summary": "Proposed clipped surrogate objective functions for policy gradients that balance sample efficiency and simplicity, becoming the standard RL algorithm for robotics and RLHF.",
    },
    {
        "id": "1712.01815",
        "title": "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (AlphaZero)",
        "authors": ["David Silver et al.", "DeepMind"],
        "year": 2017,
        "category": "07-reinforcement-learning",
        "slug": "03_alphazero_game_intelligence_2017",
        "arxiv_id": "1712.01815",
        "venue": "Science 2018 / arXiv:1712.01815",
        "summary": "Mastered chess, shogi, and Go from scratch through pure self-play reinforcement learning and Monte Carlo Tree Search (MCTS) with zero human domain knowledge.",
    },
    {
        "id": "2106.01345",
        "title": "Decision Transformer: Reinforcement Learning via Sequence Modeling",
        "authors": ["Lili Chen", "Kevin Lu", "Aravind Rajeswaran", "Kimin Lee", "Aditya Grover", "Michael Laskin", "Pieter Abbeel", "Aravind Srinivas", "Igor Mordatch"],
        "year": 2021,
        "category": "07-reinforcement-learning",
        "slug": "04_decision_transformer_2021",
        "arxiv_id": "2106.01345",
        "venue": "NeurIPS 2021",
        "summary": "Cast reinforcement learning as a conditional sequence modeling problem, generating actions using autoregressive transformers conditioned on desired returns-to-go.",
    }
]

def search_arxiv(query, max_results=5):
    """Search arXiv API using urllib."""
    encoded_query = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query={encoded_query}&start=0&max_results={max_results}"
    req = urllib.request.Request(url, headers={"User-Agent": "AIML-Research-Papers-Manager/1.0"})
    
    with urllib.request.urlopen(req) as response:
        xml_data = response.read()
        
    root = ET.fromstring(xml_data)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    
    results = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
        published = entry.find("atom:published", ns).text.strip()
        id_url = entry.find("atom:id", ns).text.strip()
        arxiv_id = id_url.split("/abs/")[-1]
        
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
        pdf_link = None
        for link in entry.findall("atom:link", ns):
            if link.attrib.get("title") == "pdf":
                pdf_link = link.attrib.get("href")
                
        results.append({
            "id": arxiv_id,
            "title": title,
            "authors": authors,
            "published": published,
            "summary": summary,
            "pdf_url": pdf_link or f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        })
    return results

def download_pdf(arxiv_id, output_path=None):
    """Download a research paper PDF from arXiv."""
    clean_id = arxiv_id.strip()
    if clean_id.startswith("http"):
        clean_id = clean_id.split("/")[-1].replace(".pdf", "")
        
    url = f"https://arxiv.org/pdf/{clean_id}.pdf"
    if output_path is None:
        output_path = PDF_DIR / f"{clean_id}.pdf"
    else:
        output_path = Path(output_path)
        
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"[*] Downloading {clean_id} from {url}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AIML-Research-Papers-Repo/1.0"}
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response, open(output_path, "wb") as f:
            f.write(response.read())
        print(f"[✓] Saved successfully to: {output_path}")
        return True
    except Exception as e:
        print(f"[!] Error downloading {clean_id}: {e}")
        return False

def generate_bibtex():
    """Generate BibTeX entries for all curated papers in the catalog."""
    entries = []
    for p in PAPERS_CATALOG:
        author_str = " and ".join(p["authors"])
        tag = p["slug"].split("_", 1)[-1]
        bib = f"""@article{{{tag},
  title = {{{p['title']}}},
  author = {{{author_str}}},
  journal = {{arXiv preprint arXiv:{p['arxiv_id']}}},
  year = {{{p['year']}}},
  url = {{https://arxiv.org/abs/{p['arxiv_id']}}}
}}"""
        entries.append(bib)
    return "\n\n".join(entries)

def main():
    parser = argparse.ArgumentParser(description="AI/ML Research Papers Repository CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # List command
    subparsers.add_parser("list", help="List all curated papers in the repository")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search arXiv online")
    search_parser.add_argument("--query", required=True, help="Search query string")
    search_parser.add_argument("--max", type=int, default=5, help="Max results to fetch")
    
    # Download command
    dl_parser = subparsers.add_parser("download", help="Download a paper PDF by arXiv ID")
    dl_parser.add_argument("--id", required=True, help="arXiv ID (e.g. 1706.03762)")
    dl_parser.add_argument("--output", help="Custom output filepath")
    
    # Download all command
    dl_all_parser = subparsers.add_parser("download-all", help="Download all seminal papers (with rate limits)")
    dl_all_parser.add_argument("--limit", type=int, default=10, help="Number of papers to download")
    
    # Export BibTeX command
    subparsers.add_parser("export-bib", help="Export citations.bib with all catalog papers")

    args = parser.parse_args()
    
    if args.command == "list":
        print(f"\n{'='*80}")
        print(f"📚 Curated AI/ML Seminal Research Papers ({len(PAPERS_CATALOG)} Papers)")
        print(f"{'='*80}\n")
        current_cat = None
        for i, p in enumerate(PAPERS_CATALOG, 1):
            if p["category"] != current_cat:
                current_cat = p["category"]
                print(f"\n📂 [{current_cat.upper()}]")
            print(f"  {i:2d}. [{p['year']}] {p['title']}")
            print(f"      Authors: {', '.join(p['authors'][:3])}{'...' if len(p['authors']) > 3 else ''}")
            print(f"      arXiv: https://arxiv.org/abs/{p['arxiv_id']} | Venue: {p['venue']}")
            
    elif args.command == "search":
        print(f"🔍 Searching arXiv for: '{args.query}'...")
        results = search_arxiv(args.query, args.max)
        for i, r in enumerate(results, 1):
            print(f"\n[{i}] {r['title']} ({r['published'][:10]})")
            print(f"    Authors: {', '.join(r['authors'][:4])}")
            print(f"    arXiv ID: {r['id']}")
            print(f"    PDF: {r['pdf_url']}")
            print(f"    Summary: {r['summary'][:200]}...")
            
    elif args.command == "download":
        download_pdf(args.id, args.output)
        
    elif args.command == "download-all":
        count = min(args.limit, len(PAPERS_CATALOG))
        print(f"[*] Starting polite download of top {count} seminal papers...")
        for i, p in enumerate(PAPERS_CATALOG[:count], 1):
            target = PDF_DIR / f"{p['slug']}.pdf"
            if target.exists():
                print(f"[-] Already exists: {target.name}")
                continue
            download_pdf(p['arxiv_id'], target)
            if i < count:
                time.sleep(3) # Respect arXiv rate limits
        print("[✓] Batch download complete.")
        
    elif args.command == "export-bib":
        bib_content = generate_bibtex()
        with open(CITATIONS_FILE, "w", encoding="utf-8") as f:
            f.write(bib_content)
        print(f"[✓] Written {len(PAPERS_CATALOG)} entries to {CITATIONS_FILE}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
