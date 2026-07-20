---
idea_name: "Transfer Learning Across Scales for Seismic Deep Learning"
related_tasks: [Seismic Phase Picking, Seismic Image Segmentation, Fault Segmentation]
related_methods: [PhaseNet, Transfer Learning, CNN]
status: active
tags: [transfer-learning, domain-adaptation, seismic-ai, research-idea]
created: 2026-07-20
---

# Idea Description / 想法描述

PhaseNet (zhu2018) demonstrated that a U-Net trained on one region (NCEDC) can be transferred to another (EGS Collab SURF) with only 0.45% of original training data (chai2020). This principle — **transfer learning across 3 orders of magnitude scale difference** — has not been systematically explored for seismic image segmentation tasks.

# Motivation / 动机来源

- **From Paper / 来自论文**: [[zhu2018_phasenet_note]], [[chai2020_using_note]]
- **From Method / 来自方法**: [[PhaseNet]], [[Transfer Learning]]
- **From Experiment / 来自实验**: [[exp_chai2020_phase_picking]]
- **From Gap / 来自研究空白**: Current seismic image segmentation models are trained and evaluated on the same dataset. No cross-dataset transfer benchmark exists.

# Problem / 问题

Current seismic DL models (fault segmentation, facies classification) are trained per-dataset. This means:
- Each new survey area requires full retraining
- No pre-trained foundation model exists for seismic interpretation
- Small datasets (e.g., Thebe, Penobscot) cannot benefit from large ones (e.g., F3 Netherlands)
- Annotation effort is duplicated across projects

# Proposed Solution / 提出的解决方案

1. **Benchmark cross-dataset transfer** for seismic image segmentation: pre-train on F3 Netherlands, fine-tune on Thebe/Parihaka/Penobscot
2. **Evaluate minimal fine-tuning data threshold**: how few labeled sections are needed?
3. **Compare domain adaptation strategies**: fine-tuning vs. adversarial adaptation vs. self-supervised pre-training
4. **Extend to 3D**: test whether 2D pre-trained models transfer to 3D volumes

# Expected Contribution / 预期贡献

1. First systematic cross-dataset transfer benchmark for seismic image segmentation
2. Practical guidelines for minimal annotation requirements
3. Pre-trained model checkpoint for seismic interpretation

# Related Knowledge / 相关知识

- Task: [[Seismic Image Segmentation]], [[Seismic Phase Picking]], [[Fault Segmentation]]
- Method: [[PhaseNet]], [[Transfer Learning]], [[CNN]]
- Paper: [[zhu2018_phasenet_note]], [[chai2020_using_note]]

# Future Experiment Plan / 未来实验计划

- [ ] Step 1: Pre-train SegFormer/U-Net on F3 Netherlands facies dataset
- [ ] Step 2: Fine-tune on Thebe (fault) with varying labeled data ratios (100%, 50%, 25%, 10%, 5%)
- [ ] Step 3: Evaluate domain gap: compare same-architecture trained from scratch vs. transferred
- [ ] Step 4: Extend to 3D volumes (SEAM, SEG Salt)

**Target Dataset / 目标数据集**: [[F3 Netherlands]], [[Thebe]], [[Parihaka]], [[Penobscot]]
**Baseline Methods / 基线方法**: 
- [[U-Net]]
- [[SegFormer]]
- [[CNN]]