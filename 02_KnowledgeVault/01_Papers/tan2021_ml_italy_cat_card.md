---
title: "Machine-Learning-Based High-Resolution Earthquake Catalog Reveals How Complex Fault Structures Were Activated during the 2016–2017 Central Italy Sequence"
authors: [Yen Joe Tan, Felix Waldhauser, William L. Ellsworth, Miao Zhang, Weiqiang Zhu, Maddalena Michele, Lauro Chiaraluce, Gregory C. Beroza, Margarita Segou]
year: 2021
venue: "The Seismic Record"
task: [Earthquake Cataloging, Fault Structure Imaging, Seismic Monitoring]
method: [PhaseNet, Hypocenter Relocation, Dense Network Analysis]
dataset: [Central Italy 139-station network, 2016-2017 Amatrice-Visso-Norcia sequence]
code_available: Not Checked
importance: medium
reading_status: keep-reference
tags: [earthquake-catalog, phase-picking, central-italy, fault-structure, machine-learning]
created: 2026-07-18
---

# Basic Information / 基本信息

- **Title**: Machine-Learning-Based High-Resolution Earthquake Catalog Reveals How Complex Fault Structures Were Activated during the 2016–2017 Central Italy Sequence
- **Authors**: Yen Joe Tan, Felix Waldhauser, William L. Ellsworth, Miao Zhang, Weiqiang Zhu, Maddalena Michele, Lauro Chiaraluce, Gregory C. Beroza, Margarita Segou
- **Year**: 2021
- **Venue**: The Seismic Record
- **Task**: Earthquake cataloging and fault structure imaging using ML-based phase picking
- **Method**: PhaseNet deep neural network picker + hypocenter relocation on 139-station dense network
- **Dataset**: Central Italy 139-station network, 2016-2017 Amatrice-Visso-Norcia sequence (~900,000 events)
- **Code**: Not Checked

# Research Problem / 研究问题

How did complex fault structures activate during the 2016-2017 central Italy seismic sequence? Can ML-based cataloging reveal fault geometries invisible to routine monitoring?

# Main Contribution / 主要贡献

Built a high-precision catalog of ~900,000 earthquakes from 139 stations over 1 year using PhaseNet, an order of magnitude more events than routine INGV catalog. Aftershock activity reveals complex fault geometries including complementary structures to 1997 Colfiorito and 2009 L'Aquila sequences.

# Method Overview / 方法概述

1. Continuous data from 139 seismic stations processed with PhaseNet for arrival times
2. Generated ~900,000 earthquake catalog spanning 1 year (Aug 2016 - Aug 2017)
3. Aftershock spatial distribution used to delineate fault geometry
4. Compared with previous catalogs (INGV routine: ~82,000 events; Chiaraluce et al.: ~26,000 events)

# Dataset and Evaluation / 数据集与评估

- **139-station dense network** in central Italy covering 80 km fault system
- **Sequence**: Mw 6.0 Amatrice (Aug 24, 2016), Mw 5.9 Visso (Oct 26), Mw 6.5 Norcia (Oct 30)
- **Comparison**: Routine INGV catalog (82,000 events) vs ML catalog (900,000 events)
- **Metrics**: Event detection count, spatial resolution of fault structures

# Why This Paper Matters / 为什么关注这篇论文

Demonstrates the power of ML-based phase picking for large-scale seismic cataloging. The 10x improvement in event detection reveals fault complexity invisible to conventional methods. Relevant for understanding how earthquake sequences activate complex fault networks — applicable to seismic hazard assessment in central Italy and similar regions.

# Limitations / 局限性

- PhaseNet was used as a black box — no ablation on picker choice
- Study focuses on catalog building, not detailed source physics
- Dense network only available for this specific sequence — generalizability to sparse networks unclear
- No quantitative comparison of relocated vs unrelocated event statistics

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

## Data Status / 数据可用性

- [x] **Public dataset available** — seismic data from Italian network
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: PhaseNet is publicly available. Seismic data from INGV network may be accessible. However, the full processing workflow and station metadata may not be fully documented.

# My Decision / 我的决定

- [ ] Read deeply / 精读
- [x] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: Important demonstration of ML-based cataloging at scale, but primarily a seismological study rather than a methodological contribution. Useful as reference for dense network analysis and fault structure imaging.

# Related Knowledge / 相关知识链接

- Task: [[Earthquake Cataloging]], [[Fault Structure Imaging]]
- Method: [[PhaseNet]]
- Dataset: [[Central Italy Seismic Network]]
