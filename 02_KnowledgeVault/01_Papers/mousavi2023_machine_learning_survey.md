---
title: "Machine Learning in Earthquake Seismology"
authors: [Mousavi, Beroza]
year: 2023
venue: "Annual Review of Earth and Planetary Sciences"
task: [Seismic Event Monitoring]
methods: [ML, Deep Learning, CNN, RNN, Transformer, GAN, PINN]
datasets: [NCEDC, various]
metrics: [various per task]
code: "Mixed — SeisBench, EQTransformer, PhaseNet (all open source)"
importance: high
status: done
paper_type: survey
tags: [survey, ml, earthquake-seismology, annual-review, mousavi-beroza]
created: 2026-07-09
---

# Paper Type / 论文类型

Type: survey

# One Sentence Summary / 一句话总结

Mousavi & Beroza (2023) 按地震处理任务（判别→检测→拾波→定位→震级→源参数→模拟→地表运动）系统综述了ML在地震学中的应用，指出基准数据集和开源框架的缺失是领域发展的主要瓶颈。

# Research Background / 研究背景

机器学习在地震学中已有数十年历史，但近年来因计算能力突破、深度学习架构发展和大规模标注数据可用而快速发展。地震监测流水线（检测→拾波→定位→震级→源参数）的每个环节都被ML方法渗透。这篇综述旨在提供全景式地图，帮助研究者理解领域全貌和未来方向。

# Problem Definition / 问题定义

- **Input / 输入**: N/A (综述论文)
- **Output / 输出**: 按8大任务组织的ML应用全景图 + 未来方向建议

# Motivation / 研究动机

1. ML在地震学中的应用快速增长，但缺乏系统性总结
2. 不同子领域进展不均（拾波/检测已成熟，源机制反演仍处早期）
3. 缺乏统一基准数据集阻碍方法比较
4. 需要推动开源框架和基准测试

# Main Contributions / 主要贡献

1. **按任务组织的全面综述**：覆盖8大地震处理任务，每任务回顾AI→DL→SOTA演进
2. **指出领域瓶颈**：基准数据集缺失、开源框架不足、泛化性验证缺乏
3. **推动SeisBench等工具**：倡导开源基准框架
4. **提出未来方向**：无监督学习、物理约束网络(PINN)、多站联合建模

# Method / 方法

## Overall Framework / 整体框架

综述按地震监测流水线组织：

```
Event Discrimination → Detection → Phase Picking → Location → Magnitude → Source Parameters → Seismogram Simulation → Ground Motion
```

## Key Modules / 关键模块

### Module 1: Event Discrimination (2.1)

- **Explosions vs Earthquakes**: CNN/RNN >99% accuracy (Linville et al. 2019)
- **Volcano-seismic**: Transfer learning from natural/handwritten images (Titos et al. 2020)
- **Source depth/distance/type**: Self-supervised autoencoder (Mousavi et al. 2019b)

### Module 2: Earthquake Detection (2.2)

- Early: STA/LTA, wavelet-based
- AI: ANN (Wang & Teng 1995), SVM, HMM
- DL: CNN (Perol et al. 2018), RNN, capsule NN, attentive models
- Innovation: Feature-domain template matching (Xiao et al. 2021)

### Module 3: Phase Picking (2.3)

- **Pioneering**: HMM, shallow NN
- **Modern**: PhaseNet (Zhu & Beroza 2019), EQTransformer (Mousavi et al. 2020)
- **Multi-station**: Yang et al. 2021, Zhu et al. 2022b
- **Generalization**: Transfer learning (Lapins et al. 2021)
- **Benchmarking**: SeisBench (Woollam et al. 2022)

### Module 4: Earthquake Location (2.4)

- Single-station: CNN regression (Wei & Zhu 2019), Bayesian CNN
- Multi-station: CNN classification (Zhang et al. 2020), GNN (Van Den Ende & Ampuero 2020)
- Dynamic multi-station: Transformer (Münchmeyer et al. 2021a)
- Physics-informed: PINN (Smith et al. 2022)

### Module 5: Magnitude Estimation (2.5)

- Single-station: CNN+RNN (Mousavi & Beroza 2020b)
- Multi-station: Simulated data training (Lin et al. 2021)
- EEW: DNN from prompt elasto-gravity signals (Licciardi et al. 2022)

### Module 6: Source Parameterization (2.6)

- Focal mechanism: CNN on synthetic waveforms (Kuang et al. 2021)
- Moment tensor: Bayesian NN ensemble (Steinberg et al. 2021)
- Physics-guided: Unsupervised displacement amplitude learning (Zhang et al. 2021)

### Module 7: Seismogram Simulation (2.7)

- PINN for wave equation (Moseley et al. 2020a, Song et al. 2020)
- GAN for synthetic data augmentation (Wang et al. 2021)
- Orders of magnitude faster than numerical methods

### Module 8: Ground Motion Characterization (2.8)

- Nonparametric GMPE: NN, Random Forest, SVM
- End-to-end EEW: CNN from first 3s waveform (Hsu & Huang 2021)
- Network-level: Transformer for multi-station PGA (Münchmeyer et al. 2021b)

# Dataset / 数据集

| Dataset | Size | Modality | Description |
|---|---|---|---|
| NCEDC | 779K+ waveforms | 3C seismograms | Northern California (used in PhaseNet, EQTransformer) |
| Japan Tottori | 21K+ events | Continuous data | AI-detected vs JMA-manual (Figure 2 in paper) |
| Italy AVN | 900K+ events | Dense network | Amatrice-Visso-Norcia sequence |
| Various | Thousands | Multiple | Chile subduction zone, volcanic regions, mines |

# Experimental Setup / 实验设置

> 综述论文，无单一实验。每小节引用代表性工作的实验设置。

# Results / 实验结果

> 综述不提供统一结果表，而是按任务总结SOTA性能：

| Task | SOTA Method | Key Performance |
|---|---|---|
| Event Discrimination | CNN/RNN | >99% accuracy (explosions vs earthquakes) |
| Detection | Attentive CNN | Similar sensitivity to match filter, faster |
| Phase Picking | EQTransformer | Near-human accuracy, 2× more events detected |
| Location | GNN/Transformer | ~10m precision on dense networks |
| Magnitude | CNN+RNN | Universal attenuation model |
| Simulation | PINN | Orders of magnitude faster than numerical |

# Ablation Study / 消融实验

> 不适用（综述论文）。但论文讨论了各方法的优势和局限性。

# Limitation / 局限性

> 论文自己承认的局限 + 你看到的局限

**Author-admitted:**
- 部分子领域（火山地震、源机制反演）文献有限，进展缓慢
- 深度学习模型在域外泛化性验证不足
- 缺乏统一基准数据集阻碍方法比较
- 震级估计受限于大震样本稀缺

**Agent-identified:**
- 未涵盖2023年的最新工作（出版时间限制）
- 对生成式AI（Diffusion Model等）在地球科学中的应用讨论较少
- 对联邦学习、隐私保护ML等新兴方向未涉及

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **Transformer for multi-station analysis** — 论文提出用Transformer编码台网级观测的时空依赖关系。这对地震图像分割有直接启发：将像素/测线视为"虚拟台站"，用attention建模长程依赖。
2. **Physics-Informed Neural Networks (PINN)** — 将波动方程嵌入损失函数。对地震图像，可将成像物理约束（如射线追踪）融入分割网络的训练。
3. **Self-supervised pre-training** — 无标注数据丰富的情况下，先用自监督学习预训练，再用少量标注微调。这对标注成本极高的地震图像分割至关重要。
4. **Domain adaptation** — 论文明确指出迁移学习是解决泛化性的可行路径。Chai 2020正是这一思想的实践（PhaseNet从km级迁移到m级）。

## Potential Improvements / 潜在改进方向

1. **Diffusion Models for seismic data** — 论文未涉及扩散模型。这在波形生成/增强方面有潜力。
2. **Foundation Models for seismology** — 类比NLP中的BERT，训练一个通用的地震信号基础模型。
3. **Active learning for annotation** — 减少人工标注成本，解决标注稀缺问题。
4. **Uncertainty quantification** — 论文提到贝叶斯神经网络，但未深入讨论。对实际部署至关重要。

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

> Paper Note inherits basic code status from Literature Card, then adds deep analysis.

- **Code Status**: [x] Available [ ] Not Found Yet [ ] Confirmed Missing [ ] Not Checked
- **Official URL**: https://github.com/seisman/seisbench (SeisBench framework)
- **Framework**: PyTorch (most cited implementations)
- **Checkpoint / Pre-trained Weights**: [ ] Available [ ] Not mentioned [ ] Not applicable
- **Last Repository Update**: <!-- unknown -->
- **Code Quality Indicators**: SeisBench is actively maintained with community contributions

## Missing Reproduction Components / 缺失的复现组件

> 综述论文本身不涉及复现。但引用的关键方法（EQTransformer, PhaseNet, SeisBench）均有开源实现。

| Component | Available? | Source Location | Notes |
|---|---|---|---|
| Source Code | [x] Yes [ ] No [ ] Partial | SeisBench, EQTransformer repos | Multiple open-source projects |
| Dataset Access | [x] Public [ ] Restricted [ ] Private | NCEDC, JMA, various | Most datasets publicly accessible |
| Pre-trained Checkpoint | [ ] Yes [ ] No [ ] N/A | Varies by method | Some models provide pre-trained weights |
| Preprocessing Scripts | [x] Fully Listed [ ] Partially [ ] Missing | In respective repos | Generally well-documented |
| Hyperparameters | [x] Fully Listed [ ] Partially [ ] Missing | In papers/repos | Varies by cited method |
| Environment Specs | [ ] requirements.txt [ ] Docker [ ] Not specified | In repos | Varies |
| Random Seeds | [ ] Specified [ ] Not specified | Varies | Not consistently reported |
| Train/Val/Test Split | [x] Defined [ ] Undefined | Varies by method | Generally standard splits |
| Data Augmentation | [x] Described [ ] Vaguely [ ] Not described | In cited papers | Varies |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [x] Easy [ ] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**: N/A (综述论文)
- **Hardware Requirements**: N/A
- **Key Barriers**: N/A
- **Workaround Options**: N/A
- **RTX 4070 Compatibility**: [x] Runs fine [ ] May struggle [ ] Won't fit in VRAM
- **Gap Between Code Existence and Reproducibility**: N/A (综述论文)

# Related Notes / 相关笔记

- Method: [[PhaseNet]], [[Transformer]], [[Attention Mechanism]], [[CNN]], [[U-Net]]
- Task: [[Seismic Phase Picking]]
- Dataset: [[EGS Collab SURF]]
