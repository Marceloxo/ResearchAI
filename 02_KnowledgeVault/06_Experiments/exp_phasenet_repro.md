---
experiment_id: "exp-phasenet-repro"
project: "phasenet_repro"
task: "Seismic Phase Picking"
dataset: "Northern California Seismic Network"
method: "PhaseNet"
date: 2026-07-20
status: planned
tags: [phasenet, reproducibility, baseline, seismic-phase-picking]
created: 2026-07-20
---

# Experiment Objective / 实验目标

Reproduce PhaseNet (zhu2018) results on the NCEDC dataset as a baseline for seismic phase picking research. Verify the claimed performance (P-wave: 99.3% recall, 99.5% precision; S-wave: 98.6% recall, 99.1% precision) on RTX 4070 hardware.

# Hypothesis / 假设

PhaseNet's 1D CNN architecture is lightweight enough to run comfortably on RTX 4070 (12GB VRAM). The official code is available and should reproduce the reported metrics within ±1% given the same train/val/test split.

# Configuration / 实验配置

- **Model / 模型**: [[PhaseNet]]
- **Dataset / 数据集**: [[Northern California Seismic Network]]
- **Task / 任务**: [[Seismic Phase Picking]]
- **Hyperparameters / 超参数**:
  - Learning rate: (not specified in paper — need to determine from code)
  - Batch size: (not specified in paper — need to determine)
  - Epochs: 20
  - Optimizer: Adam
  - Loss function: Cross-entropy
- **Hardware / 硬件**: RTX 4070 12GB, Ubuntu 24.04
- **Code Location / 代码位置**: `https://github.com/weiqiangzhu/PhaseNet`

# Results / 实验结果

## Quantitative Results / 定量结果

| Metric | Expected (paper) | Achieved |
|--------|-----------------|----------|
| P-wave Recall | 99.3% | — |
| P-wave Precision | 99.5% | — |
| S-wave Recall | 98.6% | — |
| S-wave Precision | 99.1% | — |

## Qualitative Results / 定性结果

<!-- Pending execution -->

# Comparison / 对比分析

| Method | P Recall | P Precision | S Recall | S Precision | Notes |
|--------|---------|------------|---------|------------|-------|
| [[PhaseNet]] (paper) | 99.3% | 99.5% | 98.6% | 99.1% | Original |
| PhaseNet (repro) | — | — | — | — | This experiment |

# Ablation / 消融实验

| Variant | P Recall | P Precision | Notes |
|---------|---------|------------|-------|
| Full PhaseNet | — | — | 4-layer 1D U-Net |
| w/o skip connections | — | — | Test skip connection importance |
| Smaller (2 layers) | — | — | RTX 4070 lightweight variant |

# Analysis / 分析

<!-- Pending execution -->

# Conclusion / 结论

<!-- Pending execution -->

# Related / 相关链接

- Method: [[PhaseNet]]
- Dataset: [[Northern California Seismic Network]]
- Task: [[Seismic Phase Picking]]
- Idea: [[idea_transfer_learning_seismic]]