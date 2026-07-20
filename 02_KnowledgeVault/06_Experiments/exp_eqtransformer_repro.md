---
experiment_id: "exp-eqtransformer-repro"
project: "eqtransformer_repro"
task: "Seismic Phase Picking"
dataset: "Northern California Seismic Network"
method: "EQTransformer"
date: 2026-07-20
status: planned
tags: [eqtransformer, reproducibility, baseline, transformer, seismic-phase-picking]
created: 2026-07-20
---

# Experiment Objective / 实验目标

Reproduce EQTransformer (mousavi2020) results as a Transformer-based baseline for seismic phase picking. Verify the claimed performance and compare with PhaseNet in terms of accuracy, speed, and memory footprint on RTX 4070.

# Hypothesis / 假设

EQTransformer's 56-layer architecture with attention is heavier than PhaseNet. Expect it to still fit on RTX 4070 (12GB VRAM) but with smaller batch size. The hierarchical attention (global + local) should outperform PhaseNet on low-SNR picks.

# Configuration / 实验配置

- **Model / 模型**: [[EQTransformer]]
- **Dataset / 数据集**: [[Northern California Seismic Network]]
- **Task / 任务**: [[Seismic Phase Picking]]
- **Hyperparameters / 超参数**:
  - Learning rate: (not specified — need to check code)
  - Batch size: (not specified — may need reduction for RTX 4070)
  - Epochs: (not specified — need to check code)
  - Optimizer: Adam
  - Loss function: Binary cross-entropy
- **Hardware / 硬件**: RTX 4070 12GB, Ubuntu 24.04
- **Code Location / 代码位置**: `https://github.com/smousavi05/EQTransformer`

# Results / 实验结果

## Quantitative Results / 定量结果

| Metric | Expected (paper) | Achieved |
|--------|-----------------|----------|
| Detection P Recall | 99.98% | — |
| Detection P Precision | 99.99% | — |
| Picking MAE (P) | 0.02s | — |
| Picking MAE (S) | 0.04s | — |

## Qualitative Results / 定性结果

<!-- Pending execution -->

# Comparison / 对比分析

| Method | P Recall | P Precision | Params | Inference Speed | Notes |
|--------|---------|------------|--------|----------------|-------|
| [[PhaseNet]] | 99.3% | 99.5% | 0.2M | Fast | Lightweight CNN |
| [[EQTransformer]] | 99.98% | 99.99% | ~2M | Moderate | 56-layer + attention |
| This experiment | — | — | — | — | RTX 4070 baseline |

# Ablation / 消融实验

| Variant | Detection F1 | Picking MAE | Notes |
|---------|------------|------------|-------|
| Full EQTransformer | — | — | Hierarchical attention |
| w/o attention | — | — | Test attention contribution |
| Smaller encoder | — | — | RTX 4070-optimized variant |

# Analysis / 分析

<!-- Pending execution -->

# Conclusion / 结论

<!-- Pending execution -->

# Related / 相关链接

- Method: [[EQTransformer]], [[Transformer]], [[Attention Mechanism]]
- Dataset: [[Northern California Seismic Network]]
- Task: [[Seismic Phase Picking]]
- Idea: [[idea_transfer_learning_seismic]]