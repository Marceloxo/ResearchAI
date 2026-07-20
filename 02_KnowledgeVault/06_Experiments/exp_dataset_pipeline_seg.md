---
experiment_id: "exp-dataset-pipeline-seg"
project: "seismic_seg_pipeline"
task: "Seismic Image Segmentation"
dataset: "F3 Netherlands"
method: "U-Net"
date: 2026-07-20
status: planned
priority: P1
tags: [dataset-pipeline, preprocessing, benchmark, seismic-segmentation, infrastructure]
created: 2026-07-20
---

# Experiment Objective / 实验目标

Build a standardized dataset loading, preprocessing, and evaluation pipeline for seismic image segmentation. This is the foundation for ALL subsequent experiments and the first paper.

**Target datasets**: F3 Netherlands (facies), Thebe (fault), SEG Salt (salt body), Parihaka (facies), Penobscot (facies)

# Hypothesis / 假设

A unified data pipeline with consistent preprocessing, train/val/test splits, and evaluation metrics will eliminate the "apples-to-oranges" comparison problem that plagues seismic segmentation literature.

# Configuration / 实验配置

- **Datasets / 数据集**:
  - [[F3 Netherlands]] — facies (primary benchmark)
  - [[Thebe]] — fault
  - [[SEG Salt]] — salt body
  - [[Parihaka]] — facies
  - [[Penobscot]] — facies
- **Task / 任务**: [[Seismic Image Segmentation]], [[Fault Segmentation]], [[Seismic Facies Segmentation]]
- **Preprocessing / 预处理**:
  - Standardize: normalize each seismic section to [0,1] or z-score
  - Patch size: determine optimal (e.g., 128×128, 256×256)
  - Data augmentation: random flip, rotation, elastic deformation
- **Evaluation Metrics / 评估指标**:
  - IoU (Intersection over Union)
  - Dice Coefficient
  - Pixel Accuracy
  - Precision / Recall / F1
- **Hardware / 硬件**: RTX 4070 12GB, Ubuntu 24.04
- **Code Location / 代码位置**: `/home/lco/ResearchAI/03_Projects/seismic_seg_pipeline/`

# Results / 实验结果

## Quantitative Results / 定量结果

| Dataset | # Samples | Patch Size | Classes | Metric |
|---------|-----------|------------|---------|--------|
| F3 Netherlands | — | — | 7 facies | IoU |
| Thebe | — | — | 2 (fault/bg) | IoU |
| SEG Salt | — | — | 2 (salt/bg) | IoU |

## Pipeline Components

1. **Data loader**: Download scripts, standardized directory structure, caching
2. **Preprocessing**: Normalization, patching, augmentation
3. **Train/val/test split**: Fixed random seed, documented split ratios
4. **Evaluation**: Unified metric computation, result logging
5. **Visualization**: Side-by-side prediction comparison, error maps

# Comparison / 对比分析

| Dataset | Previous Split | Our Split | Notes |
|---------|---------------|-----------|-------|
| F3 Netherlands | varies by paper | 70/15/15 | Standardize for reproducibility |
| Thebe | as published | 70/15/15 | Preserve original if possible |
| SEG Salt | varies | 70/15/15 | Standardize |

# Analysis / 分析

<!-- Pending execution -->

# Conclusion / 结论

<!-- Pending execution -->

# Related / 相关链接

- Method: [[U-Net]], [[SegFormer]], [[CNN]]
- Dataset: [[F3 Netherlands]], [[Thebe]], [[SEG Salt]], [[Parihaka]], [[Penobscot]]
- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]], [[Seismic Facies Segmentation]]
- Roadmap: [[Research_Roadmap]]