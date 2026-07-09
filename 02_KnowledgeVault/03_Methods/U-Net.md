---
method_name: "U-Net"
category: "CNN Encoder-Decoder"
application: ["Semantic Segmentation", "Biomedical Imaging", "Seismic Segmentation"]
related_tasks: ["Seismic Image Segmentation", "Fault Segmentation"]
tags: [unet, cnn, segmentation, encoder-decoder, deep-learning]
created: 2026-07-08
---

# Definition / 定义

U-Net is a symmetric encoder-decoder CNN architecture with skip connections between corresponding encoder and decoder layers. Originally proposed for biomedical image segmentation, it has become the dominant architecture for seismic image segmentation tasks.

# Core Idea / 核心思想

The encoder progressively downsamples to capture semantic context ("what"). The decoder progressively upsamples to recover spatial precision ("where"). Skip connections directly pass fine-grained spatial information from encoder to decoder, enabling precise localization despite the bottleneck.

This is critical for seismic tasks: faults and salt boundaries are thin structures that require both global context (to understand the geological setting) and local precision (to delineate exact boundaries).

# Architecture / Formulation / 架构/公式

## U-Net Structure

```
Input (e.g., 256x256 seismic section)
    ↓ [Encoder: Conv → Conv → MaxPool] ×4
    ↓ Bottleneck (lowest resolution, highest semantics)
    ↓ [Decoder: UpConv → Concat(skip) → Conv → Conv] ×4
    ↓
Output (same resolution as input, e.g., fault probability map)
```

## Key Components

- **Encoder**: Standard CNN (VGG-style or ResNet backbone), halves resolution at each stage
- **Bottleneck**: Deepest layer with largest receptive field
- **Decoder**: Transposed convolution or upsampling + convolution, doubles resolution each stage
- **Skip Connections**: Concatenate encoder features with decoder features at same resolution

# Advantages / 优势

- Excellent for tasks requiring precise localization (faults, boundaries)
- Multi-scale feature capture via hierarchical encoder-decoder
- Skip connections preserve fine spatial details
- Works well with moderate training data (hundreds to thousands of images)
- Many proven variants: Attention U-Net, Residual U-Net, U-Net++, 3D U-Net
- Fits comfortably on RTX4070 (12GB) for 2D and patch-based 3D

# Limitations / 局限性

- Limited receptive field — may miss very long-range geological structures
- Fixed architecture — less flexible than Transformer for modeling global dependencies
- 3D U-Net is memory-intensive; full-volume 3D may exceed RTX4070 capacity
- Performance depends on quality and quantity of labeled training data

# Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Fault Segmentation | 2D/3D fault detection in seismic volumes | Fault-Net, Attention U-Net |
| Salt Segmentation | Salt body delineation | Residual U-Net, TGS Salt Challenge |
| Biomedical Segmentation | Cell/Organ segmentation | Original U-Net paper (Ronneberger 2015) |

# Related Papers / 相关论文

- [[Literature-review-on-deep-learning-for-segmentation-of-seismic-images]] — Discusses U-Net and variants as dominant methods
- [[Paper - U-Net (Ronneberger 2015)]] — Original U-Net paper

# Related Methods / 相关方法

- [[CNN]] — Parent architecture family
- [[Attention Mechanism]] — Attention U-Net: adds attention gates to U-Net
- [[ResNet]] — Residual U-Net: replaces standard conv blocks with residual blocks
- [[Transformer]] — TransUNet: hybrid CNN-Transformer architecture
