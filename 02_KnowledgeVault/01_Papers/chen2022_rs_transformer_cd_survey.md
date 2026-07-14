---
title: "Remote Sensing Image Change Detection With Transformers"
authors: [Chen et al.]
year: 2022
venue: "IEEE Transactions on Geoscience and Remote Sensing"
task: [Change Detection]
methods: ["Transformer", "Vision Transformer", "Self-Attention", "Siamese Network"]
datasets: ["LEVIR-CD", "DSIFN-CD", "WHU-CD"]
metrics: ["F1 Score", "Precision", "Recall", "OA"]
code: "Not specified"
importance: high
status: done
paper_type: survey
tags: [change-detection, transformer, remote-sensing, survey, chen]
created: 2026-07-10
---

# Paper Type

**Survey / Review Paper** —Reviews transformer-based methods for remote sensing image change detection.

# One Sentence Summary

Systematic survey of transformer applications in remote sensing change detection, categorizing methods by architecture design, attention mechanisms, and application domains.

# Research Landscape

## Domain: Transformer + Remote Sensing Change Detection

Modern change detection has achieved remarkable success through deep convolutions. However, high-resolution RS change detection remains challenging due to object complexity, intra-class variation, and contextual ambiguity. Transformers offer powerful discriminative ability through self-attention mechanisms.

# Taxonomy

## Task Taxonomy

1. **Binary Change Detection**: Change vs. no-change pixel classification
2. **Semantic Change Detection**: Per-class change identification
3. **Multi-temporal Change Detection**: More than two time points
4. **Coarse-to-Fine Change Detection**: Region-level then pixel-level

## Method Taxonomy

1. **Pure Transformer**: Full ViT architecture adapted for bi-temporal image pairs
2. **Transformer-CNN Hybrid**: CNN backbone with transformer attention modules
3. **Siamese Transformer**: Dual-encoder transformers with cross-attention for change modeling
4. **Lightweight Transformer**: Reduced attention complexity for RS image scale

## Dataset Taxonomy

1. **LEVIR-CD**: Urban building change detection, 637 image pairs
2. **DSIFN-CD**: Dense settlement change detection, multi-scale
3. **WHU-CD**: Aerial image change detection, high resolution
4. **CDD**: Road change detection dataset

# Key Findings

1. Self-attention excels at capturing long-range dependencies in bi-temporal images
2. Hybrid CNN-Transformer architectures balance local feature extraction and global context
3. Transformer methods generally outperform pure CNN methods but at higher computational cost
4. Cross-attention mechanisms are particularly effective for modeling change relationships

# Future Research Directions

1. **Efficient Transformers**: Reducing quadratic attention complexity for large RS images
2. **Self-supervised Pre-training**: Leveraging unlabeled bi-temporal data
3. **Multi-modal Change Detection**: Beyond optical (SAR, hyperspectral fusion)
4. **Foundation Models for RS**: General-purpose change detection models

# My Analysis

## Transferable Insights

- Transformer attention mechanisms for seismic image change detection
- Siamese architecture design patterns applicable to seismic monitoring
- Survey provides taxonomy of CD methods that can inform model selection

## Relevance to Current Research

> Remote sensing change detection shares core challenges with seismic image segmentation: pixel-level prediction, handling complex textures, and managing class imbalance. Transformer-based CD methods offer transferable architecture patterns.

# Related Notes

- Topic: [[Seismic AI]]
- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[Transformer]], [[Vision Transformer]], [[Attention Mechanism]]
- Dataset: [[F3 Netherlands]], [[Marmousi]]


# Zotero

- **Status**: Imported
- **Item Key**: 46C4TYYR