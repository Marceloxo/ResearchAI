---
dataset_name: "Marmousi"
domain: "Seismic"
size: "Synthetic 3D volume"
modality: "Synthetic seismic data"
task: ["Seismic Interpretation", "Velocity Modeling"]
official_link: "https://www.egt.de/marmousi/"
related_papers: ["Billette and Laurain (1991)"]
tags: [seismic, synthetic, benchmark]
source_type: public_dataset
created: 2026-07-08
---

# Dataset Overview / 数据集概述

Marmousi is a classic synthetic seismic model created by the Consortium Project Structural Modeling European Black Oil Model. It represents a complex geological structure with realistic seismic response and is widely used for algorithm testing.

- **Source / 来源**: Consortium Project (European)
- **Purpose / 目的**: Testing seismic interpretation and inversion algorithms on complex geology
- **License / 许可**: Open synthetic model

# Data Format / 数据格式

- **File Format / 文件格式**: Synthetic (not SEGY originally, can be exported)
- **Nature / 性质**: Synthetic — ground truth is known exactly

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Classes / 类别 | Multiple | Complex geological layers |

# Usage / 使用方式

- **Loading / 加载**: Synthetic data format
- **Data Location / 数据位置**: `D:\ResearchAI_Data\datasets\Marmousi`

# Related Papers / 相关论文

- [[Paper - ]] — Billette and Laurain (1991): Original Marmousi model description

# Limitations / 局限性

- Synthetic data does not capture real-world noise and acquisition artifacts
- Limited direct applicability to field data interpretation

## Tasks Using This Dataset / 使用该数据集的任务
- [[Seismic Facies Segmentation]] — Complex velocity model; synthetic benchmark
- [[Seismic Image Segmentation]] — Classic benchmark model
