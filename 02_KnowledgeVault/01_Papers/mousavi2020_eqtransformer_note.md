---
title: "Earthquake transformer: an attentive deep-learning model for simultaneous earthquake detection and phase picking"
authors: [Mousavi, Ellsworth, Zhu, Chuang, Beroza]
year: 2020
venue: "Nature Communications"
task: [Earthquake Detection, Seismic Phase Picking]
methods: [EQTransformer, Attention, LSTM, CNN, Residual, NiN]
datasets: [STEAD, HiNet]
metrics: [Precision, Recall, F1 Score, Mean Error, Std Error]
code: "https://github.com/smousavi05/EQTransformer"
importance: high
status: done
paper_type: research_article
tags: [eqtransformer, attention, cnn, lstm, earthquake-detection, phase-picking, mousavi]
created: 2026-07-09
---

# Paper Type / 论文类型

Type: research_article

# One Sentence Summary / 一句话总结

EQTransformer用层次注意力机制（全局检测注意力+局部震相注意力）和56层非常深编码器，同时完成地震检测和P/S震相拾波，在STEAD测试集和日本鸟取连续数据上均超越PhaseNet等传统方法。

# Research Background / 研究背景

地震监测流水线包括检测（从噪声中识别地震信号）和拾波（测量P/S波到达时间）两个紧密相关但目标不同的任务。传统方法分别处理这两个任务，但实际分析流程中分析师首先看整个波形识别地震信号，然后聚焦各震相精确拾波。深度学习模型也应利用这种上下文信息的关联性。

# Problem Definition / 问题定义

- **Input / 输入**: 1分钟三分量波形 (100Hz采样, 6000样本点)
- **Output / 输出**: 三个概率序列 — 地震存在概率, P波到达概率, S波到达概率

# Motivation / 研究动机

1. 检测与拾波在物理上是相关的 — 检测是全局问题，拾波是局部问题
2. 单独处理两个任务浪费了上下文信息
3. 注意力机制已在NLP和CV中成功应用，但在地震信号中未充分探索
4. 需要一种能同时输出检测结果和精确到达时间的模型

# Main Contributions / 主要贡献

1. **提出EQTransformer架构** — 56层非常深编码器 + 三个独立解码器（检测/P/S），通过层次注意力机制共享信息
2. **层次注意力设计** — 全局注意力在编码器末尾聚焦地震信号，局部注意力在拾波解码器开头聚焦震相特征
3. **不确定性估计** — 使用MC Dropout近似贝叶斯推断，提供预测置信度
4. **大规模验证** — 在STEAD测试集（113K样本）和日本鸟取连续数据上验证，超越PhaseNet, GPD, STA/LTA等基线

# Method / 方法

## Overall Framework / 整体框架

EQTransformer = 多任务注意力网络

```
Input (6000×3) → Down-sampling → Very Deep Encoder (ResCNN + BiLSTM + NiN + Global Attention) → 3 Decoders
                                                                        ├── Detection Decoder
                                                                        ├── P-phase Decoder (Local Attention)
                                                                        └── S-phase Decoder (Local Attention)
```

## Key Modules / 关键模块

### Module 1: Very Deep Encoder (56 layers)

- **Down-sampling**: Conv + Max-pooling at front end (addresses O(n²·d) attention complexity for long sequences)
- **Residual Convolution Blocks**: Extends depth without degradation (He et al. 2016)
- **BiLSTM + NiN**: Bidirectional LSTM with Network-in-Network modules (Lin et al. 2013) — increases depth without more parameters
- **Global Attention**: Self-attention at encoder end — directs focus to earthquake signal portions
- **Activation**: ReLU throughout

### Module 2: Detection Decoder (Short Path)

- Direct connection from encoder output
- Naturally higher loss → easier learning (mimics analyst workflow: detect first, then pick)
- Outputs binary probability: earthquake present or not

### Module 3: P-phase Decoder (Local Attention)

- LSTM (16 units) at beginning for position information
- Local attention attends to small subset of sequence
- Sharpen focus on P-wave within earthquake waveform

### Module 4: S-phase Decoder (Local Attention)

- Same structure as P-phase decoder
- Local attention for S-wave focusing

### Module 5: Uncertainty Estimation (MC Dropout)

- Dropout (rate=0.1) applied at every layer during BOTH training and inference
- Multiple forward passes → Bernoulli distribution over weights
- Approximates Bayesian posterior over models

### Module 6: Data Augmentation

- Secondary earthquake signal in empty trace
- Random Gaussian noise addition
- Random event shifting within trace
- Array rotation
- Random gap insertion (zeroing short time spans)
- Random channel dropping (probability: 0.3, 0.5, 0.99, 0.2, 0.3)
- Half of each batch is augmented

## Mathematical Formulation / 数学表述

**Self-Attention** (single-head additive):

```
e_{t,t'} = σ(W₂ᵀ[tanh(W₁ᵀhₜ + W₁ᵀhₜ') + b₁] + b₂)
α_{t,t'} = exp(e_{t,t'}) / Σ_{t'} exp(e_{t,t'})
c_t = Σ_{t'} α_{t,t'} · h_{t'}
```

**Feed-forward layer**: FF(x) = max(0, xW₁+b₁)W₂+b₂

**Label format**: Triangular labeling — P/S probability = 1 at first arrival, linearly decreases to 0 within ±20 samples

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| STEAD | 1M earthquake + 300K noise | 3C waveforms, 1min, 100Hz | ~450K earthquakes, diverse geography, mostly M<2.5, <300km epicentral distance |
| HiNet (Japan) | 5 weeks continuous | 3C waveforms | 2000 Tottori earthquakes for real-world testing |

**Train/Val/Test Split**: 85%/5%/10% (random)

**Preprocessing**: Causal bandpass filter 1.0-15.0 Hz, standard deviation normalization

# Experimental Setup / 实验设置

- **Optimizer**: Adam with varying learning rates
- **Initialization**: Xavier normal for conv/LSTM, zero for biases
- **Dropout**: 0.1 (training + test)
- **Training time**: ~89 hours (4×Tesla-V100 GPUs, TensorFlow)
- **Convergence**: Stopped when validation loss didn't improve for 12 epochs
- **Batch size**: Not specified (half augmented)
- **Comparison models**: PhaseNet, GPD, PpkNet, Yews, DetNet, CRED, STA/LTA, Kurtosis, Filter-Picker, AIC

# Results / 实验结果

## Detection Performance (Table 1)

| Method | Precision | Recall | F1 Score |
|---|---|---|---|
| EQTransformer | ~1.0 | ~1.0 | Highest |
| CRED | Lower | Lower | Lower |
| STA/LTA | Lower | Lower | Lower |
| DetNet | Lower | Lower | Lower |
| Yews | Lower | Lower | Lower |

- EQTransformer: 1 false positive, 0 false negatives out of 113K test samples (threshold=0.5)

## Picking Performance (Tables 2-3)

- EQTransformer increases F1 scores for both P and S picks
- P-wave improvement more significant than S-wave
- Precision close to manual picks by human analysts
- Higher sensitivity detects more and smaller events

## Real-world Validation (Japan Tottori)

- Detected 2× more earthquakes using <1/3 of seismic stations
- Successfully handles multi-event windows
- Works on single-channel data and noisy channels

# Ablation Study / 消融实验

- **Data augmentation essential**: Without augmentations, model produces false positives at abrupt changes
- **Attention mechanism**: Deeper network + attention outperforms CRED (similar architecture but no attention)
- **Hierarchical attention**: Global attention at encoder → local attention at decoders mimics analyst workflow
- **Triangular labeling**: Lower loss and higher F-score than box or Gaussian labeling

# Limitation / 局限性

> 论文自己承认的局限 + 你看到的局限

**Author-admitted:**
- Training data from diverse geography but NOT Japan — generalization to Japan tested empirically
- Uncertainty estimation via MC Dropout is approximate, not full Bayesian
- Model needs 1-minute window (6000 samples) — may miss very short signals

**Agent-identified:**
- Training hyperparameters partially missing: exact learning rate schedule, batch size not specified
- No random seed reported
- No requirements.txt or environment.yml
- Performance on events with multiple close-spaced phases not thoroughly tested
- Single-head attention (not multi-head like original Transformer) — why?

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **Hierarchical attention for multi-scale problems**: Global attention for detection + local attention for picking. This is directly applicable to seismic image segmentation where we need global context (fault region) + local precision (pixel-level boundary).
2. **Multi-task learning**: Joint detection + picking shares encoder features. Similarly, segmentation + boundary detection could share features in seismic image tasks.
3. **MC Dropout for uncertainty**: Simple uncertainty quantification without changing architecture. Useful for identifying unreliable picks in our target tasks.
4. **Triangular labeling**: Soft labels with gradual transitions improve training. Analogous to soft masks in image segmentation.
5. **Very deep encoder with residual connections**: 56 layers with residual blocks — this depth is achievable with modern architectures and could benefit seismic image segmentation.

## Potential Improvements / 潜在改进方向

1. **Multi-head attention**: Original Transformer uses multi-head; EQTransformer uses single-head. Multi-head might capture more diverse features.
2. **Self-supervised pre-training**: Pre-train on unlabeled seismic data (like BERT) before fine-tuning on labeled picks — reduces annotation cost.
3. **Cross-station attention**: Extend to multi-station inputs (like Van Den Ende & Ampuero 2020 GNN approach) for network-level feature aggregation.
4. **Real-time deployment**: Model is 56 layers — could be simplified for edge deployment on monitoring stations.
5. **Application to seismic image segmentation**: The encoder-decoder architecture with attention is essentially a U-Net variant — directly applicable to 2D seismic images.

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

> Paper Note inherits basic code status from Literature Card, then adds deep analysis.

- **Code Status**: [x] Confirmed Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked
- **Official URL**: https://github.com/smousavi05/EQTransformer
- **Framework**: TensorFlow (mentioned in paper)
- **Checkpoint / Pre-trained Weights**: [ ] Available [ ] Not mentioned [ ] Not applicable
- **Last Repository Update**: <!-- unknown -->
- **Code Quality Indicators**: <!-- stars, forks, issues responsiveness, documentation quality -->

## Missing Reproduction Components / 缺失的复现组件

> 即使代码公开，也可能缺少某些关键组件导致无法复现。逐项评估。

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [x] Yes [ ] No [ ] Partial | GitHub repo | EQTransformer package |
| Dataset Access | [x] Public [ ] Restricted [ ] Private | STEAD (GitHub), HiNet (BOSAI) | Both publicly accessible |
| Pre-trained Checkpoint | [ ] Yes [ ] No [ ] N/A | Not mentioned in paper | May be in repo |
| Preprocessing Scripts | [x] Fully Listed [ ] Partially [ ] Missing | Bandpass 1-15Hz, normalization | Clearly described |
| Hyperparameters | [ ] Fully Listed [x] Partially [ ] Missing | Adam, dropout=0.1, 89h training | Learning rate schedule and batch size NOT specified |
| Environment Specs | [ ] requirements.txt [ ] Docker [ ] Not specified | TensorFlow mentioned, version unknown | CUDA/Python versions not specified |
| Random Seeds | [ ] Specified [x] Not specified | Not mentioned | |
| Train/Val/Test Split | [x] Defined [ ] Undefined | 85%/5%/10% random | Ratio specified |
| Data Augmentation | [x] Described [ ] Vaguely [ ] Not described | 6 augmentation types with probabilities | Well described |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [ ] Easy [x] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: <!-- 2-3 weeks with some trial and error -->
- **Hardware Requirements**: <!-- 4×Tesla-V100 GPUs, ~89 hours training -->
- **Key Barriers**: Learning rate schedule unspecified, batch size unknown, no random seed, no environment file
- **Workaround Options**: Use standard LR schedule (cosine decay), estimate batch size from training time, set seed manually
- **RTX 4070 Compatibility**: [x] Runs fine [ ] May struggle [ ] Won't fit in VRAM
- **Gap Between Code Existence and Reproducibility**: Code and architecture are well-documented. Main gap is hyperparameter details (LR schedule, batch size). These can be reasonably inferred or searched for in the code repository.

# Related Notes / 相关笔记

- Method: [[PhaseNet]], [[Transformer]], [[Attention Mechanism]], [[CNN]]
- Task: [[Seismic Phase Picking]]
- Dataset: [[EGS Collab SURF]]
