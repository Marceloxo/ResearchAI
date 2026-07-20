---
title: "An all-in-one seismic phase picking, location, and association network for multi-task multi-station earthquake monitoring"
authors: [Xu Si, Xinming Wu, Zefeng Li, Shenghou Wang, Jun Zhu]
year: 2024
venue: "Communications Earth & Environment"
task: [Phase Picking, Phase Association, Earthquake Location]
methods: [PLAN GNN, TransformGConv, Multi-task Learning, Multi-station Picking, Physics-informed Layers]
datasets: [Ridgecrest SCSN, Japan Hi-net]
metrics: [mPrecision, mRecall, mF1, offset residual, depth residual]
code: "https://github.com/sixu0/PLAN4Earthquake_Monitoring"
importance: high
status: completed
paper_type: research_article
tags: [phase-picking, phase-association, earthquake-location, plan, graph-neural-network, transformgconv, multi-task-learning, multi-station, ridgecrest, japan-hinet]
created: 2026-07-19
---

# Paper Type / 論文類型

Type: research_article

# One Sentence Summary / 一句話總結

Proposes PLAN, a multi-task multi-station GNN that simultaneously performs phase picking, phase association, and earthquake location using TransformGConv layers with physics-informed alignment, achieving superior performance over PhaseNet, EQTransformer, and Aggregated-GNN on Ridgecrest and Japan datasets.

# Research Background / 研究背景

Earthquake monitoring involves three interdependent tasks: phase picking, phase association, and event location. Deep learning has been applied to each task individually, but existing methods process them separately and ignore geographic relationships among stations. Most phase-picking methods operate station-by-station, losing the inter-station contextual information that could improve accuracy.

Graph neural networks have shown promise for handling irregular station geometries in association and location tasks, but no existing method integrates all three tasks simultaneously with inter-task and inter-station constraints.

# Problem Definition / 問題定義

- **Input / 輸入**: Multi-station three-component seismic waveforms + station geographic coordinates (longitude, latitude, elevation)
- **Output / 輸出**: (1) P/S phase picks at all stations, (2) source-arrival association via time-shift estimation, (3) event depth and epicentral offset predictions for triangulation

# Motivation / 研究動機

1. **Inter-task dependency**: Phase picking accuracy affects association and location; association and location impose constraints back on picking.
2. **Inter-station relationships**: Geographic proximity and waveform similarity across stations provide additional signal for multi-station picking.
3. **Separate processing inefficiency**: Current pipelines run picking → association → location sequentially, accumulating errors at each stage.
4. **Irregular station geometry**: GNNs naturally handle variable station counts and non-uniform distributions.

# Main Contributions / 主要貢獻

1. **First all-in-one system**: PLAN is the first method to simultaneously perform phase picking, association, and location with multi-station data and inter-task constraints.
2. **Physics-informed architecture**: Multi-station association module implements a non-trainable physical layer (PyTorch roll) that aligns waveform features using predicted time shifts, mimicking array seismology "shift-and-stack."
3. **Superior performance**: Outperforms PhaseNet, EQTransformer (picking), and Aggregated-GNN (location) on both Ridgecrest and Japan datasets across mPrecision, mRecall, and mF1 metrics.
4. **Flexible station count**: Trained network handles variable numbers of stations per event, adapting to real-world network changes.

# Method / 方法

## Overall Framework / 整體框架

PLAN consists of four interdependent modules processed jointly:

1. **Waveform Feature Extraction**: Shared encoder-decoder CNN extracts features from multi-station seismic data
2. **Earthquake Location**: Combines waveform features + station geographic features to predict event depth and station-event offset
3. **Multi-station Association**: Uses predicted offsets/depth to estimate time shifts for aligning multi-station waveform features
4. **Phase Picking**: Aggregates aligned features via TransformGConv, then uses a physical unshift layer + conv layers for P/S picks

All four modules are optimized simultaneously with three regression loss functions (one per task).

## Key Modules / 關鍵模塊

### Module 1: TransformGConv Backbone

- Graph neural network layer based on attention mechanism
- Dynamically learns linking weights among stations during training
- Graph nodes are NOT fixed — adapts to varying station counts
- Superior to GCN, SAGE, GATv2 in ablation comparison

### Module 2: Earthquake Location Module

- Concatenates waveform features (from CNN encoder-decoder) + geographic features (normalized lon/lat/elevation via MLP)
- Uses multiple TransformGConv layers to aggregate features across stations
- Predicts: (a) station-event offset, (b) event depth
- Triangulation from predicted offset + depth gives epicenter location
- Key design: predicts offset/depth rather than direct hypocenter — more robust

### Module 3: Multi-station Association Module

- Bridges location and picking tasks
- Uses predicted offsets and depth to compute time shifts for P and S waves
- Non-trainable physical layer (PyTorch roll function) shifts and aligns waveform features
- Multiple TransformGConv layers aggregate aligned features
- Another physical layer unshifts aggregated features back to original space
- Can be detached post-training to estimate S-P differential travel time

### Module 4: Physics-informed Multi-station Phase Picking

- Takes aligned waveform features from association module
- Two convolutional layers produce P/S-wave picks at all stations simultaneously
- Multi-station picking leverages inter-station contextual information
- Even simplified single-station versions outperform baseline single-station methods

## Mathematical Formulation / 數學表述

### Loss Functions

Phase picking loss (MSE for multi-task compatibility):
```
L_picking-p, L_picking-s = MSE(predicted, Gaussian-target)
```

Association loss (absolute difference):
```
L_Delta_p = sum_i |CTime_p - (label_p_i + Delta_t_p_i)|
L_Delta_s = sum_i |CTime_s - (label_s_i + Delta_t_s_i)|
```

Location loss (MSE):
```
L_offset, L_depth = MSE(predicted, catalog reference)
```

Total loss:
```
L_total = L_picking-p + L_picking-s + L_Delta_p + L_Delta_s + L_offset + L_depth
(lambda_1 = lambda_2 = lambda_3 = 1)
```

### Evaluation Metrics (mPrecision, mRecall, mF1)

Multi-threshold metrics averaging Precision/Recall/F1 at thresholds 11-50 (0.11s to 0.50s):
```
mPrecision = (Precision@11 + ... + Precision@50) / 40
mRecall = (Recall@11 + ... + Recall@50) / 40
mF1 = (F1@11 + ... + F1@50) / 40
```

# Dataset / 數據集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| Ridgecrest SCSN | 71,000+ M>-0.5 events (2014-2021), 16 CALNET stations | 3-component velocity | Southern California; epicentral distance <80 km; training/validation/test split 85/5/10%; 30.72s window |
| Japan Hi-net | 35,000+ M>2 events (2011), NIED Hi-net | 3-component velocity | Tohoku sequence; dense network; training/validation/test split 85/5/10%; 61.44s window; 100 Hz sampling |

# Experimental Setup / 實驗設置

**Baselines**:
1. PhaseNet (single-station CNN picker)
2. EQTransformer (single-station picker with attention)
3. Aggregated-GNN (location baseline)

**Training details**:
- Optimizer: Adam, initial LR=0.001, decay=0.9 per 100 epochs
- Batch size: 16
- Epochs: 2000
- Random sampling: 2048 events per epoch (not full training set)
- Hardware: ~24 hours on NVIDIA Tesla A100 GPU

**Evaluation**: Retrained all baselines on same training set, evaluated on common test set for fair comparison.

# Results / 實驗結果

### Ridgecrest Region

- **P-wave picking**: PLAN residual distribution more concentrated than PhaseNet and EQTransformer
- **S-wave picking**: PLAN significantly better than EQTransformer; minor improvement over PhaseNet
- **Offset prediction**: PLAN avg error 1.09 km (SD 1.41 km), beating Aggregated-GNN
- **Depth prediction**: PLAN outperforms Aggregated-GNN across all GNN variants

### Japan Region

- **P-wave picking**: PLAN mRecall=95.14, mF1=95.46 — best recall and F1
- **S-wave picking**: PLAN mRecall=85.09, mF1=86.72 — best recall and F1
- **EQTransformer** had slightly higher mPrecision but lower overall F1
- **Offset prediction**: PLAN notably more accurate than Aggregated-GNN
- **Depth prediction**: PLAN narrower distribution but systematic shift; GATv2 variant had lowest depth error

### Ablation: GNN Layer Comparison

Replacing TransformGConv with alternatives (Supplementary Fig. 1):
- GCN, SAGE, GATv2 all underperformed TransformGConv
- SAGE-based PLAN still beat single-station baselines, confirming multi-station value

# Ablation Study / 消融實驗

1. **TransformGConv vs. GCN/SAGE/GATv2**: TransformGConv superior across all metrics
2. **Multi-station vs. Single-station**: Even simplified SAGE-based PLAN outperforms PhaseNet and EQTransformer in S-wave mF1, confirming multi-station picking benefit
3. **Region transfer**: Models retrained on Japan data show PLAN's advantage increases in Japan vs. Ridgecrest

# Limitation / 侷限性

### Author-Admitted Limitations

- Tested on only two regions (Ridgecrest and Japan) — generalization to other tectonic settings unverified
- mRecall advantage comes at slight mPrecision cost (more false positives)
- Depth estimation in Japan shows systematic shift — GATv2 variant performed better, suggesting architecture sensitivity

### Agent-Identified Limitations

- No comparison with McBrearty & Beroza (2023) GENIE — a competing GNN-based associator
- No comparison with end-to-end methods (Zhu et al., 2022; Munchmeyer et al., 2021)
- Training requires 24h on A100 — inference efficiency not discussed
- No analysis of continuous data processing latency — operational deployment feasibility unclear
- Gaussian-shaped target function for labels may not generalize to all data qualities
- No uncertainty quantification on picks or location predictions
- Velocity model assumption (6 km/s P, 3.4 km/s S) used only for catalog generation, not network training

# My Analysis / 我的分析

## Transferable Ideas / 可遷移思想

1. **Physics-informed alignment layers**: The PyTorch roll-based time-shift alignment is a clean way to embed domain knowledge (moveout curves) directly into the network — applicable to any multi-station seismic task.
2. **Predict offset + depth instead of direct location**: This indirect prediction approach is more robust than direct hypocenter regression, as it decomposes the problem into physically interpretable quantities.
3. **Multi-task joint training with separate losses**: The three-loss approach (picking + association + location) with equal weighting is simple but effective; could be extended to weighted losses for imbalanced tasks.
4. **Variable station count handling**: GNN nodes not being fixed allows the model to adapt to network changes — directly applicable to real-world monitoring where stations go offline.
5. **Shift-and-stack detection strategy**: The post-processing pipeline (pick → shift-and-stack → station filtering → catalog generation) provides a principled approach for converting continuous waveform processing into earthquake catalogs.

## Potential Improvements / 潛在改進方向

1. **Cross-region transfer test**: Apply Ridgecrest-trained PLAN to other regions (e.g., Iceland, Japan-only to California) to test generalization.
2. **Weighted loss functions**: Experiment with different lambda values to balance the three tasks, especially if one task dominates gradient updates.
3. **Uncertainty estimation**: Add Bayesian layers or ensemble methods for confidence estimates on picks and locations.
4. **Real-time inference benchmark**: Measure inference latency for continuous waveform processing to assess operational viability.
5. **Comparison with GENIE**: Direct benchmark against McBrearty & Beroza (2023) on shared data.
6. **Integration with matched filtering**: Combine PLAN picks with template-based detection for improved sensitivity.

# Reproducibility Analysis / 復現性分析

## Official Implementation Verification / 官方實現驗證

> Distinguish "code exists" from "paper is reproducible."

**Code Status**:
- [x] **Confirmed Available** — paper explicitly provides GitHub URL: https://github.com/sixu0/PLAN4Earthquake_Monitoring
- [ ] Confirmed Missing
- [ ] Not Found Yet
- [ ] Not Checked

**Evidence Location**: Section "Code availability" states source code is openly available with GitHub link

**Repository URL**: https://github.com/sixu0/PLAN4Earthquake_Monitoring

**Framework**: PyTorch (explicitly mentioned: "implemented with the Pytorch roll function")

**Checkpoint / Pre-trained Weights**: Not mentioned in full.md

**Last Repository Update**: Unknown — requires manual verification

**Code Quality Indicators**: Unknown — requires manual verification

**Verification Method**: Paper text confirmation of open-source code with URL

## Missing Reproduction Components / 缺失的復現組件

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [x] Yes [ ] No [ ] Not Found Yet | https://github.com/sixu0/PLAN4Earthquake_Monitoring | URL confirmed in paper |
| Dataset Access | [x] Public [ ] Restricted [ ] Private | SCSN (free), Hi-net (registration required) | Ridgecrest data freely available |
| Pre-trained Checkpoint | [ ] Yes [ ] No [x] Not mentioned | | |
| Preprocessing Scripts | [ ] Yes [ ] No [x] Not mentioned | Paper describes normalization procedure | |
| Hyperparameters | [x] Fully Listed [ ] Partially [ ] Missing | LR=0.001, batch=16, epochs=2000, decay=0.9/100ep, 2048 events/epoch | Well-documented |
| Environment Specs | [ ] requirements.txt [ ] Docker [x] Not specified | PyTorch mentioned; CUDA version not specified | |
| Random Seeds | [ ] Specified [x] Not specified | Not found in text | |
| Train/Val/Test Split | [x] Defined [ ] Undefined | 85%/5%/10% random split | |
| Data Augmentation | [x] Described [ ] Vaguely [ ] Not described | Gaussian target function, normalization | |

## Reproduction Difficulty Assessment / 復現難度評估

- **Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: 2-3 weeks for a researcher familiar with PyTorch and GNNs (PyG/DGL)
- **Hardware Requirements**: Training requires ~24h on A100; RTX 4070 feasible for inference and lighter training
- **Key Barriers**: Hi-net data requires registration; CUDA/library version compatibility
- **Workaround Options**: Use Ridgecrest data only (freely available); implement TransformGConv from scratch if PyG version unavailable

## Reproducibility vs. Code Availability

> **Important distinction**: Code existing ≠ paper is reproducible.

- **Code Exists**: [x] Yes — GitHub URL provided and confirmed
- **Paper Actually Reproducible**: [x] Yes [ ] Partially [ ] No
- **Gap Between Code Existence and Reproducibility**: Code is open source, hyperparameters are well-documented, Ridgecrest data is freely available. Main barrier is Hi-net registration. RTX 4070 can handle inference; training may require more VRAM for full dataset.

# Related Notes / 相關筆記

- Method: [[PLAN]], [[TransformGConv]], [[Graph Neural Network]], [[Multi-task Learning]]
- Task: [[Phase Picking]], [[Phase Association]], [[Earthquake Location]]
- Dataset: [[Southern California Seismic Network]], [[Japan Hi-net]]
- Related: [[PhaseNet]], [[EQTransformer]], [[GENIE]], [[Aggregated-GNN]]
- Authors: [[Si Xu]], [[Wu Xinming]]
