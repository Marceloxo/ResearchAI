---
task_name: "Fault Segmentation"
domain: "Seismic AI / Structural Interpretation"
input: "2D Seismic Sections or 3D Seismic Volumes"
output: "Binary Fault Probability Maps"
metrics: ["IoU", "Dice", "Precision", "Recall"]
tags: [seismic-ai, fault-segmentation, segmentation, task]
created: 2026-07-08
---

# Task Definition / 任务定义

Fault Segmentation is the task of automatically identifying and delineating geological faults in seismic images. Faults appear as discontinuities in seismic reflections where rock layers have fractured and shifted.

This is the primary research task for the current ResearchAI focus.

# Problem Formulation / 问题形式化

- **Given / 给定**: A 2D seismic section $X \in \mathbb{R}^{H \times W}$ (or 3D volume)
- **Goal / 目标**: Predict a binary fault probability map $Y \in [0,1]^{H \times W}$ where each pixel indicates the likelihood of a fault
  - Threshold at 0.5 for binary fault/non-fault classification
  - Higher values = higher confidence of fault presence

# Input Data / 输入数据

- **Modality / 模态**: Post-stack seismic amplitude data
- **Typical Dimensions / 典型维度**: 256×256 to 512×512 (2D sections); 128×256×256 (3D patches)
- **Characteristics / 特点**: 
  - Faults appear as breaks/discontinuities in otherwise continuous reflectors
  - Very thin (1-3 pixels wide), curvilinear, often branching/intersecting
  - Severe class imbalance: <5% of pixels are faults

# Output / 输出

- **Type / 类型**: Dense probability map (continuous) or binary mask (thresholded)
- **Format / 格式**: Same resolution as input; values in [0,1] or {0,1}
- **Resolution / 分辨率要求**: Must preserve single-pixel-width fault lines; coarse outputs lose fault connectivity

# Evaluation Metrics / 评估指标

| Metric | Formula | Description |
|---|---|---|
| IoU | $\frac{TP}{TP+FP+FN}$ | Standard; penalizes both false positives and false negatives |
| Dice | $\frac{2TP}{2TP+FP+FN}$ | More sensitive to small objects than IoU |
| Precision | $\frac{TP}{TP+FP}$ | Important: we don't want false fault detections |
| Recall | $\frac{TP}{TP+FN}$ | Important: we don't want to miss real faults |

Note: Pixel-wise metrics don't capture topological correctness. A broken fault line may have good pixel metrics but poor structural accuracy.

# Common Methods / 常用方法

| Method Family | Representative Work | Key Idea | Performance |
|---|---|---|---|
| U-Net | [[U-Net]] | Skip connections for precise localization | Strong baseline |
| Attention U-Net | Attention U-Net | Focus on thin fault regions | Improved recall |
| Residual U-Net | Fault-Net | Deeper network for complex patterns | State-of-the-art |
| 3D CNN | 3D U-Net | Leverage 3D spatial continuity | Best for 3D data |
| Transformer | Swin-Unet | Global context for fault connectivity | Emerging |

# Challenges / 挑战

- **Extreme class imbalance**: Faults are ~1-5% of pixels; standard cross-entropy fails
- **Thin structures**: 1-3 pixel width; downsampling in encoders can lose faults entirely
- **Fault connectivity**: Pixel-wise metrics don't ensure faults are continuous lines
- **Annotation uncertainty**: Different geologists label faults differently; "ground truth" is fuzzy
- **Domain shift**: Models trained on one seismic survey may not generalize to another

# Benchmark Datasets / 基准数据集

| Dataset | Size | Year | Notes |
|---|---|---|---|
| [[F3 Netherlands]] | Large 3D survey | 2019 | Most widely used; includes fault labels |
| [[Thebe]] | 3D + multi-expert | 2020 | Multiple interpreters; captures uncertainty |

# Open Problems / 开放问题

- Can we ensure topological correctness (continuous fault lines) rather than just pixel accuracy?
- How to train with minimal labeled data? (self-supervised pre-training on unlabeled seismic)
- Can lightweight models (suitable for RTX4070) match heavy 3D models?
- How to transfer fault detection models across different geological settings?
- Can we jointly detect faults AND estimate their properties (dip, throw, type)?
