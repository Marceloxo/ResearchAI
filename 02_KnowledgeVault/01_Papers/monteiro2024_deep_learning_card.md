---
title: "Literature Review on Deep Learning for the Segmentation of Seismic Images"
authors: [survey paper]
year: 2023
venue: "Survey/Review Journal"
task: ["Seismic Image Segmentation", "Fault Segmentation", "Salt Segmentation"]
method: ["CNN", "U-Net", "Transformer", "Attention Mechanism", "GAN"]
dataset: ["F3 Netherlands", "Thebe", "SEG Salt", "Marmousi"]
code_available: false
importance: high
reading_status: done
tags: [seismic-ai, segmentation, survey, key-paper, fault-segmentation, cnn, unet, transformer, attention]
created: 2026-07-08
---

# Basic Information / 鍩烘湰淇℃伅

- **Title**: Literature Review on Deep Learning for the Segmentation of Seismic Images
- **Authors**: Survey paper 鈥?multiple authors covering the field
- **Year**: 2023
- **Venue**: Survey/Review Journal
- **Task**: Seismic Image Segmentation (Fault Segmentation, Salt Segmentation, Facies Classification)
- **Method**: CNN, U-Net variants, Transformer, Attention Mechanisms, GAN, Hybrid Methods
- **Dataset**: F3 Netherlands, Thebe, SEG Salt, Marmousi, SEAM
- **Code**: Not applicable (survey paper)

# Research Problem / 鐮旂┒闂

How has deep learning been applied to seismic image segmentation? What are the key methods, datasets, and challenges in this field? This survey organizes and synthesizes the rapidly growing literature.

# Main Contribution / 涓昏璐＄尞

Provides a comprehensive taxonomy of deep learning methods for seismic image segmentation, covering tasks (fault, salt, facies), method families (CNN, U-Net, Transformer, GAN, Attention), datasets, and evaluation protocols. Serves as the entry-point survey for anyone entering this field.

# Method Overview / 鏂规硶姒傝堪

The survey organizes methods into families: (1) CNN-based (U-Net and its encoder-decoder variants dominate), (2) Attention-enhanced architectures, (3) Transformer-based methods (emerging trend), (4) GAN-based approaches for data augmentation and segmentation, (5) Hybrid methods combining multiple techniques.

# Dataset and Evaluation / 鏁版嵁闆嗕笌璇勪及

Key benchmarks: F3 Netherlands (fault interpretation with manual labels), Thebe (fault benchmark), SEG Salt (salt body identification), Marmousi (synthetic model), SEAM. Primary metrics: IoU, Dice coefficient, Precision, Recall, Pixel Accuracy.

# Why This Paper Matters / 涓轰粈涔堝叧娉ㄨ繖绡囪鏂?
This is the foundational survey for our primary research direction (Seismic AI). It provides the complete landscape: what tasks exist, which methods work, what datasets are available, and where the gaps are. Essential for orienting all future work.

# Limitations / 灞€闄愭€?
- Covers literature up to ~2022-2023; Transformer methods are still rapidly evolving.
- Survey format 鈥?no new experimental results or benchmarks.
- May not cover very recent foundation model approaches.
- Limited discussion of computational efficiency / lightweight models.

## Zotero

**Status**: Imported
**Item Key**: SGUIYBB2

# My Decision / 鎴戠殑鍐冲畾

- [x] Read deeply / 绮捐
- [ ] Keep reference / 淇濈暀鍙傝€?- [ ] Ignore / 蹇界暐

**Reason / 鐞嗙敱**: This is the entry-point survey for seismic AI segmentation. Every future paper we read will be mapped against the taxonomy established here. Essential for building the knowledge base structure.

# Related Knowledge / 鐩稿叧鐭ヨ瘑閾炬帴

- Task: [[Seismic Image Segmentation]], [[Fault Segmentation]]
- Method: [[CNN]], [[U-Net]], [[Transformer]], [[Attention Mechanism]]
- Dataset: [[F3 Netherlands]], [[Thebe]], [[SEG Salt]], [[Marmousi]]
- Topic: [[Seismic AI]]

