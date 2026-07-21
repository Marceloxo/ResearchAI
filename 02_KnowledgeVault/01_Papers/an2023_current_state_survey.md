---
title: "Current state and future directions for deep learning based automatic seismic fault interpretation: A systematic review"
authors: [Yu An, Haiwen Du, Siteng Ma, Yingjie Niu, Dairui Liu, Jing Wang, Yuhan Du, Conrad Childs, John Walsh, Ruihai Dong]
year: 2023
venue: "Earth-Science Reviews"
task: [Survey, Literature Review, Fault Interpretation]
method: [Systematic Literature Review, CNN, U-Net, Deep Learning]
dataset: [73 seismic datasets from 56 papers]
code_available: Not Found Yet
importance: Critical
reading_status: Screening Complete
tags: [survey, systematic-review, fault-interpretation, deep-learning, seismic, cnn, unet, benchmark]
created: 2026-07-20
---

# Basic Information / 基本信息

- **Title**: Current state and future directions for deep learning based automatic seismic fault interpretation: A systematic review
- **Authors**: Yu An, Haiwen Du, Siteng Ma, Yingjie Niu, Dairui Liu, Jing Wang, Yuhan Du, Conrad Childs, John Walsh, Ruihai Dong
- **Year**: 2023
- **Venue**: Earth-Science Reviews (IF > 10)
- **Task**: 系统性文献综述 (Systematic Literature Review)
- **Method**: 遵循Kitchenham系统综述指南，7个数字图书馆检索，2012-2022年文献
- **Dataset**: 从56篇论文中提取的73个地震数据集
- **Code**: 未找到（综述论文，无可执行代码）

# Research Problem / 研究问题

自2018年以来，基于深度学习的自动地震断层解释方法不断涌现并展现出良好效果。然而，这些方法尚未得到合理的系统梳理和总结，使得研究者难以理解当前的发展脉络。本文旨在填补这一空白，系统性地回答四个研究问题：(1) 已开发了哪些DL模型用于断层解释？(2) 使用了哪些数据集？(3) DL方法在断层解释中的优势是什么？(4) 存在哪些挑战和候选解决方案？

# Main Contribution / 主要贡献

1. **首个针对DL断层解释的系统性文献综述（SLR）**，覆盖2018-2022年发表的56篇论文，采用Kitchenham系统综述方法，具有可重复性。
2. **提出多维分类体系**：从计算机科学角度（DL任务类型、模型架构、输入维度、学习范式）和地球科学角度（直接/半直接/间接断层解释、地质目标）对文献进行系统分类。
3. **提出目标-模型分类（Target-Model Category）**：STSN（单目标单网络）、MTSN-MCC（多目标单网络-多类分类）、MTSN-MTL（多目标单网络-多任务学习）、STMN（单目标多网络）。
4. **系统汇总73个数据集**，统计公开可用性、标注情况、使用频率，发现仅3个野外数据集和4个合成数据集同时公开了数据和标签。
5. **识别12个挑战**，归为四类：数据相关（4个）、DL相关（3个）、评估相关（2个）、实际应用相关（3个），并系统梳理了候选解决方案。

# Method Overview / 方法概述

**系统综述方法**（遵循Kitchenham et al., 2007指南）：

1. **研究问题定义**（RQ1-4）：DL模型、数据集、优势、挑战
2. **检索策略**：7个数字图书馆（ACM、IEEE Xplore、ScienceDirect、Scopus、SpringerLink、Web of Science、SEG Digital Library），检索时间2012-2022年
3. **文献筛选**：721条初始记录 → 格式/语言过滤 → 去重 → 两轮人工筛选 → 质量评估 → 最终56篇研究论文 + 9篇辅助文献
4. **数据提取**：交叉验证提取DL模型、数据集、优势、挑战等信息
5. **数据分析**：按年份、出版类型、期刊、DL任务、模型架构、学习范式、地质目标等多维度统计分析

**分类体系**：
- **DL任务**：图像分割（60%）、图像分类（26.7%）、图像合成（6.7%）、实例分割（3.3%）、边缘检测（3.3%）
- **DL模型**：UNet变体（54%）、自定义CNN（17.5%）、VGG变体（7.9%）、GAN变体（6.3%）等
- **学习范式**：监督学习（83.9%）、迁移学习（12.5%）、无监督学习（3.5%）、知识蒸馏（1.8%）
- **目标-模型分类**：STSN（82%）、MTSN-MCC、STMN、MTSN-MTL

# Dataset and Evaluation / 数据集与评估

**数据集统计**：
- 共73个数据集（47个野外 + 26个合成），使用123次
- 仅3个野外数据集（LANDMASS、GSB、Thebe）和4个合成数据集（FaultSeg3D、Bi's 3D synthetic、Wu's 2D SR、Pochet's 2D synthetic）同时公开了数据和标签
- 公开标注的数据集使用频率是非公开的3.9倍
- 最受欢迎的合成数据集：Wu et al. (2019a) 的FaultSeg3D
- 最常用的野外数据集：F3（荷兰北海）

**评估方法**：
- 大多数论文使用Accuracy、Precision、Recall、F1
- 但存在评估标准不统一的问题，像素级Accuracy对不平衡分类不适用
- 部分论文采用带容忍距离的评估方法（如IoU with tolerance）

# Why This Paper Matters / 为什么关注这篇论文

**本文是DL断层解释领域的必读综述**，具有极高参考价值：
1. 全面覆盖2018-2022年所有重要工作，是领域研究的"地图"
2. 提出的分类体系（DL任务、模型、学习范式、目标-模型分类）可直接用于组织ResearchAI的知识体系
3. 识别的12个挑战为后续研究选题提供直接指导
4. 数据集汇总表可直接用于ResearchAI的论文索引和基准测试
5. 发表在Earth-Science Reviews（IF > 10），代表了领域权威共识

# Limitations / 局限性

1. 检索截止于2022年3月，不包含2022年后的最新进展（如ViT、大模型、扩散模型等）
2. 仅涵盖CNN方法，未涉及Transformer等方法（这些方法在2023年后才开始在断层检测中大量出现）
3. 对数据集的统计虽然全面，但未提供直接下载链接或标准化评估基准
4. 未提供定量比较（如统一的基准测试结果），仅有定性总结
5. 作为综述论文，本身不包含实验验证

# Reproducibility Status / 可复现性状态

> Literature Card: lightweight screening. Paper Note / Paper Logic: deep analysis.

## Code Availability

**Status**: [ ] Available [x] Not Found Yet (N/A - Survey paper) [ ] Confirmed Missing [ ] Not Checked

**URL**: <!-- Only fill when Status = Available -->

## Data Status / 数据可用性

- [x] **Public dataset available** — 综述使用公开文献数据
- [ ] **Restricted dataset** — requires application or license
- [ ] **Private dataset** — not publicly accessible
- [ ] **Unknown** — paper does not specify

**Dataset Link**: 论文中提供了各数据集的引用和公开链接

## Reproduction Feasibility / 复现可行性

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: 综述论文遵循Kitchenham系统综述方法，详细描述了检索策略、筛选标准、数据提取流程，理论上可完全复现。但部分数据集可能因时间推移而不再可访问。

**Notes / 备注**: 因为是综述论文，不涉及代码复现。

# My Decision / 我的决定

- [x] Read deeply / 精读
- [ ] Keep reference / 保留参考
- [ ] Ignore / 忽略

**Reason / 理由**: 领域必读综述，为ResearchAI的知识体系提供分类框架、挑战清单和基准数据集参考，是后续所有断层检测论文的定位基础。

# Related Knowledge / 相关知识链接

- Task: [[Survey]] [[Fault Interpretation]]
- Method: [[Systematic Literature Review]]
- Dataset: [[FaultSeg3D]] [[F3]] [[Thebe]]

## Zotero

**Zotero Item Key**: CZR5AZX9 (att), parent: PNK3T84P