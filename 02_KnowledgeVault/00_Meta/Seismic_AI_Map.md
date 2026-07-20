---
tags: [meta, seismic-ai, navigation]
created: 2026-07-08
---

# Seismic AI Map / 地震AI研究地图

Current primary research direction. This map organizes seismic AI research by tasks, methods, and datasets.

---

## Tasks / 任务

### Seismic Phase Picking / 震相拾取

- [[Seismic Phase Picking]]

### Phase Association / 震相关联

- [[Phase Association]]

### Earthquake Location / 地震定位

- [[Earthquake Location]]

### Earthquake Sequence Analysis / 地震序列分析

- [[Earthquake Sequence Analysis]]

### Fault Segmentation / 断层分割

Identify and delineate geological faults in seismic images.

- [[Fault Segmentation]]

### Seismic Denoising / 地震数据去噪

Remove noise from seismic data while preserving geological structures.

- [[Seismic Denoising]]

### Seismic Imaging / 地震成像

Reconstruct subsurface images from seismic acquisition data.

- [[Seismic Imaging]]

### Seismic Inversion / 地震反演

Estimate subsurface physical properties from seismic data.

- [[Seismic Inversion]]

### Other Tasks

- [[Seismic Interpretation]] — Comprehensive interpretation of seismic volumes
- [[Seismic Reconstruction]] — Reconstruct missing or corrupted seismic traces

---

## Methods / 方法

### CNN-Based / 卷积神经网络

- [[CNN]]
- [[U-Net]]
- [[ResNet]]

### Transformer-Based / Transformer方法

- [[Transformer]]
- [[Vision Transformer]]
- [[Swin Transformer]]
- [[SegFormer]]
- [[U-SegFormer-Hyper]]

### GNN-Based / 图神经网络

- [[GENIE]] — GNN-based phase association
- [[PLAN]] — Multi-task multi-station GNN

### Frequency Domain / 频域方法

- [[Frequency Domain Learning]]
- [[Fourier Neural Operator]]

### Attention Mechanisms / 注意力机制

- [[Attention Mechanism]]
- [[Self-Attention]]
- [[Channel Attention]]

---

## Datasets / 数据集

### Fault Detection

- [[DeepFault]]
- [[Thebe]]
- [[F3 Netherlands]]

### Full Waveform Inversion

- [[OpenFWI]]
- [[SEG Salt]]

### General Seismic

- [[SEAM]]
- [[Marmousi]]

---

## Key Papers / 关键论文

### Seismic Phase Picking

- [[zhu2018_phasenet_note]] — PhaseNet (2018)
- [[mousavi2020_eqtransformer_note]] — EQTransformer (2020)
- [[chai2020_using_note]] — Transfer learning for PhaseNet (2020)

### Seismic Facies Segmentation

- [[wang2024_segformer_seismic_facies_note]] — U-SegFormer-Hyper (2024)

### Multi-task Earthquake Monitoring

- [[si2024_plan_allinone_note]] — PLAN (2024)
- [[mcbrearty2023_genie_note]] — GENIE (2023)

### Surveys

- [[monteiro2024_deep_learning_survey]] — DL for seismic segmentation (2024)
- [[mousavi2023_machine_learning_survey]] — ML in seismology (2023)

---

## Active Research Ideas / 活跃研究想法

- [[idea_transfer_learning_seismic]] — Transfer learning across scales for seismic DL
- [[idea_multi_task_seismic_interp]] — Multi-task learning for seismic interpretation
- [[idea_transformer_seismic_arch]] — Transformer architectures for seismic segmentation
- [[idea_self_supervised_seismic]] — Self-supervised pre-training for seismic DL

## Planned Experiments / 计划实验

- [[exp_phasenet_repro]] — PhaseNet baseline reproduction
- [[exp_eqtransformer_repro]] — EQTransformer baseline reproduction
- [[exp_chai2020_phase_picking]] — Transfer learning validation

## Writing / 写作

- [[writing_seismic_seg_survey]] — DL for seismic segmentation survey

---

## Navigation / 导航

- Back to [[Research_Map]]
- Back to [[Home]]
- Explore [[Method_Map]]
- Explore [[Dataset_Map]]
- Explore [[Idea_Index]]
- Explore [[Experiment_Index]]

## Added in Stage 6.5.2 / 已合并到上方分类

<!-- These nodes have been merged into the main taxonomy sections above. -->
