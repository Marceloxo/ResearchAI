---
task_name: "Seismic Image Segmentation"
domain: "Seismic AI / Computer Vision"
input: "2D Seismic Sections or 3D Seismic Volumes"
output: "Pixel-wise or Voxel-wise Label Maps (binary or multi-class)"
metrics: ["IoU", "Dice Coefficient", "Precision", "Recall", "Pixel Accuracy"]
tags: [seismic-ai, segmentation, task]
created: 2026-07-08
---

# Task Definition / 任务定义

Seismic Image Segmentation is the task of assigning a label to each pixel (2D) or voxel (3D) in seismic data, identifying geological structures such as faults, salt bodies, and facies.

# Problem Formulation / 问题形式化

- **Given / 给定**: A seismic image/section $X \in \mathbb{R}^{H \times W}$ (2D) or volume $X \in \mathbb{R}^{D \times H \times W}$ (3D)
- **Goal / 目标**: Predict a label map $Y$ where each pixel/voxel is assigned a class label
  - Binary case: $Y \in \{0,1\}^{H \times W}$ (e.g., fault vs. non-fault)
  - Multi-class case: $Y \in \{1,...,C\}^{H \times W}$ (e.g., facies categories)

# Input Data / 输入数据

- **Modality / 模态**: Seismic amplitude data (post-stack or pre-stack)
- **Typical Dimensions / 典型维度**: 
  - 2D sections: 256×256 to 1024×1024 pixels
  - 3D volumes: 128×256×256 to 512×512×512 voxels
- **Characteristics / 特点**: 
  - Low signal-to-noise ratio
  - Structures appear as coherent reflections
  - Thin curvilinear features (faults), blob-like features (salt)

# Output / 输出

- **Type / 类型**: Dense pixel-wise prediction map
- **Format / 格式**: Same resolution as input; binary mask or multi-class label map
- **Resolution / 分辨率要求**: Must preserve fine details (thin faults, precise boundaries)

# Evaluation Metrics / 评估指标

| Metric | Formula | Description |
|---|---|---|
| IoU (Jaccard) | $\frac{TP}{TP+FP+FN}$ | Intersection over Union — standard segmentation metric |
| Dice (F1) | $\frac{2TP}{2TP+FP+FN}$ | Harmonic mean of precision and recall |
| Precision | $\frac{TP}{TP+FP}$ | How many predicted positives are correct |
| Recall | $\frac{TP}{TP+FN}$ | How many actual positives are detected |
| Pixel Accuracy | $\frac{TP+TN}{Total}$ | Overall correct classification (can be misleading for imbalanced classes) |

# Common Methods / 常用方法

| Method Family | Representative Work | Key Idea | Performance |
|---|---|---|---|
| U-Net | [[U-Net]] | Encoder-decoder with skip connections | Strong baseline |
| Attention U-Net | Attention U-Net | Attention gates on skip connections | Improved for thin structures |
| Transformer | SegFormer, Swin-Unet | Global self-attention | Emerging, competitive |
| CNN + Attention | [[CNN]] + [[Attention Mechanism]] | Lightweight enhancement | Good balance of speed/accuracy |

# Challenges / 挑战

- **Severe class imbalance**: Faults occupy <5% of pixels; standard losses are biased toward background
- **Thin, curvilinear structures**: Faults are only 1-3 pixels wide; easy to miss or break
- **Noisy data**: Seismic data has low signal-to-noise ratio; models must be robust
- **Limited labeled data**: Expert annotation is expensive and time-consuming
- **Annotation uncertainty**: Different interpreters label differently; ground truth is fuzzy

# Benchmark Datasets / 基准数据集

| Dataset | Size | Year | Notes |
|---|---|---|---|
| [[F3 Netherlands]] | Large 3D survey | 2019 | Widely used fault benchmark |
| [[Thebe]] | 3D + multi-expert labels | 2020 | Captures annotation uncertainty |
| [[SEG Salt]] | 2D/3D | 2018 | Kaggle competition dataset |
| [[Marmousi]] | 2D synthetic | 1988 | Classic benchmark model |

# Open Problems / 开放问题

- How to segment faults with minimal labeled data (few-shot, self-supervised)?
- How to ensure fault continuity (topological correctness, not just pixel accuracy)?
- How to handle 3D data efficiently on consumer GPUs (RTX4070)?
- How to transfer models across different seismic surveys (domain adaptation)?
- How to quantify and communicate prediction uncertainty to interpreters?
