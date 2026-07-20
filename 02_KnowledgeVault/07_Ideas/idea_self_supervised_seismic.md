---
idea_name: "Self-Supervised Pre-Training for Seismic Deep Learning"
related_tasks: [Seismic Phase Picking, Seismic Facies Segmentation, Fault Segmentation, Seismic Image Segmentation]
related_methods: [CNN, Transformer, Transfer Learning, Attention Mechanism]
status: exploring
tags: [self-supervised-learning, pre-training, seismic-ai, foundation-model, research-idea]
created: 2026-07-20
---

# Idea Description / 想法描述

Multiple papers note that "self-supervised pre-training on unlabeled seismic data" could reduce annotation requirements (mousavi2020, zhu2018). In NLP/vision, masked autoencoding (MAE, BERT) has revolutionized pre-training. **Can we build a seismic foundation model via self-supervised learning on large unlabeled seismic volumes?**

# Motivation / 动机来源

- **From Paper / 来自论文**: [[mousavi2020_eqtransformer_note]], [[zhu2018_phasenet_note]], [[wang2024_segformer_seismic_facies_note]]
- **From Method / 来自方法**: [[Transfer Learning]], [[CNN]], [[Transformer]]
- **From Gap / 来自研究空白**: No seismic foundation model exists. All seismic DL models train from scratch per dataset.

# Problem / 问题

- Labeled seismic data is scarce (especially for fault/facies)
- Each new survey area requires manual annotation
- Pre-training on ImageNet is not optimal for seismic (different feature distribution)
- Existing models do not benefit from the vast amount of unlabeled seismic data

# Proposed Solution / 提出的解决方案

1. **Pre-train a masked autoencoder (MAE)** on large unlabeled seismic volumes (F3, Parihaka, SEAM, Marmousi)
2. **Fine-tune on downstream tasks** (facies, fault, salt) with varying labeled data ratios
3. **Compare with ImageNet pre-training and scratch training**
4. **Evaluate: does seismic-specific pre-training outperform ImageNet transfer?**

# Expected Contribution / 预期贡献

1. First seismic foundation model pre-trained via self-supervised learning
2. Quantitative comparison: SSL pre-training vs. ImageNet transfer vs. scratch
3. Pre-trained checkpoint released for community

# Related Knowledge / 相关知识

- Task: [[Seismic Facies Segmentation]], [[Fault Segmentation]], [[Seismic Image Segmentation]]
- Method: [[Transformer]], [[Transfer Learning]], [[CNN]]
- Paper: [[wang2024_segformer_seismic_facies_note]], [[monteiro2024_deep_learning_survey]]

# Future Experiment Plan / 未来实验计划

- [ ] Step 1: Collect unlabeled seismic data (F3, Parihaka, Penobscot, SEAM, Marmousi — ~500M+ pixels)
- [ ] Step 2: Implement MAE pre-training with ViT-Small backbone
- [ ] Step 3: Fine-tune on F3 facies (1%, 5%, 10%, 50%, 100% labeled)
- [ ] Step 4: Compare with ImageNet-initialized and scratch baselines

**Target Dataset / 目标数据集**: [[F3 Netherlands]], [[Parihaka]], [[Penobscot]], [[SEAM]], [[Marmousi]]
**Baseline Methods / 基线方法**: 
- [[U-Net]]
- [[SegFormer]]
- [[Vision Transformer]]