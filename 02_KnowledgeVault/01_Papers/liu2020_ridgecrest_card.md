---
title: "Rapid Characterization of the July 2019 Ridgecrest, California Earthquake Sequence from Raw Seismic Data using Machine Learning Phase Picker"
authors: [Liu, Zhang, Zhu, Ellsworth, Li]
year: 2020
venue: "Geophysical Research Letters"
task: [Earthquake Catalog Building, Phase Picking, Seismicity Characterization]
method: [PhaseNet, REAL, VELEST, hypoDD]
dataset: [Ridgecrest 2019, SCSN]
code_available: N/A (uses existing PhaseNet)
importance: medium-high
reading_status: done
tags: [phasenet, ridgecrest, earthquake-catalog, machine-learning, phase-picking, liu-zhang]
created: 2026-07-09
---

# Basic Information / 基本信息

- **Title**: Rapid Characterization of the July 2019 Ridgecrest, California Earthquake Sequence from Raw Seismic Data using Machine Learning Phase Picker
- **Authors**: Min Liu, Miao Zhang, Weiqiang Zhu, William L. Ellsworth, Hongyi Li
- **Year**: 2020
- **Venue**: Geophysical Research Letters
- **Task**: Earthquake catalog building from raw continuous data using ML picker
- **Method**: PhaseNet (picking) + REAL (association) + VELEST/hypoDD (relocation)
- **Dataset**: Ridgecrest 2019 sequence (MW 6.4 + MW 7.1), SCSN network
- **Code**: Uses PhaseNet (Zhu & Beroza 2019) — code available at https://github.com/weiqiangzhu/PhaseNet

# Research Problem / 研究问题

> 从原始连续波形数据中，无需先验信息，自动构建高精度地震目录，揭示2019年Ridgecrest地震序列的时空演化。

# Main Contribution / 主要贡献

> 首次使用PhaseNet+sequential workflow从Ridgecrest原始数据自动构建了包含15,445个事件的hypoDD目录，比SCSN常规目录多2倍事件，清晰定义了多条隐伏断层结构。

# Method Overview / 方法概述

> 三步工作流：(1) PhaseNet拾波 → (2) REAL关联定位 → (3) VELEST绝对定位+hypoDD相对定位。严格筛选条件（≥13个震相，≤200°台站间隙，≤0.6s走时残差）。

# Dataset and Evaluation / 数据集与评估

- **Ridgecrest 2019**: MW 6.4 (Jul 4) + MW 7.1 (Jul 6)，45个台站，120km范围内
- **评估**: 与SCSN常规目录、routine CC目录对比
- **结果**: 15,445 events (hypoDD) vs 7,743 events (SCSN) — 2倍提升

# Why This Paper Matters / 为什么关注这篇论文

> 展示了PhaseNet在实际地震序列中的泛化能力（从北加州训练→南加州Ridgecrest应用）。证明了ML拾波器可以用于近实时地震目录构建，为未来地震监测提供了实用工作流。

# Limitations / 局限性

> 依赖PhaseNet预训练模型（需外部代码）。REAL关联算法需要调参（阈值设置严格）。未测试对其他地震序列的泛化性。hypoDD定位依赖初始速度模型。

# Reproducibility Status / 可复现性状态

> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: N/A (paper uses PhaseNet, not a new method)

## Data Status / 数据状态

- [ ] **Public dataset available** — freely downloadable
- [x] **Restricted dataset** — requires application (SCSN data via IRIS)
- [ ] Private dataset
- [ ] Unknown

**Dataset Link**: IRIS (iris.edu), SCEC (scec.org)

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: 方法基于现有工具链（PhaseNet + REAL + VELEST + hypoDD），但需要获取Southern California地震台阵数据，且REAL算法细节不完全公开。

**Notes / 备注**:
- 论文本身不提出新方法，而是应用工作流
- PhaseNet代码开源，REAL/VELEST/hypoDD各有开源实现
- 数据获取需要IRIS/SCEC账号

## Zotero

**Status**: Imported
**Item Key**: K9XWQTIL

# My Decision / 我的决定

- [ ] Read deeply / 精读
- [x] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: 这是一篇应用论文，展示了PhaseNet在Ridgecrest地震序列上的实际效果。方法论上没有新颖贡献，但对理解ML方法在实际地震序列中的表现有价值。作为Reference保存。

# Related Knowledge / 相关知识链接

- Task: [[Seismic Phase Picking]]
- Method: [[PhaseNet]], [[CNN]]
- Dataset: [[EGS Collab SURF]]
