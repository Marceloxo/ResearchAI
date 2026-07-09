---
dataset_name: "SEAM"
domain: "Seismic"
size: "Synthetic 3D volume"
modality: "Synthetic seismic data"
task: ["Seismic Interpretation", "Velocity Modeling"]
official_link: "https://seg.org/Community/SEAM"
related_papers: ["SEG Wiki"]
tags: [seismic, synthetic, benchmark]
created: 2026-07-08
---

# Dataset Overview / 数据集概述

SEAM (Seismic Modelling And Imaging Workshop) is a series of synthetic benchmarks maintained by SEG for testing seismic imaging and interpretation algorithms. The models include increasingly complex geological structures.

- **Source / 来源**: SEG Workshop
- **Purpose / 目的**: Standardized benchmark for seismic imaging and interpretation
- **License / 许可**: Open data (SEG Wiki)

# Data Format / 数据格式

- **File Format / 文件格式**: Synthetic
- **Nature / 性质**: Ground truth is known exactly (synthetic)

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Versions / 版本 | Multiple | SEG I, SEG II, etc. |

# Usage / 使用方式

- **Data Location / 数据位置**: `D:\ResearchAI_Data\datasets\SEAM`

# Related Papers / 相关论文

- [[Paper - ]] — SEG Wiki: SEAM model documentation

# Limitations / 局限性

- Synthetic data — limited transfer to field data
- Focused on imaging rather than segmentation
