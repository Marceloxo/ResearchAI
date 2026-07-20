---
method_name: "Vision Transformer (ViT)"
category: "Architecture"
application: ["Image Classification", "Medical Image Segmentation", "Remote Sensing", "Seismic Image Interpretation"]
related_tasks: ["Image Classification", "Semantic Segmentation", "Fault Detection", "Facies Classification"]
tags: [vision-transformer, transformer, self-attention, patch-tokenization, global-modeling]
created: 2026-07-19
---

# Definition / 定义

Vision Transformer (ViT) is a pure Transformer architecture applied directly to sequences of image patches, demonstrating that Transformers without convolutional inductive biases can scale effectively on large datasets and rival CNNs in image recognition.

# Core Idea / 核心思想

The key insight of ViT is that an image can be treated as a sequence of patches, each projected into a token embedding space, and then processed by a standard Transformer encoder — the same architecture that powers NLP success. Unlike CNNs that rely on local receptive fields and weight sharing, ViT models global interactions across all patches from the first layer via self-attention.

Core steps:
- **Image patch tokenization**: The input image is divided into fixed-size non-overlapping patches (e.g., 16x16 pixels).
- **Patch embedding**: Each patch is flattened and linearly projected into a d-dimensional embedding vector.
- **Positional encoding**: Since the Transformer is permutation-invariant, learned positional embeddings are added to preserve spatial information.
- **Transformer encoder**: The patch tokens are fed through stacked multi-head self-attention and MLP blocks.
- **Classification token (CLS)**: A learnable [CLS] token is prepended to the sequence; its final hidden state serves as the global image representation for classification.

# Architecture / Formulation / 架构/公式

Given an input image X ∈ ℝ^(H×W×C), it is partitioned into N patches P ∈ ℝ^(N×(P²×C)), where P is patch size (e.g., P=16).

## Patch Embedding

Each patch is linearly mapped to a d-dimensional embedding:
```
E = P.W_proj + b_proj    (N × d)
```

Positional encoding is added:
```
E' = E + PosEnc            (N × d)
```

A learnable [CLS] token is prepended:
```
X_input = [CLS; E']          (N+1 × d)
```

## Transformer Encoder Blocks

Each block contains:
1. **Multi-Head Self-Attention (MSA)**:
   ```
   MSA(Q,K,V) = Concat(head₁, head₂, ..., headₕ) · Wᴼ
   where headᵢ = Attention(QWᵢ^Q, KWᵢ^K, VWᵢ^V)
   ```
2. **MLP Block**:
   ```
   MLP(x) = Linear₂(Activation(Linear₁(x)))
   ```

With LayerNorm and residual connections applied throughout.

## Classification Head

The final hidden state of the [CLS] token is passed through a classifier:
```
y_hat = LayerNorm(CLSToken) → Linear → Softmax
```

# Advantages / 优势

- **Global receptive field**: Self-attention connects all patches in a single operation, unlike CNNs which require deep stacking to capture long-range dependencies.
- **Scalability with data and computation**: ViT scales predictably with dataset size and model capacity — it benefits more from large-scale training (e.g., ImageNet-21k, JFT-300M) than CNNs do.
- **Parameter efficiency at scale**: With sufficient data, ViT achieves better accuracy-to-parameter ratios than CNNs.
- **Architectural simplicity**: Uses the same Transformer blocks as NLP, enabling cross-domain knowledge transfer and unified architectures.
- **Parallelizable computation**: Self-attention over patches is inherently parallel, unlike the sequential nature of CNN convolutions at each layer.

# Limitations / 局限性

- **Large data requirement**: ViT lacks the local inductive bias of CNNs and therefore requires substantially more training data to achieve comparable performance on small datasets. Fine-tuning on pre-trained weights mitigates this.
- **Computational cost**: Quadratic attention complexity with respect to sequence length (N = HW/P²) makes training memory-intensive for high-resolution images.
- **Local inductive bias deficiency**: CNNs naturally exploit locality and translation equivariance; ViT must learn these properties from data, which is inefficient for small datasets.
- **Small dataset challenges**: For medical imaging, seismic interpretation, and other domains with limited labeled data, pure ViT underperforms compared to CNNs or hybrid approaches — unless pretrained on large domains or augmented with convolutional inductive biases.

# Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Image Classification | Pure ViT on ImageNet achieves competitive results with CNNs at scale | Dosovitskiy et al. (2020) |
| Medical Image Segmentation | ViT adapted for semantic segmentation via hierarchical or hybrid designs | TransUnet, SvIT |
| Remote Sensing | Land-use classification, change detection on satellite imagery | RS-ViT, SAT |
| Seismic Image Interpretation | Fault segmentation, facies classification, salt body delineation | SeisViT, fault-ViT |

# Related Papers / 相关论文

- Dosovitskiy et al. (2020) "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale" — 原始 ViT 论文，提出将纯 Transformer 应用于图像分类

# Related Methods / 相关方法

- [[Transformer]] — 原始 Transformer 架构，ViT 的基础
- [[SegFormer]] — 轻量级混合 Transformer 编码器用于语义分割
- [[U-SegFormer-Hyper]] — SegFormer 的超参数优化变体，针对地震图像分割
