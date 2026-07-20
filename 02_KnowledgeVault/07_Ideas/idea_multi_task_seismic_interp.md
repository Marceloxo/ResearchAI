---
idea_name: "Multi-Task Learning for Seismic Interpretation"
related_tasks: [Seismic Phase Picking, Phase Association, Earthquake Location, Seismic Facies Segmentation]
related_methods: [Multi-task Learning, PLAN, GENIE, EQTransformer]
status: active
tags: [multi-task-learning, joint-training, shared-representation, seismic-ai, research-idea]
created: 2026-07-20
---

# Idea Description / 想法描述

Several seismic papers demonstrate that joint training on related tasks improves performance: EQTransformer (detection + picking), PLAN (picking + association + location), GENIE (association + location). This principle — **shared encoder with task-specific decoders** — has not been systematically applied to seismic image interpretation tasks (fault + facies + salt simultaneously).

# Motivation / 动机来源

- **From Paper / 来自论文**: [[mousavi2020_eqtransformer_note]], [[si2024_plan_allinone_note]], [[mcbrearty2023_genie_note]]
- **From Method / 来自方法**: [[Multi-task Learning]], [[PLAN]], [[GENIE]], [[EQTransformer]]
- **From Experiment / 来自实验**: 
- **From Gap / 来自研究空白**: Seismic image segmentation treats fault, facies, and salt as separate tasks. No multi-task model exists.

# Problem / 问题

Seismic interpretation involves multiple correlated tasks (fault detection, facies classification, salt body segmentation) that are currently solved independently. This means:
- Encoder features are learned separately for each task (wasted computation)
- Cross-task relationships (e.g., faults often bound facies bodies) are not exploited
- Field deployment requires running N separate models

# Proposed Solution / 提出的解决方案

1. **Design a multi-task seismic interpretation network**: shared encoder (SegFormer/Transformer) + task-specific decoders for fault, facies, salt
2. **Evaluate task synergy**: does joint training improve individual task performance?
3. **Compare with single-task baselines**: is there a "free lunch" from multi-task learning?
4. **Test on multi-annotation datasets**: F3 Netherlands (has both facies and fault labels)

# Expected Contribution / 预期贡献

1. First multi-task model for comprehensive seismic interpretation (fault + facies + salt)
2. Quantitative analysis of task synergy in seismic deep learning
3. Compute-efficient alternative to running N separate models

# Related Knowledge / 相关知识

- Task: [[Seismic Facies Segmentation]], [[Fault Segmentation]], [[Seismic Image Segmentation]]
- Method: [[Multi-task Learning]], [[SegFormer]], [[PLAN]], [[GENIE]]
- Paper: [[mousavi2020_eqtransformer_note]], [[si2024_plan_allinone_note]], [[wang2024_segformer_seismic_facies_note]]

# Future Experiment Plan / 未来实验计划

- [ ] Step 1: Build shared encoder (SegFormer-MiT-B2) with 3 task-specific decoders
- [ ] Step 2: Train on F3 Netherlands (facies + fault labels available)
- [ ] Step 3: Compare: joint training vs. 3 independent models (total params, FLOPs, per-task accuracy)
- [ ] Step 4: Test generalization on Thebe (fault) + SEG Salt (salt) + Parihaka (facies)

**Target Dataset / 目标数据集**: [[F3 Netherlands]], [[Thebe]], [[SEG Salt]], [[Parihaka]]
**Baseline Methods / 基线方法**: 
- [[SegFormer]]
- [[U-Net]]
- [[CNN]]