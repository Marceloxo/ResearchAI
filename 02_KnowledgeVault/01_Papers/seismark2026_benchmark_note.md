---
title: "SeisMark: A Large-Scale Open Benchmark for Robust 3D Seismic Fault Detection"
authors: [Anonymous]
year: 2026
venue: "待确认（预印本/投稿中）"
task: [Benchmark, 3D Seismic Fault Detection]
methods: [Benchmark Pipeline, Procedural Geology, Diffusion-Based Texture Synthesis, Domain Adaptation]
datasets: [SeisMark Benchmark, F3 Netherlands, Gorgon Australia]
metrics: [IoU, Precision, Recall, F1, SSIM, GMC]
code: "Not Found Yet (论文接受后将公开)"
importance: High
status: deep_reading
paper_type: benchmark
tags: [seismic-fault-detection, benchmark, domain-shift, sim2real, diffusion-model, procedural-geology, seismark]
created: 2026-07-20
---

# Paper Type / 论文类型

Type: **benchmark** — 提供首个大规模开放基准测试SeisMark，用于鲁棒的3D地震断层检测在域偏移下的评估

# One Sentence Summary / 一句话总结

SeisMark通过创新的三阶段混合管线（程序化地质建模→1D物理正演→扩散模型纹理合成），生成了2.7B体素（1500×1500×1200）的场级三维地震基准，包含5种纹理变体和493条精确标注的断层，揭示了现有简化合成数据存在Recall饱和效应，证明真实纹理下V1模型性能崩塌而V2模型保持鲁棒。

# Research Background / 研究背景

地震解释领域存在一个根本性的**数据悖论（Data Paradox）**：

- **野外数据**有真实纹理但缺乏可靠标注（标注主观性强，小断层常被漏标，不同解释者之间差异大）
- **合成数据**有精确标注但纹理过于干净（Sim2Real差距大）
- 现有合成基准（如FaultSeg3D数据集）采用简化声学近似，导致模型在合成数据上表现优异但在真实数据上性能崩塌

**核心问题**：能否生成同时满足(a)标注精确和(b)纹理真实的三维地震数据，用于严格评估模型在域偏移下的鲁棒性？

**类比**：ImageNet推动了计算机视觉的进步，但地球物理学缺乏类似的标准化、可验证基准。OpenFWI（全波形反演）是重要先驱，但它是回归任务且规模较小，不直接服务于地震解释中的断层检测任务。

**安全关键应用**：准确的断层检测是碳捕集与封存（CCS）项目安全性的前提——未检测到的断层可能成为CO₂泄漏通道，危及长期封存完整性。

# Problem Definition / 问题定义

- **Input / 输入**: 三维地震数据体 $S_{\text{styled}} \in \mathbb{R}^{D \times H \times W}$，尺寸为1500×1500×1200（约2.7B体素），物理范围18.75 km × 18.75 km × 6.0 km，体素间距12.5 m × 12.5 m × 5.0 m
- **Output / 输出**: 断层概率图 $Y_{\text{pred}} \in \{0, 1\}^{D \times H \times W}$，二值分割掩码

**任务定义**：场级（field-scale）三维语义分割，在存在显著域偏移（domain shift）下评估模型鲁棒性。采用零样本（zero-shot）评估：模型使用预训练权重，直接在Styled变体上测试，不进行微调。

# Motivation / 研究动机

**现有合成数据的"错觉"问题**：

1. **Recall饱和效应**：在Clean（简化物理）数据上，传统V1模型和SOTA V2模型Recall均超过0.80，难以区分模型真实能力差异。简化数据无法有效测试模型的敏感性。

2. **Sim2Real差距**：标准物理模拟依赖简化声学近似，无法模拟绕射波、多次波、采集足迹等真实波场特征。模型在合成数据上表现优异，但在真实数据上性能崩塌。

3. **缺乏标准化评估框架**：不同研究使用不同的合成数据、不同的评估协议（如是否使用空间容忍度T），导致结果不可比。

4. **CCS安全需求**：随着碳捕集与封存（CCS）和地热能源需求增长，断层检测从"勘探辅助"上升为"安全关键"任务，需要严格的、可验证的基准来评估模型部署就绪性。

# Main Contributions / 主要贡献

1. **问题定义**：正式将3D地震断层检测定义为存在显著域偏移下的语义分割任务，指出缺乏可靠标注基准的困境，提出评估路线图。

2. **SeisMark基准数据集**：首创的开放基准，包含2.7B体素的场级三维地震体（1500×1500×1200），具有精确验证的断层标注（493条断层：5条主断层 + 488条次级断层），采用混合管线确保标注完整性。

3. **全面评估**：评估不同代断层分割架构（FaultSeg3D V1 vs V2），量化真实纹理对模型性能的影响，揭示Recall饱和效应和"甜蜜点"效应，建立基准基线。

# Method / 方法

## Overall Framework / 整体框架

SeisMark采用**三阶段混合数据生成管线**，将结构生成与纹理合成解耦：结构由程序化地质建模提供（可验证的精确标注），纹理由扩散模型从真实野外数据迁移（真实视觉特征）。

管道流程：随机种子 + 地质参数 → **Stage 1** 程序化模型构建（P波速度模型V + 断层标签Y） → **Stage 2** 1D正演模拟（伪地震体S_pseudo） → **Stage 3** 扩散模型纹理合成（Styled地震体S_styled，保持标签Y）

## Key Modules / 关键模块

### Stage 1: 程序化模型构建（Procedural Model Building）

基于澳大利亚Gorgon气田的构造背景，采用事件模块化架构：

- **Deposit模块**：沉积层生成，含3D Perlin噪声速度异质性，随机化层间边界
- **Squish模块**：差异压实，使用2D分形噪声场产生褶皱和厚度变化
- **Fault模块**：铲式正断层（listric normal fault），通过坐标旋转和深度变化倾角实现，含5条主NNE走向断层+488条次级断层
- **Stratigraphic模块**：前积/加积/退积旋回，模拟碳酸盐岩斜坡沉积
- **Erosion模块**：侵蚀面，分形海底地形

**输出**：三维P波速度模型（1500-4912 m/s）+ 体素对齐的断层标签（493条）

### Stage 2: 1D正演模拟引擎（Forward Modeling Engine）

- 计算阻抗对比（使用Gardner关系估算密度）→ 反射率序列
- 与25Hz零相位Ricker子波褶积 → 伪地震体
- 采用轻量级代理，复杂波传播效应委托给后续扩散阶段

### Stage 3: 扩散模型纹理合成（Diffusion-Based Style Transfer）

**核心思想**：条件图像到图像翻译框架，伪地震体作为结构条件（控制信号）。扩散模型在真实野外数据（F3或Gorgon）上训练，从部分噪声状态开始迭代去噪。

**纹理强度控制**：
- 通过初始噪声水平（timestep t）和引导尺度（guidance scale）控制
- 低强度：仅修改高频频谱内容（精细纹理）
- 高强度：允许修改中频振幅（模拟更强的采集足迹）

**标签保持约束**：
- 通过条件机制强制：模型偏离伪地震体结构边缘时受惩罚
- SSIM > 0.88（全局结构保持）
- GMC（梯度幅度相关）> 0.87（局部边缘保持）

**盆地特定纹理**：
- **F3（1987年窄方位角拖缆）**：老式采集，可见采集足迹，振幅变化显著
- **Gorgon（2015-2016年全方位OBN）**：现代采集，宽带频率，最小采集足迹，反射连续

## Benchmark Variants / 基准变体

5种变体共享相同的精确标注，便于直接比较：

| 变体 | 纹理来源 | 强度 | 大小 | 说明 |
|:----:|:---------:|:----:|:----:|:----:|
| SeisMark-Clean | 纯物理 | N/A | 10.8 GB | 基线，理想物理情景 |
| SeisMark-F3-L | 北海F3 | 低 | 10.8 GB | 低强度老式采集纹理 |
| SeisMark-F3-H | 北海F3 | 高 | 10.8 GB | 高强度老式采集纹理 |
| SeisMark-Aus-L | 澳大利亚Gorgon | 低 | 10.8 GB | 低强度现代OBN纹理 |
| SeisMark-Aus-H | 澳大利亚Gorgon | 高 | 10.8 GB | 高强度现代OBN纹理 |

**难度递进阶梯**：Clean → Low Intensity → High Intensity，逐步增加域偏移程度。

# Dataset / 数据集

## SeisMark数据集规格

| Property | Value |
|----------|-------|
| 维度 | 1500 × 1500 × 1200 体素 |
| 物理范围 | 18.75 km × 18.75 km × 6.0 km |
| 体素间距 | 12.5 m × 12.5 m × 5.0 m |
| 总体素量 | 2.70 billion（约65 GB） |
| 地层标签 | 14个唯一层位 |
| 断层标签 | 493条（5条主断层 + 488条次级断层） |
| 速度范围 | 1500-4912 m/s |
| 地质背景 | 基于Gorgon气田，Northern Carnarvon Basin |

## 断层特征

| 属性 | 主断层（5条） | 次级断层（488条） |
|:----:|:------------:|:----------------:|
| 走向 | ~30°/210°（NNE） | 主断层±10° |
| 地表倾角 | 45-70° | 与主断层相似 |
| 长度 | 固定模板 | 对数均匀（10-100%平均长度） |
| 位移 | 0.4-0.7 × shift_scale | 长度的16.7-30% |
| 深度范围 | 贯穿整个前断层段 | 上部前断层段 |

# Experimental Setup / 实验设置

**评估协议**：
- **零样本评估（Zero-shot）**：使用V1/V2模型预训练权重，直接在Styled变体上测试（不微调）
- **空间容忍度T**：采用3D形态膨胀（3×3×3结构，迭代T次），报告T ∈ {0, 1, 2}
  - Recall：膨胀预测掩码后再与GT相交
  - Precision：膨胀GT掩码后再与预测相交
  - T=0：严格逐像素匹配
  - T=1-2：考虑薄断层线的空间不确定性

**基线模型**：
- **V1 (FaultSeg3D)**：标准U-Net，合成数据+随机噪声训练，代表传统方法
- **V2 (FaultSeg3D+)**：更深残差架构，课程式真实噪声训练，代表最先进水平

**结构保真度验证**：SSIM（全局结构相似性）+ GMC（梯度幅度相关性，验证断层边缘稳定性）

# Results / 实验结果

## 结构保真度验证

| 纹理来源 | 强度 | SSIM ↑ | GMC ↑ |
|:--------:|:----:|:------:|:-----:|
| F3 North Sea | Low | 0.92 | 0.91 |
| F3 North Sea | High | 0.88 | 0.87 |
| Gorgon Australia | Low | 0.97 | 0.93 |
| Gorgon Australia | High | 0.96 | 0.90 |

**结论**：SSIM > 0.88，GMC > 0.87，确认纹理注入未破坏断层标注。GMC的降低是由于纹理引入了额外的高频梯度（模拟噪声），而非断层位移。

## 基准性能对比（T=1, 有效地质容忍度）

| 变体 | V1 F1 | V2 F1 | V1 Precision | V2 Precision | V1 Recall | V2 Recall |
|:----:|:-----:|:-----:|:------------:|:------------:|:---------:|:---------:|
| Clean | 0.541 | 0.723 | 0.405 | 0.660 | 0.816 | 0.800 |
| F3-Low | 0.591 | **0.750** | 0.702 | **0.891** | 0.511 | 0.648 |
| F3-High | 0.450 | 0.660 | 0.552 | 0.872 | 0.380 | 0.531 |
| Aus-Low | 0.581 | 0.726 | 0.742 | 0.911 | 0.478 | 0.603 |
| Aus-High | 0.417 | 0.730 | 0.577 | **0.923** | 0.326 | 0.683 |

## 关键发现

### 发现1：Recall饱和效应（Clean数据）

在Clean数据上，V1和V2的Recall均超过0.80（V1: 0.816, V2: 0.800），难以区分模型真实能力。但F1较低（V1: 0.541, V2: 0.723），因为地质建模产生的尖锐干扰伪影被误判为断层（低Precision）。**说明简化物理数据不足以作为严格的性能测试集**。

### 发现2：低强度纹理的"甜蜜点"效应

F3-Low变体上V2的F1达到最高0.750，优于Clean基线（0.723）。原因：扩散纹理合成起到了**相干性滤波器**的作用，修复了纯物理输入中模拟断层伪影的尖锐干扰，使反射更连续自然，减少了V2的误报。

### 发现3：高强度纹理下V1性能崩塌

在高强度纹理下，V1的Recall从0.816（Clean）骤降至0.326（Aus-High），F1从0.541降至0.417，性能崩塌。而V2保持相对鲁棒，在Aus-High上F1=0.730，Precision甚至达到0.923。**SeisMark成功区分了传统模型和鲁棒模型的真实能力差距**。

### 发现4：V2的精度优势

V2在所有Styled变体上的Precision均显著高于V1（0.872-0.923 vs 0.552-0.742），说明残差架构和课程式真实噪声训练有效提升了模型在真实纹理下的抗干扰能力。

# Ablation Study / 消融实验

## 纹理强度的影响

| 强度 | V1 F1 (F3) | V2 F1 (F3) | V1 F1 (Aus) | V2 F1 (Aus) |
|:----:|:----------:|:----------:|:-----------:|:-----------:|
| Clean | 0.541 | 0.723 | 0.541 | 0.723 |
| Low | 0.591 | 0.750 | 0.581 | 0.726 |
| High | 0.450 | 0.660 | 0.417 | 0.730 |

**结论**：
- V1：Low强度有提升（相干性滤波效应），High强度性能崩塌
- V2：F3变体Low>High>Clean，Aus变体Low≈High>Clean
- 纹理来源（F3 vs Aus）对V2影响较小，说明V2模型具有较好的纹理泛化能力

## 空间容忍度的影响

以Clean数据为例，展示T从0到2的变化：

| T | V1 F1 | V2 F1 |
|:-:|:-----:|:-----:|
| 0 | 0.409 | 0.460 |
| 1 | 0.541 | 0.723 |
| 2 | 0.571 | 0.754 |

**结论**：T=0时所有模型F1均较低（<0.5），说明断层体素级的精确匹配非常困难。T≥1是更合理的评估标准，反映了地质解释中的实际容忍度。

# Limitation / 局限性

1. **匿名预印本**：作者身份未知，论文尚未被正式接收，可能仍有修改。
2. **仅评估了两种模型**：V1和V2均来自同一系列（FaultSeg3D），未包含Transformer架构（如FaultEdgeFormer）或其他SOTA方法，限制了基准的全面性。
3. **1D褶积模型的物理简化**：虽然扩散模型弥补了纹理不足，但1D褶积无法模拟绕射波、多次波等复杂波场效应。
4. **仅一个地质模型**：基于Gorgon单一构造背景，虽然断层多样（493条）但地质背景有限，模型可能对特定构造风格存在过拟合。
5. **数据量大**：65GB的单体数据对存储和加载提出较高要求，可能限制部分研究者的使用。
6. **扩散模型的计算开销**：生成Styled变体需要训练扩散模型，管线整体计算成本较高。
7. **标签保持约束的局限性**：SSIM和GMC是参考指标，可能无法完全捕捉极细微的断层位移，特别是当纹理噪声与断层边缘频率重叠时。

# My Analysis / 我的分析

## Transferable Ideas / 可迁移思想

1. **结构-纹理解耦管线**：程序化建模（精确标注）+ 物理正演（结构骨架）+ 扩散模型（真实纹理）的三阶段管线是通用的，可迁移到其他地震解释任务（如盐体检测、相分类、层位追踪）。

2. **"甜蜜点"效应**：低强度扩散纹理修复了纯物理数据的伪影，提升了模型性能。这一发现提示：**适度的纹理增强可作为数据增强策略**，而非简单的噪声添加。

3. **空间容忍度评估**：T=0的严格逐像素匹配对薄断层线不公平，T≥1的形态膨胀评估更合理。这一评估协议可推广到其他细长结构的分割任务（如血管分割、道路分割）。

4. **Recall饱和检测**：如果两个模型在现有基准上Recall都超过0.80，说明基准复杂度不够。SeisMark的"难度递进"设计思路值得借鉴。

## Potential Improvements / 潜在改进方向

1. **评估FaultEdgeFormer在SeisMark上的性能**：FaultEdgeFormer的可训练Sobel卷积和改进Swin Transformer可能在高强度纹理下表现出不同的鲁棒性特征，这是最直接的后续工作。

2. **扩展地质多样性**：增加更多地质背景（如压缩构造、走滑构造、盐构造），构建多盆地SeisMark套件。

3. **引入更丰富的基线模型**：包括FaultEdgeFormer、UNETR、Swin UNETR等Transformer架构，以及半监督/自监督方法（如FaultSSL）。

4. **提供训练/验证拆分**：当前SeisMark仅提供测试评估，可考虑增加训练集拆分（如裁剪为子块），允许研究者使用SeisMark数据训练模型。

5. **多任务扩展**：在断层标注基础上增加层位标注、盐体标注等，扩展为多任务基准。

# Reproducibility Analysis / 复现性分析

## Official Implementation Verification / 官方实现验证

**Code Status**:
- [ ] Confirmed Available — verified the repository exists and is accessible
- [ ] Confirmed Missing — full-text verification confirms no code is provided
- [X] **Not Found Yet** — paper mentions code but URL not located
- [ ] Not Checked — agent has not verified (requires human follow-up)

**Evidence Location**: 论文声称"All datasets will be made publicly available upon acceptance of the paper." 代码将在论文接收后公开。

**Repository URL**: 未找到（论文接收后将公开）

**Framework**: 未明确说明（推测为PyTorch，基于扩散模型和3D CNN）

**Checkpoint / Pre-trained Weights**: [ ] Available [X] Not mentioned [ ] Not applicable
- V1和V2预训练权重来自原始论文（FaultSeg3D和FaultSeg3D+），但SeisMark论文未提供

**Last Repository Update**: N/A

**Code Quality Indicators**: N/A

**Verification Method**: 论文全文搜索，未发现代码仓库链接

## Missing Reproduction Components / 缺失的复现组件

| Component | Available? | Source Location | Notes |
|-----------|-----------|-----------------|-------|
| Source Code | [ ] Yes [X] No [ ] Partial | 待论文接收后公开 | 程序化建模 + 扩散模型代码 |
| Dataset Access | [ ] Public [ ] Restricted [X] Private (待发布) | 论文接收后公开 | 65GB单体数据 |
| Pre-trained Checkpoint | [ ] Yes [X] No [ ] N/A | — | V1/V2权重需从原始论文获取 |
| Preprocessing Scripts | [ ] Yes [X] No [ ] Not mentioned | — | 正演模拟脚本未公开 |
| Hyperparameters | [X] Fully Listed [ ] Partially [ ] Missing | 附录B | 15步构建序列完整，参数详细 |
| Environment Specs | [ ] requirements.txt [ ] Docker [X] Not specified | — | 未指定 |
| Random Seeds | [ ] Specified [X] Not specified | — | 程序化建模使用随机种子，但未指定具体值 |
| Train/Val/Test Split | [ ] Defined [X] Undefined | — | 基准仅为测试集，无训练/验证拆分 |
| Data Augmentation | [ ] Described [ ] Vaguely [X] Not described | — | 不适用（零样本评估） |

## Reproduction Difficulty Assessment / 复现难度评估

- **Overall Difficulty**: [ ] Easy [X] Moderate [ ] Hard [ ] Impossible
- **Estimated Effort**:
  - **评估复现**（使用预发布数据集）：数天
  - **完整管线复现**：数周至数月
- **Hardware Requirements**:
  - 评估：单GPU 12GB VRAM（V1/V2推理）
  - 完整管线：多GPU（扩散模型训练）
- **Key Barriers**:
  1. 数据集和代码均未公开（论文接收后发布）
  2. 程序化建模代码（Gorgon地质模型）需要专业地质知识
  3. 扩散模型训练需要大量计算资源
- **Workaround Options**:
  1. 关注论文发布状态，及时获取数据和代码
  2. 可自行实现V1/V2评估流程（权重来自FaultSeg3D/FaultSeg3D+原始论文）
- **RTX 4070 Compatibility**: [X] Runs fine [ ] May struggle [ ] Won't fit in VRAM
  - 评估阶段（V1/V2推理）完全可在RTX 4070上运行

## Reproducibility vs. Code Availability

- **Code Exists**: [ ] Yes [X] No (待发布)
- **Paper Actually Reproducible**: [ ] Yes [ ] Partially [X] No（当前阶段）
  - 论文接受后数据集和代码公开，情况将改善
- **Gap Between Code Existence and Reproducibility**: 当前阶段代码和数据集均未公开，论文的评估协议（V1/V2零样本测试）可基于FaultSeg3D原始论文复现，但SeisMark数据本身和完整生成管线不可复现。建议关注论文发布状态，及时纳入KnowledgeVault。

# Related Notes / 相关笔记

- Method: [[Procedural Geology]], [[Diffusion-Based Texture Synthesis]]
- Task: [[3D Seismic Fault Detection Benchmark]]
- Dataset: [[SeisMark]], [[F3 Netherlands]], [[Gorgon]]
- Model: [[FaultEdgeFormer]] — 建议在SeisMark上评估FaultEdgeFormer的鲁棒性