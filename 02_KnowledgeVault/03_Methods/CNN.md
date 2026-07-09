---
method_name: "CNN"
category: "Convolutional Neural Network"
application: ["Image Classification", "Semantic Segmentation", "Object Detection"]
related_tasks: ["Seismic Image Segmentation", "Fault Segmentation"]
tags: [cnn, deep-learning, segmentation]
created: 2026-07-08
---

# Definition / 定义

Convolutional Neural Networks (CNNs) are a class of deep neural networks that use convolution operations to extract hierarchical features from grid-structured data (images, volumes). They are the foundational architecture for most deep learning-based seismic image analysis.

# Core Idea / 核心思想

Replace fully-connected layers with convolutional filters that slide across the input, detecting local patterns (edges, textures, shapes) at increasing levels of abstraction through hierarchical layers.

Key properties:
- **Translation equivariance**: A pattern detected at one location is detected anywhere.
- **Parameter sharing**: Same filter applied across the entire input — dramatically fewer parameters than MLPs.
- **Hierarchical features**: Early layers detect edges/textures, deeper layers detect semantic structures.

# Architecture / Formulation / 架构/公式

## Basic CNN Layer

$$
\text{Output}(i,j) = \sum_{m}\sum_{n} \text{Input}(i+m, j+n) \cdot \text{Kernel}(m,n) + b
$$

## Typical CNN Pipeline for Segmentation

```
Input Image
    ↓
Conv + ReLU + Pool (repeat N times, decreasing resolution)
    ↓
Feature Maps (low resolution, high semantic content)
    ↓
Upsampling / Decoder (for segmentation tasks)
    ↓
Output (pixel-wise prediction)
```

# Advantages / 优势

- Efficient parameter usage via weight sharing
- Automatic hierarchical feature learning — no hand-crafted features needed
- Well-established, extensive literature and pre-trained models available
- Works well with limited data via transfer learning
- Computationally efficient on GPUs (fits RTX4070 well)

# Limitations / 局限性

- Limited receptive field — struggles with long-range dependencies
- Primarily local operations — may miss global context important for seismic structures
- Fixed kernel size — cannot adaptively adjust to feature scale
- Translation equivariance can be a limitation when absolute position matters

# Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Fault Segmentation | Identify faults in seismic images | [[Paper - ]] |
| Salt Segmentation | Identify salt bodies | [[Paper - ]] |
| Seismic Facies Classification | Classify geological facies | [[Paper - ]] |

# Related Papers / 相关论文

- [[Literature-review-on-deep-learning-for-segmentation-of-seismic-images]] — Survey covering CNN applications in seismic segmentation

# Related Methods / 相关方法

- [[U-Net]] — CNN encoder-decoder with skip connections (dominant for segmentation)
- [[ResNet]] — Residual CNN with skip connections for deeper training
- [[Transformer]] — Attention-based alternative to CNNs
- [[Attention Mechanism]] — Enhances CNNs with focus mechanisms
