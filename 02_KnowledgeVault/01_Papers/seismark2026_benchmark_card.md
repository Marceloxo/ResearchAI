---
title: "SeisMark: A Large-Scale Open Benchmark for Robust 3D Seismic Fault Detection"
authors: [Anonymous]
year: 2026
venue: "待确认（预印本/投稿中）"
task: [Benchmark, 3D Seismic Fault Detection]
method: [Benchmark Pipeline, Procedural Geology, Diffusion-Based Texture Synthesis, Domain Adaptation]
dataset: [SeisMark Benchmark, F3 Netherlands, Gorgon Australia]
code_available: Not Found Yet
importance: High
reading_status: to_read
tags: []
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: SeisMark: A Large-Scale Open Benchmark for Robust 3D Seismic Fault Detection
- **Authors**: Anonymous（投稿中）
- **Year**: 2026
- **Venue**: 待确认（预印本/投稿中）
- **Task**: 三维地震断层检测基准测试（3D Seismic Fault Detection Benchmark）
- **Method**: 混合数据生成管线（程序化地质建模 + 1D正演模拟 + 扩散模型纹理合成）
- **Dataset**: SeisMark Benchmark（1500×1500×1200体素，2.7B体素，约65GB）
- **Code**: Not Found Yet（论文称接受后将公开）

# Research Problem / 研究问题

地震解释领域存在一个根本性的**数据悖论（Data Paradox）**：
- **野外数据**有真实纹理但缺乏可靠标注（标注主观性强，小断层常被漏标）
- **合成数据**有精确标注但纹理过于干净（Sim2Real差距大）
- 现有合成基准（如FaultSeg3D数据集）采用简化声学近似，导致模型在合成数据上表现优异但在真实数据上性能崩塌

**核心问题**：能否生成同时满足(a)标注精确和(b)纹理真实的三维地震数据，用于严格评估模型在域偏移下的鲁棒性？

# Main Contribution / 主要贡献

1. **问题定义**：正式将3D地震断层检测定义为存在显著域偏移下的语义分割任务，指出缺乏可靠标注基准的困境。
2. **SeisMark基准数据集**：首创的开放基准，包含2.7B体素的场级三维地震体（1500×1500×1200），具有精确验证的断层标注（493条断层：5条主断层 + 488条次级断层），采用混合管线确保标注完整性。
3. **全面评估**：评估不同代断层分割架构（FaultSeg3D V1 vs V2），量化真实纹理对模型性能的影响，建立基准基线。

# Method Overview / 方法概述

SeisMark采用**三阶段混合数据生成管线**，将结构生成与纹理合成解耦：

**Stage 1 — 程序化模型构建（Procedural Model Building）**
- 基于澳大利亚Gorgon气田的构造背景，使用事件模块化架构
- 模块包括：Deposit（沉积层，含Perlin噪声速度异质性）、Squish（差异压实，产生褶皱）、Fault（铲式正断层，5条主 NNE走向 + 488条次级断层）、Stratigraphic（前积/加积/退积旋回）、Erosion（侵蚀面）
- 输出：三维P波速度模型 + 体素对齐的断层标签

**Stage 2 — 正演模拟引擎（Forward Modeling Engine）**
- 1D褶积模型：计算反射率序列 → 与25Hz Ricker子波褶积
- 采用轻量级代理，将复杂波传播效应委托给后续扩散阶段

**Stage 3 — 扩散模型纹理合成（Diffusion-Based Style Transfer）**
- 条件图像到图像翻译框架：伪地震体作为结构条件（控制信号）
- 在F3（1987年窄方位角拖缆）或Gorgon（2015-2016年全方位OBN）数据上训练扩散模型
- 通过初始噪声水平（timestep t）和引导尺度控制纹理强度（Low vs. High）
- 严格标签保持约束：通过SSIM（>0.88）和梯度幅度相关性GMC（>0.87）验证

**基准变体**（5种，共享相同标注）：
| 变体 | 纹理来源 | 强度 | 大小 |
|------|---------|------|------|
| SeisMark-Clean | 纯物理 | N/A | 10.8 GB |
| SeisMark-F3-L | 北海F3 | 低 | 10.8 GB |
| SeisMark-F3-H | 北海F3 | 高 | 10.8 GB |
| SeisMark-Aus-L | 澳大利亚Gorgon | 低 | 10.8 GB |
| SeisMark-Aus-H | 澳大利亚Gorgon | 高 | 10.8 GB |

# Dataset and Evaluation / 数据集与评估

**数据集规格**：
- 范围：18.75 km × 18.75 km × 6.0 km
- 体素间距：12.5 m × 12.5 m × 5.0 m
- 断层：493条（5条主 NNE走向铲式正断层 + 488条次级合成/反倾断层）
- 地层：14个层位标签，速度范围1500-4912 m/s
- 总大小：约65 GB

**评估方法**：
- 零样本评估（Zero-shot）：使用V1和V2模型预训练权重，直接在Styled变体上测试
- 空间容忍度T：采用3D形态膨胀（3×3×3结构，迭代T次），报告T ∈ {0, 1, 2}
- 指标：IoU, Precision, Recall, F1

**基线模型**：
- **V1 (FaultSeg3D)**：标准U-Net，合成+随机噪声训练，代表传统方法
- **V2 (FaultSeg3D+)**：更深残差架构，课程式真实噪声训练，代表最先进水平

**关键结果**：
| 变体 | V1 F1(T=1) | V2 F1(T=1) | 结论 |
|------|-----------|-----------|------|
| Clean | 0.541 | 0.723 | 简化数据存在Recall饱和 |
| F3-Low | 0.591 | **0.750** | 低强度纹理有"甜蜜点"效应 |
| F3-High | 0.450 | 0.660 | V1性能崩塌（Recall从0.816→0.380） |
| Aus-Low | 0.581 | 0.726 | |
| Aus-High | 0.417 | 0.730 | V2最高Precision 0.923 |

**结构保真度验证**：SSIM 0.88-0.97, GMC 0.87-0.93，确认纹理注入未破坏断层标注。

# Why This Paper Matters / 为什么关注这篇论文

1. **填补了地震解释基准的空白**：作为首个融合物理精确标注+真实纹理的大规模开放基准，SeisMark类似于ImageNet在地震领域的角色，对评估和推动地震AI发展至关重要。
2. **揭示了现有基准的"错觉"**：论文证明简化合成数据存在Recall饱和效应，传统模型在Clean数据上表现与SOTA模型相当，但真实纹理下性能崩塌，说明现有评估过于乐观。
3. **扩散模型+地质建模的创新管线**：三阶段管线（程序化建模→物理正演→扩散纹理）实现了结构精确性与纹理真实性的解耦，具有高度可扩展性。
4. **对CCS等安全关键应用的重要性**：准确的断层检测是碳捕集与封存（CCS）项目安全性的前提，SeisMark为评估部署就绪性提供了严格标准。

# Limitations / 局限性

1. **匿名预印本**：作者身份未知，论文尚未被正式接收，可能仍有修改。
2. **仅评估了两种模型**：V1和V2均来自同一系列（FaultSeg3D），未包含Transformer架构（如论文1的FaultEdgeFormer）或其他SOTA方法。
3. **1D褶积模型的物理简化**：虽然扩散模型弥补了纹理不足，但1D褶积无法模拟绕射波、多次波等复杂波场效应。
4. **仅一个地质模型**：基于Gorgon单一构造背景，虽然断层多样但地质背景有限，模型可能对特定构造风格存在过拟合。
5. **数据量大**：65GB的单体数据对存储和加载提出较高要求，可能限制部分研究者的使用。

# Reproducibility Status / 可复现性状态

> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [ ] Available [X] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Only fill when Status = Available -->

## Data Status / 数据可用性

- [ ] **Public dataset available** — freely downloadable
- [ ] **Restricted dataset** — requires application or license
- [ ] **Private dataset** — not publicly accessible
- [X] **Unknown** — paper does not specify

**Dataset Link**: 论文声称"All datasets will be made publicly available upon acceptance of the paper."（接受后公开）

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [ ] High [X] Medium [ ] Low

**Reason**: 数据生成管线描述详细（含附录中的模块实现和构建序列），但(a)程序化建模代码未公开，(b)扩散模型训练代码未公开，(c)数据集本身待论文接受后发布。用户可复现评估流程（使用V1/V2预训练权重），但完整管线复现需等待代码发布。

**Notes / 备注**: 论文接受后数据集将公开，这是关键资源。建议关注其发布状态并及时纳入KnowledgeVault。

# My Decision / 我的决定

- [X] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: SeisMark作为地震断层检测领域的首个大规模开放基准，对本项目具有战略意义。建议进入Level 2 Paper Note分析，重点关注：(a)基准数据集发布后获取和评估；(b)将FaultEdgeFormer等模型在SeisMark上进行测试；(c)其扩散纹理合成管线的可移植性。

# Related Knowledge / 相关知识链接

- Task: [[3D Seismic Fault Detection Benchmark]]
- Method: [[Procedural Geology]], [[Diffusion-Based Texture Synthesis]]
- Dataset: [[SeisMark]], [[F3 Netherlands]], [[Gorgon]]

## Zotero

- **Item Key**: YBC44YPE
- **Type**: Benchmark/Preprint