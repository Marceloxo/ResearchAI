---
title: "Literature Review on Deep Learning for the Segmentation of Seismic Images"
authors: [survey paper]
year: 2023
venue: "Survey/Review Journal"
task: ["Seismic Image Segmentation"]
methods: ["CNN", "U-Net", "Transformer", "Attention Mechanism", "GAN"]
datasets: ["F3 Netherlands", "Thebe", "SEG Salt", "Marmousi", "SEAM"]
metrics: ["IoU", "Dice", "Precision", "Recall", "Pixel Accuracy"]
code: "N/A"
importance: high
status: done
tags: [seismic-ai, segmentation, survey, key-paper, fault-segmentation, cnn, unet, transformer, attention]
created: 2026-07-08
---

# Paper Type / 论文类型

**Survey / Review Paper** — does not propose a new model. Provides a comprehensive taxonomy and synthesis of existing work.

# One Sentence Summary / 一句话总结

Comprehensive survey organizing deep learning methods for seismic image segmentation into a taxonomy of tasks (fault, salt, facies), method families (CNN, U-Net, Transformer, GAN, Attention), and datasets, providing the definitive entry point for research in this field.

# Research Landscape / 研究全景

## Domain: Deep Learning + Seismic Image Segmentation

Seismic image segmentation is a critical task in geophysical exploration. Traditional methods rely on manual interpretation or hand-crafted features. Deep learning, particularly CNN and U-Net architectures, has revolutionized this field by enabling automatic, high-accuracy segmentation.

### Why This Matters

- Oil & gas exploration depends on accurate subsurface interpretation
- Manual interpretation is time-consuming, subjective, and inconsistent
- Deep learning enables automation, consistency, and scalability

# Task Taxonomy / 任务分类

## 1. Fault Segmentation / 断层分割

Identify and delineate geological faults in 2D/3D seismic volumes.

- **Input**: 2D seismic sections or 3D seismic volumes
- **Output**: Binary fault probability maps or fault surfaces
- **Challenge**: Faults are thin, curvilinear, and sparse; class imbalance is severe
- **Key Methods**: U-Net, Attention U-Net, Fault-Net, 3D CNN

## 2. Salt Segmentation / 盐体分割

Identify salt bodies in seismic images.

- **Input**: 2D/3D seismic data
- **Output**: Binary salt masks
- **Challenge**: Salt bodies have complex geometries, varying textures
- **Key Methods**: U-Net, DeepLab, Attention U-Net, Residual U-Net

## 3. Seismic Facies Classification / 地震相分类

Classify seismic textures into geological facies categories.

- **Input**: Seismic volumes with texture patterns
- **Output**: Multi-class facies maps
- **Challenge**: Inter-class similarity, intra-class variation
- **Key Methods**: CNN, Encoder-Decoder, Transfer Learning

## 4. Horizon Tracking / 层位追踪

Track continuous geological horizons across seismic volumes.

- **Input**: 3D seismic volumes
- **Output**: Horizon surfaces
- **Challenge**: Discontinuities (faults), low signal-to-noise ratio
- **Key Methods**: CNN + Dynamic Programming, RNN

# Method Taxonomy / 方法分类

## CNN-Based / 卷积神经网络方法

### U-Net Family (Dominant Architecture)

The U-Net encoder-decoder with skip connections is the most widely used architecture for seismic segmentation.

- **Standard U-Net**: Symmetric encoder-decoder with skip connections; captures multi-scale features
- **Attention U-Net**: Adds attention gates to focus on relevant regions; particularly effective for faults
- **Residual U-Net**: Residual connections improve gradient flow for deeper networks
- **U-Net++**: Dense skip connections for better feature fusion
- **3D U-Net**: Extends to 3D for volumetric seismic data

Key insight: skip connections are essential — they preserve fine spatial details lost during downsampling, which is critical for thin structures like faults.

### Other CNN Architectures

- **DeepLab**: Atrous convolution for multi-scale context
- **PSPNet**: Pyramid pooling for global context
- **FCN**: Fully convolutional networks as baseline
- **LinkNet**: Lightweight encoder-decoder for efficiency

## Transformer-Based / Transformer方法

Emerging trend (~2021+). Transformers capture long-range dependencies that CNNs struggle with.

- **Vision Transformer (ViT)**: Patch-based transformer for images
- **Swin Transformer**: Hierarchical transformer with shifted windows
- **SegFormer**: Lightweight transformer encoder + simple MLP decoder
- **TransUNet**: Hybrid CNN-Transformer architecture

Advantage over CNNs: better at modeling global context and long-range fault continuity.
Disadvantage: higher computational cost, more data-hungry.

## Attention Mechanisms / 注意力机制

Attention modules enhance CNNs without full transformer architecture.

- **Channel Attention (SE-Net)**: Re-weights feature channels
- **Spatial Attention**: Focuses on relevant spatial locations
- **Self-Attention**: Captures non-local dependencies within feature maps
- **CBAM**: Combined channel + spatial attention

Attention is particularly effective for fault segmentation — it helps the model focus on thin, subtle fault lines.

## GAN-Based / 生成对抗网络

- **cGAN**: Conditional GAN for segmentation (Pix2Pix style)
- **CycleGAN**: Domain adaptation across seismic surveys
- **GAN-based augmentation**: Generate synthetic seismic data

GANs are more commonly used for data augmentation (generating synthetic training samples) than for direct segmentation.

## Hybrid Methods / 混合方法

Combining multiple techniques:

- CNN + Transformer hybrids
- CNN + Graph Neural Networks for fault connectivity
- Physics-informed neural networks for seismic inversion + segmentation

# Dataset Overview / 数据集概览

## Fault Detection Datasets

| Dataset | Description | Key Feature |
|---|---|---|
| **F3 Netherlands** | Real 3D seismic survey, manually interpreted faults | Widely used benchmark; includes seismic + fault labels |
| **Thebe** | Fault benchmark dataset with multiple interpreters | Multi-expert labels; captures annotation uncertainty |
| **Kerry3D** | 3D seismic with fault annotations | Large-scale 3D fault detection |

## Salt Detection Datasets

| Dataset | Description | Key Feature |
|---|---|---|
| **SEG Salt** | TGS Salt Identification Challenge dataset | Industry-standard salt benchmark |
| **SEG Advanced Modeling (SEAM)** | Synthetic 3D model with salt bodies | High-quality synthetic data |

## Synthetic/General Datasets

| Dataset | Description | Key Feature |
|---|---|---|
| **Marmousi** | 2D synthetic seismic model | Classic benchmark; complex geological structures |
| **SEAM** | SEG Advanced Modeling Program | Realistic 3D synthetic; multiple geological features |

# Future Research Opportunities / 未来研究方向

Based on the survey's gap analysis:

## 1. Lightweight and Efficient Models / 轻量化高效模型

Most SOTA models are large and computationally expensive. Opportunity for:
- Lightweight U-Net variants (fewer parameters, faster inference)
- Knowledge distillation from large to small models
- Mobile/edge deployment for field use

**Suitable for RTX4070 (12GB VRAM)**: 2D models fit easily; 3D models may need patch-based or lightweight approaches.

## 2. Limited Labeled Data / 有限标注数据

Seismic annotation is expensive and requires expertise. Opportunities:
- Self-supervised pre-training on unlabeled seismic data
- Semi-supervised learning leveraging unlabeled volumes
- Few-shot segmentation with minimal annotation
- Transfer learning from synthetic to real data

## 3. Multi-Task Learning / 多任务学习

Simultaneously segment faults, horizons, and facies — these tasks share geological context.

## 4. Uncertainty Quantification / 不确定性量化

Seismic interpretation is inherently uncertain. Models that output confidence maps are more useful to interpreters.

## 5. 3D vs 2D Approaches / 3D vs 2D

3D models capture spatial continuity but are computationally expensive. Hybrid approaches (2D slices + 3D context) are promising.

## 6. Foundation Models / 基础模型

Pre-training large models on massive seismic datasets, then fine-tuning for specific tasks — analogous to what happened in NLP and general CV.

# My Analysis / 我的分析

## Directions Suitable for RTX4070 / 适合RTX4070的方向

RTX4070 has 12GB VRAM — capable but not workstation-class. Good fits:

1. **2D fault segmentation**: 2D U-Net variants fit easily. Batch size 8-16 is comfortable.
2. **Lightweight 3D models**: Patch-based 3D or 2.5D approaches. Full 3D volumes may need aggressive patching.
3. **Attention modules on top of CNN backbone**: Adds capability without massive parameter increase.
4. **Transfer learning**: Fine-tune pre-trained models rather than train from scratch.
5. **Self-supervised pre-training**: Requires only unlabeled data, runs efficiently on consumer GPUs.

Avoid: training large 3D Transformers from scratch, large-scale GANs, full-volume 3D segmentation without patching.

## Lightweight Model Opportunities / 轻量化模型机会

- **MobileNet/ShuffleNet backbones**: Replace heavy ResNet/VGG encoders
- **Depth-wise separable convolutions**: Reduce parameters 8-10x
- **Pruning + Quantization**: Post-training optimization for deployment
- **Knowledge distillation**: Train a small student model from a large teacher

## CV Method Transfer Opportunities / CV方法迁移机会

Many advances from general computer vision can be adapted:

- **Boundary-aware losses** (from medical imaging edge detection) → fault segmentation
- **Contrastive learning** (SimCLR, MoCo) → self-supervised pre-training on seismic
- **SAM (Segment Anything Model)** → zero-shot seismic segmentation? Unclear if it generalizes to seismic textures
- **Denoising diffusion models** → seismic data enhancement before segmentation

# Related Notes / 相关笔记

- Topic: [[Seismic AI]]
- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[CNN]], [[U-Net]], [[Transformer]], [[Attention Mechanism]]
- Dataset: [[F3 Netherlands]], [[Thebe]], [[SEG Salt]], [[Marmousi]]
