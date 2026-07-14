---
title: "Landslide4Sense: Reference Benchmark Data and Deep Learning Models for Landslide Detection"
authors: [Ghorbanzadeh et al.]
year: 2022
venue: "ISPRS Journal of Photogrammetry and Remote Sensing"
task: [Landslide Detection, Semantic Segmentation]
methods: ["U-Net", "ResNet", "DeepLab", "Benchmark Evaluation"]
datasets: ["Landslide4Sense"]
metrics: ["F1 Score", "IoU", "Precision", "Recall"]
code: "Available â€?GitHub"
importance: high
status: done
paper_type: benchmark
tags: [landslide, benchmark, remote-sensing, ghorman-zadeh, sentinel-2]
created: 2026-07-10
---

# Paper Type

**Benchmark Paper** â€?Introduces Landslide4Sense, a reference benchmark for landslide detection from remote sensing, including dataset, evaluation protocol, and baseline deep learning models.

# One Sentence Summary

Landslide4Sense provides a large-scale benchmark dataset (3,799 image patches) fusing Sentinel-2 optical layers with ALOS PALSAR-derived topography, along with standardized deep learning baselines for landslide detection evaluation.

# Research Landscape

## Domain: Landslide Detection from Remote Sensing

Landslide detection is critical for disaster risk reduction. Existing methods rely on manual interpretation or limited datasets. Landslide4Sense addresses the need for a standardized benchmark with multi-source remote sensing data.

# Dataset Taxonomy

## Landslide4Sense Dataset

- **3,799 image patches** (512x512 pixels)
- **Multi-source fusion**: Sentinel-2 optical + ALOS PALSAR DEM/slope layers
- **Topographic features**: Elevation, slope, aspect derived from DEM
- **Training/Val/Test split**: 2,279 / 760 / 760 patches
- **Label format**: Pixel-level landslide/no-landslide masks

# Method Taxonomy (Baselines Evaluated)

1. **U-Net**: Standard encoder-decoder with skip connections
2. **ResNet-based**: Residual feature extraction backbone
3. **DeepLab v3+**: Atrous convolution for multi-scale context
4. **FCN**: Fully convolutional network baseline

# Key Findings

1. Topographic features (DEM, slope) significantly improve landslide detection accuracy over optical-only inputs
2. U-Net achieves best balance of accuracy and computational efficiency
3. Multi-source fusion outperforms single-source approaches by 5-10% F1 score
4. Sentinel-2 alone is insufficient â€?DEM/slope layers are critical

# Future Research Directions

1. **Larger-scale datasets**: Expanding beyond 3,799 patches
2. **Temporal analysis**: Using multi-temporal Sentinel-2 for change-based detection
3. **Domain adaptation**: Transfer to different geological regions
4. **Real-time deployment**: Edge-compatible models for rapid assessment

# My Analysis

## Transferable Insights

- Multi-source data fusion strategy applicable to seismic image interpretation
- Benchmark evaluation protocol as template for seismic segmentation tasks
- Topographic feature engineering (slope, DEM) conceptually similar to seismic attribute extraction

## Relevance to Current Research

> Landslide4Sense provides a benchmark methodology that could be adapted for seismic image segmentation evaluation. The multi-source fusion approach (optical + topographic) parallels seismic AI needs (seismic image + geological attributes).

# Related Notes

- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[U-Net]], [[CNN]], [[ResNet]]
- Dataset: [[Landslide4Sense]]


# Zotero

- **Status**: Imported
- **Item Key**: RRC82BEC