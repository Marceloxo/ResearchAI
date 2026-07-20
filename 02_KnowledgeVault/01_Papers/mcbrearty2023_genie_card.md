---
title: "Earthquake Phase Association with Graph Neural Networks"
authors: [I.W. McBrearty, G.C. Beroza]
year: 2023
venue: "arXiv preprint"
task: [Phase Association, Earthquake Detection, Catalog Building]
method: [GENIE GNN, Two-Graph Architecture, Synthetic Training]
dataset: [Northern California seismic network, PhaseNet picks]
code_available: Not Checked
importance: high
reading_status: deep-read
tags: [genie, graph-neural-network, phase-association, northern-california, phasenet, synthetic-training]
created: 2026-07-18
---

# Basic Information / 基本信息

- **Title**: Earthquake Phase Association with Graph Neural Networks
- **Authors**: I.W. McBrearty, G.C. Beroza
- **Year**: 2023
- **Venue**: arXiv preprint
- **Task**: Earthquake phase association using graph neural networks
- **Method**: GENIE — GNN that simultaneously predicts source space-time localization and source-arrival association likelihoods using two graphs (station graph + source region graph)
- **Dataset**: Northern California seismic network, PhaseNet-generated picks
- **Code**: Not Checked

# Research Problem / 研究问题

Can graph neural networks effectively solve the phase association problem under high-rate ML picker conditions, where traditional methods struggle with time-entangled arrivals from overlapping small earthquakes?

# Main Contribution / 主要贡献

Developed GENIE, a GNN associator that handles arbitrary network geometry and time-varying stations. Trained on synthetic data, tested on NC seismic network. Successfully re-detected ~96% of USGS M>1 events and detected ~4.2x more events in a 100-day interval. New events concentrated near active faults and quarries.

# Method Overview / 方法概述

1. **Two-graph architecture**: Station graph (represents monitoring network) + Source graph (represents spatial source region)
2. **Joint learning**: GNN learns relationships from combined representation
3. **Simultaneous prediction**: Source localization + source-arrival association likelihoods
4. **Synthetic training**: Method trained on synthetic data for generalization
5. **Real data testing**: Applied to NC network with PhaseNet picks

# Dataset and Evaluation / 数据集与评估

- **Northern California seismic network**: ~500 random days (2000-2022)
- **100-day continuous interval** (2017-2018): Full processing test
- **Comparison**: USGS catalog (M>1 events)
- **Performance**: 96% USGS re-detection rate, 4.2x more events detected

# Why This Paper Matters / 为什么关注这篇论文

Phase association is a critical bottleneck in ML-based seismic cataloging. GENIE addresses this with a novel GNN approach that scales to high-rate picks from ML detectors. The two-graph architecture is elegant and generalizable.

# Limitations / 局限性

- Published as arXiv preprint — not yet peer-reviewed
- Synthetic training may not capture all real-world complexities
- Tested only on NC network — generalizability to other regions unverified
- PhaseNet picks used as input — quality depends on picker performance

# Reproducibility Status / 可复现性状态

## Code Availability

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

## Data Status / 数据可用性

- [x] **Public dataset available** — NC seismic data is public
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [x] Medium [ ] Low

**Reason**: Synthetic training data generation details needed. NC data is public. PhaseNet is available.

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason**: Novel GNN approach to phase association. High relevance to building complete seismic catalogs from ML picker output.

# Related Knowledge / 相关知识链接

- Task: [[Phase Association]], [[Earthquake Detection]]
- Method: [[GENIE]], [[Graph Neural Network]], [[Two-Graph Architecture]]
- Dataset: [[Northern California Seismic Network]]
