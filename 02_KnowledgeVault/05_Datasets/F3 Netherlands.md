---
dataset_name: "F3 Netherlands"
domain: "Seismic"
size: "Large 3D volume"
modality: "Seismic reflection data"
task: ["Facies Segmentation", "Fault Detection"]
official_link: "https://wiki.seg.org/wiki/Elastic_waveform_inversion_aided_by_facies_classification"
related_papers: ["Alaudah et al. (2019)", "Silva et al. (2019)", "ConocoPhillips"]
tags: [seismic, facies-segmentation, benchmark]
source_type: public_dataset
created: 2026-07-08
---

# Dataset Overview / 数据集概述

The F3 Netherlands dataset is the most widely used benchmark for seismic facies segmentation. It has been released with multiple interpretations by different research groups, making it ideal for comparing methods.

- **Source / 来源**: SEG Wiki Open Data
- **Purpose / 目的**: Benchmark for seismic facies classification and fault detection
- **License / 许可**: Open data (SEG Wiki)

# Data Format / 数据格式

- **File Format / 文件格式**: SEGY (standard seismic format)
- **Dimensions / 维度**: 3D seismic volume
- **Annotation Format / 标注格式**: Multiple interpretation versions exist

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Full Volume | 3D | Complete survey area |

# Usage / 使用方式

- **Loading / 加载**: Standard SEGY reader
- **Preprocessing / 预处理**: Normalization, patch extraction
- **Data Location / 数据位置**: `D:\ResearchAI_Data\datasets\F3 Netherlands`

# Benchmark Results / 基准结果

| Method | Metric | Year |
|---|---|---|
| DeepLabv3+ | PA: 98%, mIoU: 94% | 2022 |
| UNet | PA: 97% | 2021 |
| SegNet | PA: 88% | 2020 |
| CNN Pixel Classification | PA: 88% | 2020 |

# Related Papers / 相关论文

- [[Paper - ]] — Alaudah et al. (2019): Released interpreted version with benchmark protocol
- [[Paper - ]] — Silva et al. (2019): Alternative interpretation
- [[Paper - ]] — ConocoPhillips: Private interpretation

# Limitations / 局限性

- Multiple interpretations exist, making direct comparison difficult
- Not all papers report which interpretation version they used
- Lack of standardized train/test splits in some studies

## Tasks Using This Dataset / 使用该数据集的任务
- [[Seismic Facies Segmentation]] — Standard benchmark; 7 facies classes; 640x640x384
- [[Fault Segmentation]] — Most widely used; includes fault labels
