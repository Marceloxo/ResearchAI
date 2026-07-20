---
method_name: "PLAN"
category: "Multi-task Multi-station GNN"
application: ["Phase Picking", "Phase Association", "Earthquake Location"]
related_tasks: ["Seismic Phase Picking", "Phase Association", "Earthquake Location"]
tags: [plan, graph-neural-network, multi-task-learning, multi-station, physics-informed, ridgecrest, japan-hinet]
created: 2026-07-19
---

# Definition / 定义

PLAN is the first all-in-one system that simultaneously performs phase picking, phase association, and earthquake location using a multi-station GNN with physics-informed alignment. It outperforms PhaseNet, EQTransformer, and Aggregated-GNN on both Ridgecrest and Japan Hi-net datasets.

# Core Idea / 核心思想

Earthquake monitoring involves three interdependent tasks that are traditionally processed sequentially: phase picking → association → location. Each stage's errors propagate to the next. PLAN eliminates this cascade by processing all three tasks jointly with inter-task and inter-station constraints. The key innovations are: (1) a dynamic graph layer (TransformGConv) that adapts to variable station counts, (2) physics-informed alignment layers that embed domain knowledge (moveout curves) directly into the network via non-trainable PyTorch roll operations, and (3) multi-task joint optimization with separate loss functions for each sub-task.

# Architecture / Formulation / 架构/公式

## Overall Framework

Four interdependent modules processed jointly:

```
Multi-station 3-component waveforms + station coordinates
    ↓
[Module 1] Waveform Feature Extraction (shared CNN encoder-decoder)
    ↓
[Module 2] Earthquake Location (offset + depth prediction)
    ↓
[Module 3] Multi-station Association (physics-informed time-shift alignment)
    ↓
[Module 4] Phase Picking (multi-station P/S classification)
    ↓
Joint optimization with 3 regression losses
```

## TransformGConv (Core GNN Layer)

Graph neural network layer based on attention mechanism:
- Dynamically learns linking weights among stations during training
- Graph nodes are NOT fixed — adapts to varying station counts
- Superior to GCN, SAGE, GATv2 in ablation comparison

## Earthquake Location Module

Concatenates waveform features + geographic features (lon/lat/elevation via MLP):
- Uses multiple TransformGConv layers to aggregate across stations
- Predicts: (a) station-event offset, (b) event depth
- Triangulation from predicted offset + depth gives epicenter
- Key design: predicts offset/depth rather than direct hypocenter — more robust

## Multi-station Association Module

Bridges location and picking tasks:
- Uses predicted offsets and depth to compute time shifts for P and S waves
- **Non-trainable physical layer** (PyTorch roll function) shifts and aligns waveform features
- Multiple TransformGConv layers aggregate aligned features
- Another physical layer unshifts aggregated features back to original space
- Can be detached post-training to estimate S-P differential travel time

## Physics-informed Multi-station Phase Picking

- Takes aligned waveform features from association module
- Two convolutional layers produce P/S-wave picks at all stations simultaneously
- Multi-station picking leverages inter-station contextual information

## Loss Functions

```
L_picking-p, L_picking-s = MSE(predicted, Gaussian-target)
L_Delta_p = sum_i |CTime_p - (label_p_i + Delta_t_p_i)|
L_Delta_s = sum_i |CTime_s - (label_s_i + Delta_t_s_i)|
L_offset, L_depth = MSE(predicted, catalog reference)
L_total = L_picking-p + L_picking-s + L_Delta_p + L_Delta_s + L_offset + L_depth
```

All lambda weights = 1 (equal contribution).

## Evaluation Metrics

mPrecision, mRecall, mF1 averaged over thresholds 11-50 (0.11s to 0.50s):
```
mPrecision = (Precision@11 + ... + Precision@50) / 40
```

## Advantages / 优势

- **All-in-one**: Single model replaces the traditional 3-stage pipeline
- **Physics-informed**: Embeds domain knowledge (travel time moveout) as non-trainable layers
- **Variable station count**: Handles network changes natively
- **Multi-station picking**: Outperforms single-station baselines even in simplified configurations
- **Code available**: GitHub repository with source code
- **Well-documented hyperparameters**: LR, batch size, epochs all specified

## Limitations / 局限性

- Tested on only two regions (Ridgecrest and Japan) — generalization to other tectonic settings unverified
- Training requires ~24h on A100 — inference efficiency not discussed
- No comparison with McBrearty & Beroza (2023) GENIE — a competing GNN-based associator
- Gaussian-shaped target function for labels may not generalize to all data qualities
- No uncertainty quantification on picks or location predictions
- Velocity model assumption (6 km/s P, 3.4 km/s S) used only for catalog generation

## Typical Applications / 典型应用

| Task | Description | Representative Work |
|---|---|---|
| Phase Picking | Multi-station P/S wave detection | Si et al. (2024) |
| Phase Association | Source-arrival assignment | Si et al. (2024) |
| Earthquake Location | Hypocenter prediction from multi-station data | Si et al. (2024) |

## Related Papers / 相关论文

- [[si2024_plan_allinone_note]] — Primary source paper

## Related Methods / 相关方法

- [[GENIE]] — Competing GNN-based phase association method
- [[Multi-task Learning]] — Training paradigm used by PLAN
- [[PhaseNet]] — Single-station baseline for picking
- [[EQTransformer]] — Single-station baseline with attention
