---
method_name: "Transformer"
category: "Attention-Based Architecture"
application: ["Image Classification", "Semantic Segmentation", "Object Detection"]
related_tasks: ["Seismic Image Segmentation", "Fault Segmentation"]
tags: [transformer, attention, deep-learning, segmentation]
created: 2026-07-08
---

# Definition / 定义

Transformer is an attention-based neural network architecture that processes input as a set of tokens, using self-attention to model global dependencies between all tokens simultaneously. Originally from NLP, vision transformers (ViT, Swin, SegFormer) have recently been applied to image segmentation, including seismic images.

# Core Idea / 核心思想

Instead of processing images with local convolution kernels, Transformers split the image into patches (tokens), then use self-attention to compute relationships between every pair of patches. This captures long-range dependencies that CNNs miss.

For seismic segmentation, this is valuable: faults extend across large regions, and understanding fault connectivity requires global context that local CNN kernels cannot provide.

# Architecture / Formulation / 架构/公式

## Self-Attention

$$
\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

## Vision Transformer (ViT) Pipeline

```
Image → Split into patches → Linear projection → Position embedding
    ↓
Transformer Encoder (Multi-Head Self-Attention + MLP) ×L layers
    ↓
[CLS] token → Classification head
```

## For Segmentation (e.g., SegFormer)

```
Image → Hierarchical Transformer Encoder (multi-scale features)
    ↓
Simple MLP Decoder (lightweight, no complex upsampling)
    ↓
Pixel-wise prediction
```

# Advantages / 优势

- Global receptive field from the first layer — captures long-range fault continuity
- Dynamic attention weights — model learns what to focus on per input
- Strong performance with sufficient training data
- SegFormer-style designs are surprisingly lightweight

# Limitations / 局限性

- **Data-hungry**: Requires more training data than CNNs to generalize well
- **Computational cost**: Self-attention is O(N²) in sequence length; large images are expensive
- **Less inductive bias**: No built-in assumptions about local spatial structure (unlike CNN convolution)
- **Memory intensive**: Full attention maps are large; patch-based approaches help but lose fine detail
- **RTX4070 constraint**: Full Vision Transformer on large images may exceed 12GB; patch-based or hybrid approaches recommended

# Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Fault Segmentation | Global context for fault continuity | Emerging; limited published work |
| General Image Segmentation | Semantic/instance segmentation | SegFormer, Swin-Unet |
| NLP (original domain) | Machine translation, text understanding | Original "Attention Is All You Need" |

# Related Papers / 相关论文

- [[Literature-review-on-deep-learning-for-segmentation-of-seismic-images]] — Notes Transformer as emerging trend in seismic segmentation

# Related Methods / 相关方法

- [[CNN]] — Alternative paradigm; CNNs and Transformers are increasingly hybridized
- [[U-Net]] — TransUNet combines CNN encoder with Transformer bottleneck
- [[Attention Mechanism]] — Transformers are built entirely from attention blocks
