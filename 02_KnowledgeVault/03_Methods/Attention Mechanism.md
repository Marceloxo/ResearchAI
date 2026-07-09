---
method_name: "Attention Mechanism"
category: "Feature Enhancement Module"
application: ["Semantic Segmentation", "Image Classification", "Feature Refinement"]
related_tasks: ["Fault Segmentation", "Seismic Image Segmentation"]
tags: [attention, cnn, segmentation, deep-learning]
created: 2026-07-08
---

# Definition / 定义

Attention mechanisms are modules that allow neural networks to dynamically focus on the most relevant parts of the input or feature maps. They compute a weighting function over features, emphasizing important regions/channels and suppressing irrelevant ones.

# Core Idea / 核心思想

Not all features are equally important. Attention learns to assign importance weights to different spatial locations (spatial attention) or feature channels (channel attention), allowing the network to "pay attention" to what matters.

For seismic fault segmentation, attention is particularly effective: faults occupy a tiny fraction of the image (severe class imbalance). Attention helps the model focus on these sparse, thin structures rather than the dominant background.

# Architecture / Formulation / 架构/公式

## Channel Attention (SE-Net style)

$$
\text{Channel Weight} = \sigma(\text{MLP}(\text{GAP}(F)))
$$
$$
F_{\text{refined}} = F \odot \text{Channel Weight}
$$

Where GAP = Global Average Pooling, σ = sigmoid, ⊙ = channel-wise multiplication.

## Spatial Attention

$$
\text{Spatial Weight} = \sigma(\text{Conv}([\text{AvgPool}(F); \text{MaxPool}(F)]))
$$

## Attention Gate (used in Attention U-Net)

```
Gating Signal (from decoder) + Skip Connection (from encoder)
    ↓
1×1 Conv → ReLU → 1×1 Conv → Sigmoid
    ↓
Attention Coefficients (α) ∈ [0,1]
    ↓
Multiply with skip features → Attended features
```

The gating signal from the coarser scale helps the attention gate focus on relevant regions.

# Advantages / 优势

- Lightweight — small parameter overhead (typically <1% of base model)
- Plug-and-play — can be inserted into any CNN architecture
- Improves performance on imbalanced tasks (fault vs. background)
- Provides interpretability — attention maps show what the model focuses on
- Computationally cheap — negligible impact on inference speed

# Limitations / 局限性

- Local attention (spatial/channel) does not capture global dependencies like Transformer self-attention
- Attention gate is sensitive to initialization; may need careful tuning
- May overfit on small datasets if attention becomes too aggressive

# Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Fault Segmentation | Focus on thin fault lines | Attention U-Net for seismic faults |
| Medical Imaging | Focus on lesions/organs | Original Attention U-Net (Oktay 2018) |
| General Segmentation | Improve CNN feature maps | SE-Net, CBAM |

# Related Papers / 相关论文

- [[Literature-review-on-deep-learning-for-segmentation-of-seismic-images]] — Notes attention as a key enhancement for seismic segmentation

# Related Methods / 相关方法

- [[CNN]] — Base architecture that attention enhances
- [[U-Net]] — Attention U-Net adds attention gates to the skip connections
- [[Transformer]] — Full self-attention architecture; attention mechanisms are its building blocks
