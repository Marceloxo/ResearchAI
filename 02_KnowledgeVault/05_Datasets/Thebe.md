---
dataset_name: "Thebe Fault Benchmark"
domain: "Seismic"
size: "2D/3D sections"
modality: "Seismic reflection data"
task: ["Fault Segmentation"]
official_link: "https://github.com/aoschwamm/Thebe_Fault_Benchmark"
related_papers: ["Schwamm et al."]
tags: [seismic, fault-segmentation, benchmark]
created: 2026-07-08
---

# Dataset Overview / 数据集概述

The Thebe dataset is a multi-expert interpreted fault benchmark. It was created to provide a fair evaluation of fault detection algorithms by having multiple experts annotate the same seismic section, capturing annotation uncertainty.

- **Source / 来源**: Multi-expert interpretation
- **Purpose / 目的**: Fault detection benchmark with expert-annotated ground truth
- **License / 许可**: Open benchmark

# Data Format / 数据格式

- **File Format / 文件格式**: Seismic sections with expert annotations
- **Task / 任务**: Binary fault segmentation

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Experts / 专家 | Multiple | Inter-annotator agreement measured |

# Usage / 使用方式

- **Loading / 加载**: Standard seismic format with annotation masks
- **Data Location / 数据位置**: `D:\ResearchAI_Data\datasets\Thebe`

# Related Papers / 相关论文

- [[Paper - ]] — Schwamm et al.: Multi-expert fault interpretation

# Limitations / 局限性

- Limited to fault detection only (not facies segmentation)
- Smaller published user base compared to F3 Netherlands
