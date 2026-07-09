---
title: "Rapid Characterization of the July 2019 Ridgecrest, California Earthquake Sequence from Raw Seismic Data using Machine Learning Phase Picker"
authors: [Liu, Zhang, Zhu, Ellsworth, Li]
year: 2020
venue: "Geophysical Research Letters"
task: [Earthquake Catalog Building, Phase Picking, Seismicity Characterization]
methods: [PhaseNet, REAL, VELEST, hypoDD]
datasets: [Ridgecrest 2019, SCSN]
metrics: [Event count, location precision, fault structure resolution]
code: "N/A — uses existing PhaseNet (Zhu & Beroza 2019)"
importance: medium-high
status: done
paper_type: research_article
tags: [phasenet, ridgecrest, earthquake-catalog, machine-learning, liu-zhang]
created: 2026-07-09
---

# Paper Type / 论文类型

Type: research_article

# One Sentence Summary / 一句话总结

Liu et al. (2020) 使用PhaseNet从Ridgecrest 2019地震序列原始连续数据自动构建了包含15,445个事件的高精度目录，比SCSN常规目录多2倍，清晰揭示了多条隐伏断层结构。

# Research Background / 研究背景

2019年7月加州Ridgecrest发生了MW 6.4和MW 7.1双主震序列，是研究地震触发和断层相互作用的理想实验室。传统地震目录构建依赖人工拾波或STA/LTA自动拾波，难以应对高频率地震事件。PhaseNet证明了ML拾波器在自然地震数据上的优越性，但其在实际地震序列（特别是高发生率序列）中的泛化能力和实用性尚未系统评估。

# Problem Definition / 问题定义

- **Input / 输入**: Ridgecrest区域45个台站的连续波形数据（2019.7.4-7.9）
- **Output / 输出**: 高精度地震目录（位置、时间、震级）+ 断层结构刻画

# Motivation / 研究动机

1. 传统方法在高发生率地震序列中容易遗漏小事件
2. PhaseNet在训练数据（北加州）之外的泛化性未知
3. 需要评估ML拾波器在实际地震应急响应中的实用性
4. 高精度目录有助于理解地震触发机制和断层结构

# Main Contributions / 主要贡献

1. **构建了Ridgecrest 2019序列的ML地震目录** — 15,445个hypoDD定位事件，比SCSN常规目录多2倍
2. **揭示了多条隐伏断层结构** — 包括与地表破裂面一致的NE向断层和NW向分支断层
3. **展示了PhaseNet的跨区泛化能力** — 从北加州训练→南加州Ridgecrest应用，性能保持良好
4. **验证了sequential workflow的实用性** — PhaseNet→REAL→VELEST→hypoDD全流程可在数小时内完成6天数据处理

# Method / 方法

## Overall Framework / 整体框架

Sequential earthquake catalog building workflow:

```
Continuous Waveforms → PhaseNet (P/S picking) → REAL (association/location) → VELEST (absolute relocation) → hypoDD (relative relocation)
```

## Key Modules / 关键模块

### Module 1: PhaseNet Picking

- **Input**: 3-component waveforms (vertical or combined)
- **Threshold**: Empirically set to 0.5
- **Training data**: NCEDC (Northern California), 779K waveforms
- **Transfer**: Zero-shot application to Ridgecrest (different region, different tectonic setting)

### Module 2: REAL Association

- **Method**: Rapid Earthquake Association and Location (Zhang et al. 2019)
- **Grid search**: 0.4° × 0.4° horizontal (1.7km grid), surface to 20km depth (2km grid)
- **Thresholds**: ≥5 P picks, ≥13 total P+S picks
- **Stations**: Epicentral distance <100km

### Module 3: VELEST Absolute Relocation

- **Velocity model**: Coso regional 1D model (Feng & Lees, 1998)
- **Iteration**: 1,633 high-quality events (≥30 picks, r>0.8) used to update velocity model
- **Station corrections**: Included in velocity model update

### Module 4: hypoDD Relative Relocation

- **Strategies**: (1) Stations <80km only, (2) Picks fitting major travel time trend, (3) Picks with probability >0.7
- **Resolution**: Sub-kilometer fault structure definition

## Mathematical Formulation / 数学表述

> 本文未提出新数学方法，而是应用现有工具链。PhaseNet使用softmax概率输出，REAL使用网格搜索最大化拾波数量。

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| Ridgecrest 2019 | 45 stations, 120km radius | Continuous 3C waveforms | MW 6.4 (Jul 4) + MW 7.1 (Jul 6) sequence |
| SCSN routine catalog | 7,425 events | Picked phases | Southern California Seismic Network |
| Coso 1D velocity model | Regional | P/S velocity | Feng & Lees (1998), used as initial model |

# Experimental Setup / 实验设置

- **Baseline**: SCSN routine catalog, routine CC (cross-correlation) catalog
- **Evaluation metrics**: Event count, location precision, fault structure definition quality
- **Comparison**: REAL catalog vs VELEST catalog vs hypoDD catalog vs SCSN vs routine CC
- **Processing time**: Minutes to hours on HPC cluster (vs. days for manual)

# Results / 实验结果

| Catalog | Events | Resolution | Notes |
|---|---|---|---|
| SCSN routine | 7,743 | Low | Misses small events |
| REAL (PhaseNet) | 16,563 | Medium | Includes strict filtering |
| VELEST relocated | 16,112 | Medium-High | Velocity model updated |
| hypoDD relocated | 15,445 | High | Best resolution |
| Routine CC | ~8,000 | High | Requires template events |

**Key findings:**
- hypoDD catalog has **2× more events** than SCSN routine catalog
- Fault structures defined by hypoDD align well with surveyed surface ruptures
- Multiple near-orthogonal buried faults revealed that were invisible in routine catalogs
- Triggered earthquake clusters identified at Coulomb stress increase regions

# Ablation Study / 消融实验

- **Threshold sensitivity**: Strict criteria (≥13 picks, ≤200° gap) reduce catalog completeness by 12% but improve reliability
- **Relocation method**: hypoDD provides better resolution than VELEST alone (sub-km vs km-scale)
- **PhaseNet threshold**: Empirical 0.5 threshold — sensitivity analysis in supplementary materials
- **Velocity model update**: Iterative update using high-quality events improves location accuracy

# Limitation / 局限性

> 论文自己承认的局限 + 你看到的局限

**Author-admitted:**
- Template matching could increase event count further but requires computational resources
- Waveform cross-correlation can improve resolution but depends on routine catalog content
- Resolution of foreshock sequence structure falls beyond PhaseNet arrival time measurement precision

**Agent-identified:**
- **No ablation on PhaseNet threshold** — the 0.5 threshold was "empirically set" without systematic study
- **No comparison with EQTransformer** — the newer model (Mousavi et al. 2020) was published in the same issue but not compared
- **Limited generalization testing** — only tested on Ridgecrest; performance on other sequences unknown
- **No uncertainty quantification** — PhaseNet provides probabilities but no confidence intervals on locations
- **Workflow is sequential, not end-to-end** — errors propagate through stages; no joint optimization
- **Real-time claim not fully validated** — "minutes/hours" depends on HPC availability

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **Sequential workflow for catalog building**: PhaseNet→association→relocation pipeline is modular and can be adapted to seismic image processing (detection→segmentation→refinement).
2. **Cross-region generalization**: PhaseNet trained on NCEDC works on Ridgecrest (different tectonic setting) — suggests pre-trained models can generalize across domains with minimal adaptation.
3. **Strict filtering improves reliability**: The 12% event loss from strict criteria is acceptable for high-quality catalog building. Similar trade-off exists in image segmentation (precision vs recall).
4. **Iterative velocity model update**: Using high-quality events to refine the model, then relocating all events — this iterative refinement concept applies to seismic image processing (initial model → refine → reprocess).

## Potential Improvements / 潜在改进方向

1. **End-to-end joint optimization**: Instead of sequential pipeline, train a unified model for detection+association+location.
2. **Uncertainty propagation**: Track PhaseNet picking uncertainty through the relocation workflow to produce uncertainty-aware catalogs.
3. **Comparison with EQTransformer**: The newer model with attention mechanism was available but not compared — could show whether attention helps in high-rate sequences.
4. **Real-time deployment testing**: Deploy on edge devices (not HPC) to validate the "near real-time" claim.
5. **Application to seismic image segmentation**: The sequential refinement concept (rough→fine) could apply to coarse segmentation→boundary refinement pipelines.

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

> Paper Note inherits basic code status from Literature Card, then adds deep analysis.

- **Code Status**: [ ] Confirmed Available [ ] Not Found Yet [x] Confirmed Missing [ ] Not Checked
- **Official URL**: N/A — this paper applies existing tools, does not introduce new code
- **Framework**: N/A
- **Checkpoint / Pre-trained Weights**: [ ] Available [ ] Not mentioned [ ] Not applicable
- **Last Repository Update**: N/A
- **Code Quality Indicators**: N/A

## Missing Reproduction Components / 缺失的复现组件

> 即使代码公开，也可能缺少某些关键组件导致无法复现。逐项评估。

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [ ] Yes [x] No [ ] Partial | N/A — paper applies existing tools | PhaseNet code available separately |
| Dataset Access | [ ] Public [x] Restricted [ ] Private | IRIS/SCEC (registration required) | Southern California data requires IRIS account |
| Pre-trained Checkpoint | [ ] Yes [x] No [ ] N/A | PhaseNet weights not included in this paper | Users must obtain PhaseNet separately |
| Preprocessing Scripts | [ ] Yes [x] Partially [ ] Not mentioned | REAL algorithm details in supplementary | Some details in supplementary materials |
| Hyperparameters | [x] Fully Listed [ ] Partially [ ] Missing | Grid size, thresholds, velocity model | Most parameters well documented |
| Environment Specs | [ ] requirements.txt [ ] Docker [x] Not specified | HPC cluster mentioned | No specific software versions |
| Random Seeds | [ ] Specified [x] Not specified | Not mentioned | Deterministic workflow, seeds less critical |
| Train/Val/Test Split | [x] Defined [ ] Undefined | N/A — this is an application paper | No ML training in this paper |
| Data Augmentation | [ ] Described [x] Vaguely [ ] Not described | N/A | No data augmentation used |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [x] Easy [ ] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: <!-- 1-2 weeks (mostly data acquisition) -->
- **Hardware Requirements**: <!-- HPC cluster for PhaseNet inference -->
- **Key Barriers**: Data access (IRIS registration), PhaseNet model weights not included
- **Workaround Options**: Use publicly available PhaseNet implementation; apply for IRIS data access
- **RTX 4070 Compatibility**: [x] Runs fine [ ] May struggle [ ] Won't fit in VRAM
- **Gap Between Code Existence and Reproducibility**: The paper itself is an **application study**, not a method paper. Reproduction requires: (1) PhaseNet model (available separately), (2) Ridgecrest waveform data (restricted via IRIS), (3) REAL/VELEST/hypoDD software (available). The main barrier is **data access**, not code availability.

# Related Notes / 相关笔记

- Method: [[PhaseNet]], [[CNN]]
- Task: [[Seismic Phase Picking]]
- Dataset: [[EGS Collab SURF]]
