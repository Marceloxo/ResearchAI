---
paper_title: "Deep Learning for Seismic Image Segmentation: A Survey and Benchmark"
target_venue: "IEEE Transactions on Geoscience and Remote Sensing"
status: outline
tags: [writing, survey, seismic-ai, segmentation]
created: 2026-07-20
---

# Research Story / 研究故事

Deep learning has transformed seismic image interpretation, but the field lacks a systematic survey that covers both methods (CNN, Transformer, GAN) and tasks (fault, facies, salt). This survey would provide the first comprehensive taxonomy, benchmark existing methods on common datasets, and identify research gaps for future work.

# Introduction Outline / 引言大纲

## Paragraph 1: Importance / 重要性

Seismic image interpretation is critical for hydrocarbon exploration, CO2 storage, and geothermal energy. Faults, facies, and salt bodies are the three primary interpretation targets.

## Paragraph 2: Existing Methods / 现有方法

Deep learning methods have been applied: U-Net for fault (wu2019), SegFormer for facies (wang2024), Vision Transformers for salt. However, these are scattered across different papers, datasets, and metrics.

## Paragraph 3: Research Gap / 研究空白

No unified benchmark exists. Each paper uses different datasets, metrics, and train/val/test splits. It is impossible to compare methods fairly.

## Paragraph 4: Our Approach / 我们的方法

We present the first comprehensive survey + benchmark: (1) taxonomy of seismic DL methods, (2) standardized evaluation protocol, (3) fair comparison of 10+ methods on 3 tasks, (4) research gap analysis.

## Contribution Statement / 贡献声明

1. First systematic taxonomy of deep learning for seismic image segmentation
2. Standardized benchmark with unified evaluation protocol
3. Fair comparison of 10+ architectures across 3 tasks (fault, facies, salt)
4. Identified research gaps and future directions

# Related Work Outline / 相关工作大纲

- **Topic 1: CNN-based seismic segmentation**
  - [[monteiro2024_deep_learning_survey]]
  - [[chai2020_using_note]]

- **Topic 2: Transformer-based seismic segmentation**
  - [[wang2024_segformer_seismic_facies_note]]
  - [[monteiro2024_deep_learning_survey]]

- **Topic 3: Multi-task learning for seismic interpretation**
  - [[mousavi2020_eqtransformer_note]]
  - [[si2024_plan_allinone_note]]

- **Topic 4: Transfer learning / domain adaptation**
  - [[chai2020_using_note]]
  - [[zhu2018_phasenet_note]]

# Method Outline / 方法大纲

## Overall Framework

Standardized evaluation protocol: same dataset splits, same preprocessing, same metrics.

## Key Components

### Component 1: Taxonomy

Hierarchical classification of methods: (1) CNN-based, (2) Transformer-based, (3) Hybrid, (4) GAN-based

### Component 2: Benchmark pipeline

Unified data loading, preprocessing, training, and evaluation scripts

## Loss Function

Standardized: Dice loss + Cross-entropy for all tasks

# Experiment Outline / 实验大纲

## Research Questions

- **RQ1**: Which architecture family performs best for seismic segmentation?
- **RQ2**: How does dataset size affect relative method rankings?
- **RQ3**: Do Transformer methods generalize better across datasets?

## Datasets

- [[F3 Netherlands]] (facies + fault)
- [[Thebe]] (fault)
- [[SEG Salt]] (salt)
- [[Parihaka]] (facies)
- [[Penobscot]] (facies)

## Baselines

- [[U-Net]]
- [[SegFormer]]
- [[U-SegFormer-Hyper]]
- [[CNN]]
- [[Vision Transformer]]
- [[Attention Mechanism]]

## Expected Results

Transformers should outperform CNNs on large datasets; CNNs may be competitive on small datasets. Multi-scale fusion (hypercolumn) should help across all architectures.

# Expected Contribution / 预期贡献

1. Comprehensive survey paper with ~50+ references
2. Open-source benchmark codebase
3. Pre-trained model weights for all methods

# Draft Progress / 写作进度

- [ ] Introduction
- [ ] Related Work
- [x] Method Taxonomy (from existing KnowledgeVault)
- [ ] Experiments
- [ ] Results
- [ ] Conclusion
- [ ] Abstract