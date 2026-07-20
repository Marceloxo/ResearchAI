---
title: "Machine-Learning-Based Analysis of the Guy-Greenbrier, Arkansas Earthquakes: A Tale of Two Sequences"
authors: [Yongsoo Park, S. Mostafa Mousavi, Weiqiang Zhu, William L. Ellsworth, Gregory C. Beroza]
year: 2020
venue: "Geophysical Research Letters"
task: [Induced Seismicity, Earthquake Cataloging, Wastewater Injection Analysis]
method: [PhaseNet, Phase Association, Hypocenter Relocation]
dataset: [Guy-Greenbrier Arkansas sequence, June 2010 - October 2011]
code_available: Not Checked
importance: medium
reading_status: keep-reference
tags: [induced-seismicity, guy-greenbrier, phasenet, wastewater-injection, arkansas, ml-catalog]
created: 2026-07-18
---

# Basic Information / 基本信息

- **Title**: Machine-Learning-Based Analysis of the Guy-Greenbrier, Arkansas Earthquakes: A Tale of Two Sequences
- **Authors**: Yongsoo Park, S. Mostafa Mousavi, Weiqiang Zhu, William L. Ellsworth, Gregory C. Beroza
- **Year**: 2020
- **Venue**: Geophysical Research Letters
- **Task**: ML-based earthquake cataloging of induced seismicity sequence
- **Method**: PhaseNet deep neural network picker + phase association + hypocenter relocation
- **Dataset**: Guy-Greenbrier, Arkansas (June 2010 - October 2011), ~90,000 events located
- **Code**: Not Checked

# Research Problem / 研究问题

Can PhaseNet-based cataloging reveal new insights into the Guy-Greenbrier induced seismicity sequence, particularly regarding the relationship between wastewater disposal wells and earthquake activity?

# Main Contribution / 主要贡献

Located nearly 90,000 events using PhaseNet on continuous data. Found the sequence consists of two adjacent subsequences on the same fault, with the second sequence potentially associated with a western disposal well rather than the previously implicated northern/eastern wells. Each sequence composed of small clusters exhibiting diffusion along the fault.

# Method Overview / 方法概述

1. Applied PhaseNet to continuous waveform data from Guy-Greenbrier region
2. Phase association and hypocenter relocation on ML-generated picks
3. Located ~90,000 events (vs. previous studies: 17,395 by Ogwari et al.; 460,000 detected but undetermined by Huang & Beroza)
4. Spatiotemporal analysis revealed two distinct subsequences

# Dataset and Evaluation / 数据集与评估

- **Period**: June 2010 - October 2011
- **Events located**: ~90,000
- **Previous catalogs**: Ogwari et al. (17,395 events), Huang & Beroza (460,000 detected, 1,740 located)
- **Evaluation**: Spatiotemporal pattern analysis, diffusion modeling

# Why This Paper Matters / 为什么关注篇论文

Demonstrates PhaseNet applied to induced seismicity — shows ML cataloging can reveal new insights about wastewater injection-induced earthquakes. The 90,000-event catalog is a significant improvement over previous studies.

# Limitations / 局限性

- PhaseNet used without ablation or comparison to other pickers
- Induced seismicity context differs from natural tectonic seismicity
- No quantitative error assessment of PhaseNet picks on this dataset
- Causal link between specific wells and seismicity remains probabilistic

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [x] Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: PhaseNet is publicly available (Mousavi & Beroza)

## Data Status / 数据可用性

- [x] **Public dataset available**
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: PhaseNet is public. Guy-Greenbrier seismic data should be accessible from US networks.

# My Decision / 我的决定

- [ ] Read deeply / 精读
- [x] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: Good demonstration of PhaseNet on induced seismicity. Useful reference for ML-based cataloging workflow.

# Related Knowledge / 相关知识链接

- Task: [[Induced Seismicity]], [[Earthquake Cataloging]]
- Method: [[PhaseNet]]
- Dataset: [[Guy-Greenbrier]]
