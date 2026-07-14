---
title: "DTPP: An efficient depthwise separable TCN for seismic phase picking"
authors: [Shuai Lv, Yuxiang Peng]
year: 2026
venue: "Computers & Geosciences"
task: [Seismic Phase Picking]
methods: [Depthwise Separable Convolution, Temporal Convolutional Network, Dilated Convolution, ASPP, Residual Connections, DeepLabV3+ Inspired Encoder-Decoder]
datasets: [STEAD, GEEDataset V1.0]
metrics: [Precision, Recall, F1 (0.1s tolerance), Error Statistics (mu, sigma, MAE at 0.5s), Inference Speed, Parameter Count]
code: ""
importance: medium
status: deep-read
paper_type: research_article
tags: [seismic-phase-picking, depthwise-separable-convolution, temporal-convolutional-network, dilated-convolution, stead, geedataset, real-time-monitoring, lightweight-model]
created: 2026-07-10
---

# Paper Type / Research Article

This paper proposes a novel lightweight deep learning architecture for seismic phase picking that achieves state-of-the-art accuracy-efficiency trade-off.

---

# One Sentence Summary

DTPP is a 0.25M-parameter encoder-decoder network combining depthwise separable convolution and dilated convolution (inspired by DeepLabV3+) that achieves the highest average P/S F1 score (0.714) on GEEDataset V1.0 while maintaining ~3ms inference time per sample.

---

# Research Background

Seismic phase picking is the crucial first step in real-time seismic data processing workflows, directly impacting downstream processes like earthquake location and magnitude estimation. With the rise of deep learning, numerous models have emerged (GPD, PhaseNet, EQTransformer, LPPN, SeisT, PickerXL, SeisLM), each offering different trade-offs between accuracy and efficiency.

Two fundamental tensions exist:
1. **Accuracy vs. Efficiency**: Transformer-based models (SeisLM: 87M params) achieve high accuracy but suffer from slow inference (57ms/sample); classical CNNs (PhaseNet) are fast but have limited receptive fields.
2. **Receptive Field vs. Computational Cost**: Traditional CNNs grow receptive fields linearly through layer stacking, requiring more parameters; Transformers require large training data and have quadratic complexity.

For real-time seismic monitoring at scale, a model must simultaneously achieve: high picking accuracy, fast inference (<10ms), small parameter count, and robust generalization across datasets.

---

# Problem Definition

- **Input**: Three-component seismic waveform data (60s windows, 100 Hz sampling rate, 3000 sampling points per component)
- **Output**: Point-wise three-class probability distribution (P, S, noise) for each sampling point

---

# Motivation

Existing methods face inherent architectural limitations:

1. **Standard CNNs** (PhaseNet): Receptive field grows linearly with layer depth. For P-S wave intervals spanning several seconds, many layers are needed, increasing parameters and computation.
2. **Transformers** (EQTransformer, SeisLM): Excellent generalization but heavy (0.38M to 87M params), slow inference (11-57ms), and require large training data.
3. **Multi-task models** (SeisT): Improve generalization via knowledge aggregation but introduce computational bottlenecks in self-attention.
4. **Sample interval methods** (LPPN): Fast processing but sacrifice accuracy through coarser temporal resolution.

The paper identifies that **dilated convolution** (used in DeepLab for semantic segmentation) and **depthwise separable convolution** (used in MobileNet for efficiency) have not been systematically combined for seismic phase picking. The "skip observation" mechanism of dilated convolution could exponentially expand the receptive field without adding parameters, while depthwise separable convolution could reduce computational load by ~65%.

---

# Main Contributions

1. **Novel Architecture**: Proposes DTPP, a lightweight encoder-decoder network integrating depthwise separable convolution and temporal dilated convolution, achieving exponential receptive field expansion with minimal parameter overhead.
2. **Seismic-Specific Module Design**: Designs SeismicBackbone (6 ETB modules with progressive dilation rates [2,4,8]) and SeismicASPP (adapted from DeepLabV3+ with dilation rates [6,12,18] aligned to typical P-S wave intervals) for 1-D seismic waveform processing.
3. **State-of-the-Art Accuracy-Efficiency Balance**: Achieves P-wave F1=0.878 and average P/S F1=0.714 (best among 7 baselines on GEEDataset V1.0) with only 0.25M parameters and ~3ms inference time, outperforming both classical CNNs and heavy Transformer models.

---

# Method

## Overall Framework

DTPP follows an encoder-decoder architecture inspired by DeepLabV3+, adapted for 1-D seismic waveforms:

```
Input (3 x 3000) -> Stem Block -> SeismicBackbone (Encoder) -> SeismicASPP -> Decoder -> Output (3 x 3000)
                                              |
                                              +---> Skip Connection to Decoder (Encoder3 shallow features)
```

Four main components:
1. **Stem Block**: Initial convolution operations (7x1 + 3x1) extracting low-level features
2. **SeismicBackbone**: 6 serial ETB modules for multi-scale feature extraction with progressive downsampling
3. **SeismicASPP**: 5-branch parallel module for multi-scale contextual modeling
4. **Decoder**: Fuses deep features (ASPP) with shallow features (Encoder3 skip connection), upsamples to original resolution

## Key Modules

### ETB (Efficient TCN Block)

Combines depthwise separable convolution, dilated convolution, and residual connections:

**Depthwise convolution**: Separates spatial and channel-wise operations
$$Z = \sigma(BN(W_{dw} \otimes X))$$

**Pointwise convolution**: Channel transformation
$$Y_{main} = Dropout(\sigma(BN(W_{pw} * Z)))$$

**Residual branch**: Ensures gradient flow
$$Y_{res} = \begin{cases} X, & C_{in} = C_{out} \& s = 1 \\ BN(W_{res} * X), & \text{otherwise} \end{cases}$$

**Combined output**:
$$Y = Y_{main} + Y_{res}$$

Computational efficiency improvement factor:
$$\eta = \frac{P_{std}}{P_{dp}} = \frac{K \times C_{out}}{K + C_{out}}$$

With K=3, C_out=96: **~65% reduction** in computational load vs. standard convolution.

### SeismicBackbone

Six ETB modules with progressive downsampling (stride=2 for first 3 layers) and increasing dilation rates (2, 4, 8 for last 3 layers):

| Layer | Input Chn | Output Chn | Kernel | Stride | Dilation | Feature Dim |
|-------|-----------|------------|--------|--------|----------|-------------|
| ETB-1 | 48 | 48 | 3 | 2 | 1 | 48x1500 |
| ETB-2 | 48 | 96 | 3 | 2 | 1 | 96x750 |
| ETB-3 | 96 | 96 | 3 | 2 | 1 | 96x375 |
| ETB-4 | 96 | 96 | 3 | 1 | 2 | 96x375 |
| ETB-5 | 96 | 96 | 3 | 1 | 4 | 96x375 |
| ETB-6 | 96 | 96 | 3 | 1 | 8 | 96x375 |

Encoder3 serves as the skip connection point, preserving shallow phase boundary information.

### SeismicASPP

Adapted from DeepLabV3+ for 1-D seismic data with 5 parallel branches:

| Branch | Type | Kernel | Stride | Dilation | Purpose |
|--------|------|--------|--------|----------|---------|
| 1 | 1x1 Conv | 1 | 1 | 1 | Preserve local features |
| 2 | DW Conv | 3 | 1 | 6 | Small P-S interval |
| 3 | DW Conv | 3 | 1 | 12 | Medium P-S interval |
| 4 | DW Conv | 3 | 1 | 18 | Large P-S interval |
| 5 | Global Pool | 1 | 1 | - | Global context |

Outputs concatenated (120 channels) then fused through 3x1 convolution to 96 channels. Achieves **6579 sampling point receptive field** (covering ~65s at 100Hz), exceeding the 60s input window.

### Decoder

Fuses ASPP deep features (96 chn) with Encoder3 shallow features (96 chn):
1. Low-level projection: 96 -> 48 channels
2. Refine 1: Concatenated (144 chn) -> 96 channels
3. Refine 2: 96 -> 48 channels
4. Output classification head: 48 -> 3 classes (P, S, noise)
5. Upsample via linear interpolation to 3 x 3000

### Training Configuration

- **Optimizer**: AdamW (lr=1e-3, weight_decay=1e-4)
- **Scheduler**: Cosine annealing (min lr=1e-6)
- **Gradient clipping**: Max norm 1.0
- **Loss**: Vector Cross Entropy (for temporal label prediction)
- **Batch size**: 1024
- **Epochs**: 200
- **Hardware**: 4x NVIDIA Tesla V100-32GB (Data Parallel)
- **Data augmentation**: Random amplitude scaling, random Gaussian noise
- **Strategy**: Memory preloading to avoid I/O bottleneck

---

# Dataset

| Dataset | Purpose | Samples | Stations | Distance Range | Sampling Rate |
|---------|---------|---------|----------|----------------|---------------|
| STEAD | Training (8:1:1 split) | ~1,050,000 | 2,613 | 0-350 km | 100 Hz |
| GEEDataset V1.0 | Evaluation (cross-dataset) | 92,219 total, 84,782 after STEAD removal | Multi-source | ~0-100 km | 100 Hz |

GEEDataset V1.0 composition: NCEDC (35.92%), NCEDC (17.42%), IPGP (1.83%), NOA (36.76%), STEAD (8%). The 8% STEAD overlap was removed (7,437 waveforms) to ensure fair cross-dataset evaluation. Labels manually verified by experienced seismologists.

---

# Experimental Setup

**Evaluation metrics**:
- **Precision/Recall/F1**: At delta-t=0.1s tolerance (10 sampling points at 100Hz)
- **Error statistics**: Mean (mu), Std Dev (sigma), MAE at 0.5s range (following PhaseNet convention)
- **Inference efficiency**: Single-sample inference time (batch=1), throughput (batch=1024), parameter count, GPU memory

**Baseline models** (all evaluated with official pre-trained weights, no retraining):
- PhaseNet (NCEDC-trained)
- EQTransformer (STEAD-trained)
- LPPN (STEAD-trained)
- SeisT (DiTing-trained, no STEAD version available)
- PickerXL (STEAD-trained)
- SeisLM (STEAD-trained)
- **DTPP** (STEAD-trained)

All models tested on identical hardware: Tesla V100-PCIE-32GB, Intel Xeon Gold 6230 (4x), 512GB DDR4.

---

# Results

## Performance Comparison on GEEDataset V1.0 (0.1s tolerance)

| Model | Training | P-Prec | P-Rec | P-F1 | S-Prec | S-Rec | S-F1 | Avg F1 |
|-------|----------|--------|-------|------|--------|-------|------|--------|
| PhaseNet | NCEDC | 0.718 | 0.793 | 0.754 | 0.449 | 0.497 | 0.471 | 0.613 |
| EQTransformer | STEAD | 0.672 | 0.643 | 0.657 | 0.537 | 0.491 | 0.513 | 0.585 |
| LPPN | STEAD | 0.860 | 0.825 | 0.842 | 0.609 | 0.557 | 0.582 | 0.712 |
| SeisT | DiTing | 0.812 | 0.807 | 0.810 | 0.524 | 0.462 | 0.491 | 0.650 |
| PickerXL | STEAD | 0.836 | 0.838 | 0.837 | 0.563 | 0.563 | 0.563 | 0.563 |
| SeisLM | STEAD | 0.749 | 0.725 | 0.737 | 0.452 | 0.503 | 0.477 | 0.607 |
| **DTPP** | **STEAD** | **0.878** | **0.877** | **0.878** | **0.551** | **0.550** | **0.551** | **0.714** |

**DTPP achieves the highest average P/S F1 score (0.714)**, marginally ahead of LPPN (0.712). P-wave F1 (0.878) is the best among all models.

## Error Statistics (0.5s range)

| Model | P-mu | P-sigma | P-MAE | S-mu | S-sigma | S-MAE |
|-------|------|---------|-------|------|---------|-------|
| PhaseNet | -0.038 | 0.078 | 0.053 | -0.105 | 0.155 | 0.135 |
| EQTransformer | -0.007 | 0.032 | 0.009 | -0.087 | 0.154 | 0.129 |
| LPPN | -0.030 | 0.080 | 0.050 | -0.030 | 0.150 | 0.110 |
| SeisT-L | 0.006 | 0.078 | 0.054 | 0.005 | 0.168 | 0.129 |
| PickerXL | -0.021 | 0.070 | 0.044 | -0.064 | 0.158 | 0.121 |
| SeisLM | -0.047 | 0.090 | 0.064 | -0.075 | 0.169 | 0.136 |
| **DTPP** | **0.003** | **0.042** | **0.032** | **0.011** | **0.051** | **0.043** |

**DTPP achieves the best error statistics for both P and S waves**: lowest P-MAE (0.032s), lowest S-MAE (0.043s), lowest P-sigma (0.042s), lowest S-sigma (0.051s). Near-zero bias (mu) indicates no systematic timing offset.

## Inference Efficiency

| Model | Inference Time (ms) | Throughput (samples/s) | Parameters (MB) | GPU Memory (MB) |
|-------|---------------------|----------------------|-----------------|-----------------|
| PhaseNet | 5.54 | 180.52 | 0.27 | 3.01 |
| EQTransformer | 11.40 | 87.69 | 0.38 | 25.86 |
| LPPN | 3.08 | 324.41 | 0.04 | 2.29 |
| SeisT-L | 22.97 | 43.53 | 0.66 | 20.53 |
| PickerXL | 2.59 | 385.22 | 4.28 | 1.36 |
| SeisLM | 57.42 | 17.41 | 87.0 | 174.20 |
| **DTPP** | **2.99** | **333.77** | **0.25** | **4.41** |

DTPP ranks **second fastest** (2.99ms, behind PickerXL's 2.59ms) while being **third smallest** in parameters (0.25MB, behind LPPN 0.04MB and PhaseNet 0.27MB). The accuracy-efficiency Pareto frontier position is superior to all competitors.

---

# Ablation Study (STEAD dataset)

| Module | Replacement | Parameters | P-F1 | Delta | S-F1 | Delta | Avg F1 | Delta |
|--------|------------|------------|------|-------|------|-------|--------|-------|
| ETB | CNN | 329,283 | 0.9627 | -0.0028 | 0.8375 | -0.0048 | 0.9001 | -0.0038 |
| ASPP | CNN | 237,985 | 0.9607 | -0.0048 | 0.8337 | -0.0086 | 0.8972 | -0.0067 |
| Decoder | Only Deep Feature | 222,209 | 0.9613 | -0.0042 | 0.8389 | -0.0034 | 0.9001 | -0.0038 |
| **Original** | **-** | **258,097** | **0.9655** | **-** | **0.8423** | **-** | **0.9039** | **-** |

**Key findings**:
- ASPP replacement causes the largest performance drop (avg F1 -0.67%), confirming multi-scale feature modeling is the most critical component
- ETB and Decoder replacements cause smaller but still significant drops (-0.38% each)
- The original model achieves the best balance of accuracy and parameter efficiency

---

# Hyperparameter Optimization (STEAD dataset)

Top configurations tested (12 trials):

| Trial | ASPP Dilations | Backbone Dilations | Skip Connection | Global Context | Fusion Method | Avg F1 |
|-------|---------------|-------------------|-----------------|----------------|---------------|--------|
| 1 | [6,12,18] | [2,4,8] | Encoder2 | Yes | Concat | 0.9021 |
| 4 | [6,12,18] | [1,2,4] | Encoder2 | Yes | Concat | 0.9584 |
| 5 | [6,12,18] | [4,8,16] | Encoder2 | Yes | Concat | **0.9753** |
| 7 | [6,12,18] | [2,4,8] | **Encoder3** | Yes | Concat | **0.9755** |
| 8 | [6,12,18] | [2,4,8] | Encoder2 | No | Concat | 0.9725 |
| 9 | [6,12,18] | [2,4,8] | Encoder2 | Yes | Add | 0.9040 |
| 10 | [6,12,18] | [2,4,8] | Encoder2 | Yes | Attention | 0.8610 |

**Optimal configuration**: ASPP dilations=[6,12,18], backbone dilations=[2,4,8], skip from Encoder3, Concat fusion.

Key insights:
- Backbone dilation rates have the most significant impact ([4,8,16] outperforms [2,4,8] and [1,2,4])
- Skip from Encoder3 (rather than Encoder1/2) yields the best F1 (0.9755 vs 0.9753)
- Simple Concat fusion outperforms Add (0.904) and Attention (0.861)
- Global context modeling provides modest but consistent benefit

---

# Limitation

1. **S-wave detection weakness**: S-F1=0.551, lower than LPPN (0.582) and PickerXL (0.563). Particularly vulnerable in low SNR environments where S-wave energy is weaker and more dispersed.
2. **Distance limitation**: Tested only on epicentral distances <= 100 km. Performance at greater distances (>100 km) requires validation, as seismic waveforms at larger distances exhibit different frequency content and attenuation patterns.
3. **No continuous data validation**: Evaluated only on pre-segmented earthquake waveforms. Real-time monitoring systems must handle continuous streams with signal density, overlapping events, and ambient noise conditions that differ significantly from isolated event windows.
4. **Code not yet available**: Paper states "will be made available upon publication," preventing immediate reproducibility assessment.
5. **Atypical signals**: Performance on extreme noise, unusual seismic signals, or events outside the training distribution (different tectonic settings, deeper sources) untested.

---

# My Analysis

## Transferable Ideas

1. **Seismic-specific ASPP adaptation**: The dilation rate design [6, 12, 18] aligned with typical P-S wave intervals is a principled approach that could transfer to other 1-D temporal signal processing tasks where multi-scale context is needed (e.g., fault segmentation, microseismic detection).
2. **Skip observation mechanism**: The dilated convolution "skip sampling" concept for expanding receptive field exponentially could inspire architectures in other seismology tasks beyond phase picking.
3. **Depthwise separable as implicit regularization**: The paper notes that depthwise separable convolution reduces capacity, acting as implicit regularization against overfitting. This is an underexplored perspective ? efficiency constraints can serve a dual purpose as regularization.
4. **Concat vs Add vs Attention fusion**: The finding that simple concatenation outperforms both additive fusion and attention-based fusion on this task suggests that for dense prediction tasks with complementary shallow/deep features, preserving all information via concatenation may be preferable to learned fusion.

## Potential Improvements

1. **S-wave enhancement**: Add a dedicated S-wave branch with longer receptive field in the decoder, or incorporate S-wave specific data augmentation (lower SNR, more dispersed arrivals).
2. **Continuous data extension**: Implement a sliding-window inference strategy with overlap-and-add to handle continuous streams. This is critical for real-world deployment.
3. **Domain adaptation**: Fine-tune on regional datasets beyond STEAD/GEEDataset to improve generalization to different tectonic settings and distance ranges.
4. **Multi-task extension**: Combine phase picking with event detection or magnitude estimation in a shared architecture, leveraging the efficient backbone.

---

# Reproducibility Analysis

## Code Status

**Status**: [ ] Available [x] Not Found Yet [ ] Confirmed Missing [ ] Not Checked

**URL**: Not Found ? paper states code will be available upon publication.

## Data Status

- [x] **Public dataset available** ? both STEAD and GEEDataset V1.0 are publicly accessible
- [ ] Restricted dataset
- [ ] Private dataset
- [ ] Unknown

**Dataset Links**:
- STEAD: https://github.com/smousavi05/STEAD
- GEEDataset V1.0: https://prismax.opencompass.org.cn/domainlb

## Reproduction Feasibility

**Overall Assessment**: [x] High [ ] Medium [ ] Low

**Reason**: Both datasets are public. Architecture is comprehensively described with:
- Complete layer-by-layer specification (Table 1)
- All hyperparameters (optimizer, LR, batch size, epochs, augmentation)
- Dilation rates for both backbone and ASPP
- Training hardware configuration (4x V100-32GB)
- Model size (0.25M params, 258,097 parameters)

**Missing Components**:
- Official code implementation (pending publication)
- Exact weight initialization details (Kaiming normal mentioned, but specific seed not specified)
- Data preprocessing pipeline specifics (normalization, filtering)

**Difficulty Assessment**: Low-Medium. The architecture is straightforward (encoder-decoder with well-defined modules), parameter count is small, and training hyperparameters are fully specified. A competent practitioner could reproduce the architecture from the paper alone.

---

# Related Notes

- Task: [[Seismic Phase Picking]]
- Method: [[Depthwise Separable Convolution]], [[Temporal Convolutional Network]], [[Dilated Convolution]], [[ASPP]], [[Residual Connections]], [[Encoder-Decoder Architecture]]
- Dataset: [[STEAD]], [[GEEDataset V1.0]]
- Baseline Papers: PhaseNet (zhu2018_phasenet_note), EQTransformer (mousavi2020_eqtransformer_note), LPPN, SeisT, PickerXL, SeisLM
