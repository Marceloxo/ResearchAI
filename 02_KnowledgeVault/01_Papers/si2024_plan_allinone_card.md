---
title: "An all-in-one seismic phase picking, location, and association network for multi-task multi-station earthquake monitoring"
authors: [Xu Si, Xinming Wu, Zefeng Li, Shenghou Wang, Jun Zhu]
year: 2024
venue: "Communications Earth & Environment"
task: [Seismic Phase Picking, Earthquake Location, Phase Association]
method: [PLAN GNN, Multi-task Network, Inter-station Constraints]
dataset: [Ridgecrest region, Japan]
code_available: Not Checked
importance: high
reading_status: deep-read
tags: [plan, graph-neural-network, multi-task, phase-picking, earthquake-location, phase-association, ridgecrest, japan]
created: 2026-07-18
---

# Basic Information / 基本信息

- **Title**: An all-in-one seismic phase picking, location, and association network for multi-task multi-station earthquake monitoring
- **Authors**: Xu Si, Xinming Wu, Zefeng Li, Shenghou Wang, Jun Zhu
- **Year**: 2024
- **Venue**: Communications Earth & Environment (Nature Portfolio)
- **Task**: Simultaneous seismic phase picking, association, and location
- **Method**: PLAN — Graph Neural Network operating on multi-station seismic data with inter-task and inter-station constraints
- **Dataset**: Ridgecrest region (California), Japan seismic network
- **Code**: Not Checked

# Research Problem / 研究问题

Can a single neural network architecture perform all three earthquake monitoring tasks (phase picking, association, location) simultaneously, leveraging inter-task and inter-station physical relationships?

# Main Contribution / 主要贡献

Proposed PLAN, the first all-in-one system achieving simultaneous phase picking, association, and location with multi-station data. Outperforms previous DL-based methods on Ridgecrest and Japan data. Demonstrates that inter-station and inter-task constraints improve accuracy and physical consistency.

# Method Overview / 方法概述

1. **Module 1**: Waveform feature extraction using encoder-decoder architecture
2. **Module 2**: Earthquake location — encodes station coordinates (lon, lat, elevation) merged with waveform features to predict depth and epicentral distance
3. **Module 3**: Phase association — uses predicted location info to estimate time shifts for aligning multi-station waveform features
4. **Module 4**: Phase picking — aggregates aligned features for simultaneous multi-station phase picking
5. **GNN architecture**: Encodes inter-station geographic relationships and inter-task physical constraints

# Dataset and Evaluation / 数据集与评估

- **Ridgecrest region, California**: Well-recorded sequence with established benchmarks
- **Japan seismic network**: Dense station coverage for testing generalization
- **Comparison**: Against state-of-the-art DL phase-picking and localization methods
- **Metrics**: Picking accuracy, association correctness, location precision

# Why This Paper Matters / 为什么关注这篇论文

Highly relevant — PLAN represents a paradigm shift from separate task pipelines to unified multi-task learning. The graph-based approach encoding inter-station relationships is directly applicable to dense seismic networks. The multi-task formulation could improve phase picking for seismic monitoring applications.

# Limitations / 局限性

- GNN architecture complexity may require significant computational resources
- Performance on sparse networks not evaluated
- Multi-task training may introduce trade-offs between individual task performance
- Physical consistency of inter-task constraints not rigorously validated

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

## Data Status / 数据可用性

- [x] **Public dataset available**
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: Architecture is well-described with four interdependent modules. Data from Ridgecrest and Japan are publicly available. Code availability uncertain.

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: Novel multi-task GNN approach to earthquake monitoring. Direct relevance to seismic phase picking research. The all-in-one architecture represents a significant advancement over sequential pipeline approaches.

# Related Knowledge / 相关知识链接

- Task: [[Seismic Phase Picking]], [[Earthquake Location]], [[Phase Association]]
- Method: [[PLAN]], [[Graph Neural Network]], [[Multi-task Learning]]
- Dataset: [[Ridgecrest]], [[Japan Seismic Network]]
