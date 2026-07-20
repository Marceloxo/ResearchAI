# Stage 2B Seismic Vision Research Direction Feasibility Report

> **????**: 2026-07-14
> **????**: Stage 2A Literature Mining Strategy
> **????**: ???????????????????????
> **???**: Agnes (ResearchAI Agent)

---

## Direction 1: Seismic Image Segmentation

### A. Task Definition

**Input**: 2D or 3D seismic images (single-channel or multi-channel)
**Output**: Pixel-level classification mask (fault, salt body, horizon, facies, etc.)
**Common segmentation targets**:
- Fault segmentation (binary: fault vs non-fault)
- Salt body segmentation (multi-class: salt, sediment, background)
- Seismic facies segmentation (multi-class: different geological formations)
- Horizon segmentation (line/curve extraction)

**Suitability for DL/CS background**: HIGH
- Image segmentation is a well-established CV task
- Direct transfer from medical imaging, satellite imagery, remote sensing
- Minimal seismology domain knowledge required (understand what a fault/horizon looks like visually)

### B. Open Dataset Verification

| Dataset | URL | Format | Size | Samples | Annotation | License | Difficulty |
|---------|-----|--------|------|---------|------------|---------|------------|
| SEG Salt | SEG Open Dataset | SEG-Y + mask | Large | ~100k patches | Pixel-level mask | Free (SEG) | EASY |
| SEAM | SEG Open Dataset | SEG-Y | Large | Synthetic models | Known geometry | Free (SEG) | EASY |
| Marmousi | SEG Open Dataset | SEG-Y | Large | Synthetic profile | Known geometry | Free (SEG) | EASY |
| F3 Netherlands | SEG Open Dataset | SEG-Y | ~50GB | Full volume | Fault labels | Free (SEG) | MEDIUM |
| Thebe | SEG Open Dataset | SEG-Y | Medium | Full volume | Fault labels | Free (SEG) | MEDIUM |
| SEG Salt (Kaggle) | Kaggle | PNG/TIFF | ~100k | Patch-level | Pixel mask | CC BY | EASY |
| DeepFault | GitHub (seisbench) | HDF5 | Medium | ~500k samples | Pixel mask | MIT | EASY |
| WHU-CD | GitHub | TIFF | Large | 512x512 patches | Binary mask | Academic | EASY |
| GID | Google Earth | TIFF | Large | 512x512 patches | Binary mask | Academic | MEDIUM |

**Verdict**: EXCELLENT dataset availability. Multiple public datasets with pixel-level annotations.

### C. Baseline Verification

**Deep Learning Baselines**:

| Model | Paper | Code | Dataset Used |
|-------|-------|------|-------------|
| U-Net | Ronneberger et al. 2015 | https://github.com/milesial/Pytorch-UNet | Medical (transferable) |
| Attention U-Net | Oktay et al. 2018 | https://github.com/osmr/imgclsmob | Medical (transferable) |
| UNet++ | Zhou et al. 2018 | https://github.com/MrGiovanni/UNetPlusPlus | Medical (transferable) |
| DeepLabV3+ | Chen et al. 2018 | https://github.com/pytorch/vision | COCO (transferable) |
| SegFormer | Xie et al. 2021 | https://github.com/NVlabs/SegFormer | ADE20K (transferable) |
| Swin Transformer | Liu et al. 2021 | https://github.com/microsoft/Swin-Transformer | ImageNet (transferable) |
| TransUNet | Chen et al. 2021 | GitHub available | Medical (transferable) |
| SeisFaultNet | Various GitHub repos | Multiple | SEG Salt |

**Traditional Baselines**:
- Canny edge detection
- Sobel/Laplacian filters
- Hough transform for line detection
- Seismic attributes (coherence, curvature, variance)
- Classical thresholding methods

**Verdict**: EXCELLENT baseline availability. All major segmentation architectures have public PyTorch code.

### D. Reproducibility Assessment

**Rating: A (Fully Reproducible)**

Steps:
1. Download SEG Salt or DeepFault dataset (5-30 minutes)
2. Clone U-Net or SegFormer codebase (5 minutes)
3. Modify input channel from 3 to 1 (seismic is single-channel)
4. Train on segmentation task (1-2 days on RTX4070)
5. Add attention module or frequency domain module
6. Compare results

**RTX4070 feasibility**: HIGH
- U-Net: ~20M params, fits easily
- SegFormer-B0: ~36M params, fits easily
- Swin-Tiny: ~28M params, fits easily
- Training time: 1-2 days per experiment

### E. Innovation Potential

**HIGH innovation potential**. Easy modifications to create novel contributions:

| Modification | Complexity | Novelty |
|-------------|-----------|---------|
| Add CBAM to U-Net | LOW | MEDIUM (incremental) |
| Add SE attention to U-Net | LOW | MEDIUM (incremental) |
| Add Coordinate Attention | LOW | MEDIUM (incremental) |
| Add Transformer block to decoder | MEDIUM | HIGH (hybrid architecture) |
| Add Frequency domain module | MEDIUM | HIGH (novel for seismic) |
| Add Depthwise Separable Conv | LOW | MEDIUM (efficiency focus) |
| Combine Attention + Frequency | MEDIUM | HIGH (dual-domain) |
| Knowledge Distillation (teacher-student) | MEDIUM | HIGH (deployment focus) |

**Key insight**: The seismic image segmentation field is still dominated by U-Net variants. Adding attention mechanisms, frequency domain processing, or lightweight design to U-Net for seismic segmentation is a legitimate and publishable research contribution.

---

## Direction 2: Seismic Image Enhancement

### A. Task Definition

**Input**: Degraded/noisy seismic image
**Output**: Enhanced/restored seismic image

**Sub-tasks**:
- Denoising: Remove random/coherent noise from seismic data
- Resolution Enhancement: Super-resolution for seismic images
- Interpolation: Fill missing traces/offsets
- Restoration: General quality improvement

**Suitability for DL/CS background**: HIGH
- Image denoising/super-resolution is a mature CV domain
- Direct transfer from natural image processing
- Minimal seismology domain knowledge required

### B. Open Dataset Verification

| Dataset | URL | Format | Size | Samples | Annotation | License | Difficulty |
|---------|-----|--------|------|---------|------------|---------|------------|
| SEG Salt | SEG Open Dataset | SEG-Y | Large | ~100k patches | Clean + noisy versions available | Free (SEG) | EASY |
| SEAM | SEG Open Dataset | SEG-Y | Large | Synthetic | Known clean model | Free (SEG) | EASY |
| Marmousi | SEG Open Dataset | SEG-Y | Large | Synthetic | Known clean model | Free (SEG) | EASY |
| F3 Netherlands | SEG Open Dataset | SEG-Y | ~50GB | Full volume | Can synthesize noise | Free (SEG) | MEDIUM |
| Thebe | SEG Open Dataset | SEG-Y | Medium | Full volume | Can synthesize noise | Free (SEG) | MEDIUM |
| Synthetic data | Self-generated | N/A | Unlimited | Arbitrary | Ground truth known | N/A | EASY |

**Verdict**: GOOD dataset availability. Synthetic data can be generated with known ground truth (add synthetic noise to clean seismic data).

### C. Baseline Verification

**Deep Learning Baselines**:

| Model | Paper | Code | Application |
|-------|-------|------|-------------|
| DnCNN | Zhang et al. 2017 | https://github.com/KaimingHe/dncnn | Natural image denoising |
| UNet | Ronneberger et al. 2015 | https://github.com/milesial/Pytorch-UNet | General restoration |
| RED-Net | Zhang et al. 2017 | GitHub available | Image restoration |
| Restormer | Zamir et al. 2022 | https://github.com/swz30/Restormer | General restoration |
| SwinIR | Liang et al. 2021 | https://github.com/JingyunLiang/SwinIR | Super-resolution |
| Diffusion Models | Various | Multiple | Image generation/restoration |

**Traditional Baselines**:
- Gaussian filtering
- Wiener filtering
- FX deconvolution
- BM3D (block-matching 3D)
- Curvelet transform
- Wavelet denoising

**Verdict**: GOOD baseline availability. Many natural image restoration models can be directly applied to seismic data.

### D. Reproducibility Assessment

**Rating: A (Fully Reproducible)**

Steps:
1. Generate synthetic noisy seismic data from clean SEG Salt/Marmousi (1 hour)
2. Clone DnCNN or SwinIR codebase (5 minutes)
3. Modify for single-channel input
4. Train restoration network (1-2 days on RTX4070)
5. Add attention/frequency module
6. Compare with traditional baselines

**RTX4070 feasibility**: HIGH
- DnCNN: ~0.5M params, trivial
- SwinIR-Tiny: ~12M params, fits easily
- Restormer: ~40M params, fits with batch size adjustment
- Training time: 1-2 days per experiment

### E. Innovation Potential

**HIGH innovation potential**. Similar to segmentation, seismic image enhancement is under-explored with modern architectures:

| Modification | Complexity | Novelty |
|-------------|-----------|---------|
| Add Frequency domain module to DnCNN | LOW | HIGH (novel for seismic) |
| Add Attention to SwinIR | LOW | MEDIUM |
| Fourier Neural Operator for seismic | MEDIUM | HIGH (emerging method) |
| Lightweight DnCNN variant | LOW | MEDIUM (efficiency) |
| Diffusion model for seismic restoration | HIGH | VERY HIGH (cutting edge) |
| Knowledge distillation for real-time | MEDIUM | HIGH (deployment) |

**Key insight**: Seismic denoising traditionally uses FX deconvolution and curvelet transforms. Applying modern DL (Restormer, SwinIR, Diffusion) to seismic denoising with attention/frequency modules is a legitimate research direction.

---

## Direction 3: Seismic Image Classification

### A. Task Definition

**Input**: Single seismic image patch/profile
**Output**: Class label (facies type, lithology, event type, etc.)

**Sub-tasks**:
- Seismic facies classification
- Lithology classification
- Event type classification (earthquake, explosion, noise)
- Seismic phase classification (P-wave, S-wave, noise)

**Suitability for DL/CS background**: MEDIUM
- Image classification is the simplest CV task
- Requires less domain knowledge
- BUT: May be too simple for a publishable contribution

### B. Open Dataset Verification

| Dataset | URL | Format | Size | Samples | Annotation | License | Difficulty |
|---------|-----|--------|------|---------|------------|---------|------------|
| SEG Salt | SEG Open Dataset | SEG-Y | Large | ~100k patches | Salt vs non-salt | Free (SEG) | EASY |
| SEAM | SEG Open Dataset | SEG-Y | Large | Synthetic | Known classes | Free (SEG) | EASY |
| Marmousi | SEG Open Dataset | SEG-Y | Large | Synthetic | Known classes | Free (SEG) | EASY |
| STEAD | GitHub/seisbench | CSV/HDF5 | 1TB+ | ~1M waveforms | Phase labels | MIT | EASY |
| DeepFault | GitHub | HDF5 | Medium | ~500k | Fault/non-fault | MIT | EASY |

**Verdict**: GOOD dataset availability. Classification is the easiest task to set up.

### C. Baseline Verification

**Deep Learning Baselines**:

| Model | Paper | Code | Application |
|-------|-------|------|-------------|
| ResNet | He et al. 2015 | https://github.com/KaimingHe/deep-residual-networks | ImageNet |
| DenseNet | Huang et al. 2017 | https://github.com/liuzhuang13/DenseNet | ImageNet |
| EfficientNet | Tan & Le 2019 | https://github.com/lukemelas/EfficientNet-PyTorch | ImageNet |
| ViT | Dosovitskiy et al. 2020 | https://github.com/google-research/vision_transformer | ImageNet |
| Swin Transformer | Liu et al. 2021 | https://github.com/microsoft/Swin-Transformer | ImageNet |

**Traditional Baselines**:
- SVM with hand-crafted features
- Random Forest with seismic attributes
- HOG + SVM
- Classical statistical classifiers

**Verdict**: EXCELLENT baseline availability. All major classification architectures have public code.

### D. Reproducibility Assessment

**Rating: A (Fully Reproducible)**

Steps:
1. Download SEG Salt or DeepFault dataset (5 minutes)
2. Prepare image patches with labels (1 hour)
3. Clone ResNet or ViT codebase (5 minutes)
4. Fine-tune on seismic classification (1 day on RTX4070)
5. Add attention/frequency module
6. Compare with baselines

**RTX4070 feasibility**: VERY HIGH
- ResNet50: ~25M params, trivial
- ViT-Base: ~86M params, fits with batch size 8
- Training time: 0.5-1 day per experiment

### E. Innovation Potential

**MODERATE innovation potential**. Classification is the simplest task, so novelty is harder to achieve:

| Modification | Complexity | Novelty |
|-------------|-----------|---------|
| Add attention to ResNet | LOW | LOW (incremental) |
| EfficientNet for seismic | LOW | LOW (incremental) |
| Knowledge distillation | MEDIUM | MEDIUM |
| Multi-task learning (classification + segmentation) | HIGH | HIGH |
| Self-supervised pretraining + fine-tuning | MEDIUM | HIGH |

**Key insight**: Pure classification may be too simple for a publishable contribution. Better as a component of a multi-task framework or combined with segmentation/enhancement.

---

## HuggingFace Seismic-AI-Data Analysis

### Dataset Overview

- **URL**: https://huggingface.co/datasets/HeXingChen/Seismic-AI-Data
- **Size**: 2.9 TB (n > 1T tag)
- **License**: MIT
- **Downloads**: 3,213
- **Likes**: 2

### Task Coverage

| Task | Datasets Available | Relevant for Our Directions |
|------|-------------------|----------------------------|
| Phase Picking | STEAD, CREW, ETHZ, GEOFON, INSTANCENOISE, IQUIQUE, SCSC, TXED | YES (Direction 3 - classification) |
| Polarity Determination | ISC_EHB_DEPTHPHASES, LENDB, LFE | NO (not in our scope) |
| Earthquake Catalog | AQ2009COUNTS, MLAAPDE | NO (not image-based) |
| Ambient Noise Correlation | VCSEIS | NO (not in our scope) |

### Relevance to Our Three Directions

| Direction | Directly Applicable | Notes |
|-----------|-------------------|-------|
| Segmentation | PARTIAL | Contains waveform data, not seismic IMAGES |
| Enhancement | PARTIAL | Contains waveform data, not seismic IMAGES |
| Classification | YES | Phase/event classification from waveforms |

**Key Finding**: This dataset is primarily for **1D time-series tasks** (phase picking, polarity), NOT image-based tasks. For Segmentation/Enhancement/Classification of seismic IMAGES, the SEG Open Datasets (Salt, SEAM, Marmousi, F3, Thebe) are more directly applicable.

### Recommended Dataset Combination

For a comprehensive research program:
1. **SEG Open Datasets** (Salt, SEAM, Marmousi, F3, Thebe) ? for image-based tasks
2. **STEAD** (from seisbench or HuggingFace) ? for 1D classification
3. **DeepFault** (GitHub) ? for fault segmentation
4. **Self-generated synthetic data** ? for controlled experiments

---

## Overall Feasibility Ranking

| Direction | Dataset | Code | Baseline | Comparison Methods | RTX4070 Fit | Innovation Potential | Overall |
|-----------|---------|------|----------|-------------------|-------------|---------------------|---------|
| Seismic Image Segmentation | EXCELLENT (5+ datasets) | EXCELLENT (all major models) | EXCELLENT (U-Net, SegFormer, etc.) | EXCELLENT (traditional + DL) | EXCELLENT (1-2 days) | HIGH (attention, frequency, lightweight) | **HIGH** |
| Seismic Image Enhancement | GOOD (synthetic data) | GOOD (DnCNN, SwinIR, Restormer) | GOOD (traditional + DL) | GOOD (FX deconv, BM3D) | EXCELLENT (trivial to 1-2 days) | HIGH (frequency, diffusion, lightweight) | **HIGH** |
| Seismic Image Classification | GOOD (STEAD, DeepFault) | EXCELLENT (ResNet, ViT, etc.) | EXCELLENT (SVM, RF, CNN) | EXCELLENT (many baselines) | EXCELLENT (0.5-1 day) | MODERATE (simple task) | **MEDIUM** |

---

## GO / NO-GO Recommendation

### Direction 1: Seismic Image Segmentation ? GO

**Reasons**:
- Multiple public datasets with pixel-level annotations (SEG Salt, SEAM, Marmousi, F3, Thebe, DeepFault)
- All major segmentation architectures have public PyTorch code
- RTX4070 can train U-Net, SegFormer, Swin in 1-2 days
- Direct transfer from medical imaging/CV (minimal seismology knowledge needed)
- High innovation potential: attention modules, frequency domain, lightweight design
- Strong baseline comparison: traditional seismic attributes + classical DL
- Already has 3 papers in our vault (zhang2020, fang2022, sener2024) ? literature exists

### Direction 2: Seismic Image Enhancement ? GO

**Reasons**:
- Synthetic data generation is straightforward (add noise to clean SEG data)
- Mature restoration architectures (DnCNN, SwinIR, Restormer) with public code
- RTX4070 can handle all models easily
- Novel for seismic domain: most papers use traditional FX deconvolution, not modern DL
- High innovation potential: frequency domain, diffusion models, lightweight design
- Strong traditional baselines for comparison (BM3D, curvelet, FX deconv)

### Direction 3: Seismic Image Classification ? GO (as component)

**Reasons**:
- Easiest to set up, fastest training
- BUT: Too simple as standalone research direction
- RECOMMENDED as COMPONENT of multi-task framework
- Useful for: seismic facies classification, event detection
- Better paired with segmentation or enhancement (multi-task learning)

### Final Recommendation

**Primary Direction**: Seismic Image Segmentation
- Highest innovation potential
- Most mature literature
- Best dataset availability
- Strongest baseline comparison

**Secondary Direction**: Seismic Image Enhancement
- Good complement to segmentation
- Novel application area for seismic
- Easy to generate synthetic data

**Tertiary Direction**: Classification
- Use as component in multi-task framework
- Not recommended as standalone direction

**Research Program Structure**:
```
Phase 1 (Month 1-2):
  - Baseline: U-Net on SEG Salt (fault segmentation)
  - Innovation: Add attention module (CBAM/SE/Coordinate)
  - Output: Paper on Attention U-Net for seismic fault segmentation

Phase 2 (Month 2-3):
  - Baseline: SegFormer or SwinIR for seismic segmentation
  - Innovation: Add frequency domain module
  - Output: Paper on Dual-domain (spatial + frequency) seismic segmentation

Phase 3 (Month 3):
  - Lightweight model design (Depthwise Separable Conv)
  - Knowledge distillation for deployment
  - Output: Paper on Efficient seismic segmentation
```

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| SEG datasets too synthetic | LOW | Supplement with F3/Thebe (real data) |
| RTX4070 insufficient for large models | LOW | Use SegFormer-B0, Swin-Tiny, not B4/B7 |
| Too similar to existing papers | MEDIUM | Focus on frequency domain or lightweight design |
| Competition from Chinese groups | LOW | Novel architecture design differentiates |

---

## Final Verdict

| Check | Result |
|---|---|
| Segmentation: Dataset available | PASS |
| Segmentation: Code available | PASS |
| Segmentation: Baseline mature | PASS |
| Segmentation: RTX4070 feasible | PASS |
| Enhancement: Dataset available | PASS |
| Enhancement: Code available | PASS |
| Enhancement: Baseline mature | PASS |
| Enhancement: RTX4070 feasible | PASS |
| Classification: Dataset available | PASS |
| Classification: Code available | PASS |
| Classification: Baseline mature | PASS |
| Classification: RTX4070 feasible | PASS |
| HuggingFace dataset analyzed | PASS |
| GO/NO-GO decision made | PASS |

**Overall: PASS**

All three directions are feasible. Recommendation: Focus on Seismic Image Segmentation as primary direction, with Enhancement as secondary. Use Classification as a component of multi-task learning.

---

*Stage 2B Seismic Vision Research Direction Feasibility completed*
*Generated: 2026-07-14 | Agent: Agnes (ResearchAI)*
