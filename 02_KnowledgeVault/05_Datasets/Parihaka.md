---
dataset_name: "Parihaka"
domain: "Seismic"
size: "3D volume"
modality: "Seismic reflection data"
task: ["Lithofacies Segmentation"]
official_link: "https://www.pets.govt.nz/resources/geoscience-data/parihaka-3d-seismic-data/"
related_papers: ["Chevron (Inc)", "Wang et al. (2021)", "Li et al. (2022)", "Tolstaya and Egorov (2022)"]
tags: [seismic, facies-segmentation, benchmark]
created: 2026-07-08
---

# Dataset Overview / 数据集概述

The Parihaka dataset is an offshore New Zealand 3D seismic survey with a detailed geological interpretation provided by Chevron USA. It became publicly available in 2020 and has quickly gained popularity as a benchmark for facies segmentation.

- **Source / 来源**: New Zealand Petroleum & Minerals (NZPM) + Chevron interpretation
- **Purpose / 目的**: Lithofacies segmentation benchmark
- **License / 许可**: Creative Commons Attribution (Chevron interpretation)

# Data Format / 数据格式

- **File Format / 文件格式**: SEGY
- **Classes / 类别**: 6 lithofacies classes
- **Interpretation / 标注**: Provided by Chevron USA

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Classes / 类别 | 6 | Basement/Other, Slope Mudstone A, Mass Transport Deposit, Slope Mudstone B, Slope Valley, Submarine Canyon |

# Usage / 使用方式

- **Loading / 加载**: Standard SEGY reader
- **Preprocessing / 预处理**: Normalization, patch extraction
- **Data Location / 数据位置**: `D:\ResearchAI_Data\datasets\Parihaka`

# Benchmark Results / 基准结果

| Method | Metric | Year |
|---|---|---|
| DeepLabv3+ | PA: 97%, MCA: 92% | 2022 |
| UNet + EfficientNet B1 | PA: 94%, MCA: 96% | 2022 |
| UNet | PA: 95% | 2022 |

# Related Papers / 相关论文

- [[Paper - ]] — Chevron (Inc): Original interpretation
- [[Paper - ]] — Wang et al. (2021): Transfer learning from Parihaka to F3
- [[Paper - ]] — Li et al. (2022): Contrastive learning on Parihaka

# Limitations / 局限性

- Relatively recent addition to the benchmark pool (2020+)
- Limited number of published studies compared to F3 Netherlands
