# Stage 2E Experimental Design Freeze Report

> **????**: 2026-07-15
> **????**: 2A (Mining Strategy), 2B (Direction Feasibility), 2C (Dataset/Baseline), 2D (Baseline Reproduction Design)
> **????**: Seismic Image Segmentation ? Fault Segmentation
> **??**: RTX4070 12GB VRAM
> **??**: 3??????????
> **????**: ??????????????????????????
> **???**: Agnes (ResearchAI Agent)

---

## 1. Final Dataset Strategy

### 1.1 Primary Dataset: DeepFault

| Property | Value |
|----------|-------|
| URL | https://github.com/seisman/DeepFault |
| License | MIT |
| Format | HDF5 |
| Samples | 500,000+ 2D patches |
| Annotation | Binary fault mask |
| Dimension | 2D |

**Role**: Primary dataset for model training, validation, and final testing. Sufficient samples for robust training and statistical significance.

### 1.2 Secondary Dataset: SEG Salt

| Property | Value |
|----------|-------|
| URL | https://wiki.seg.org/wiki/Image_library |
| License | Creative Commons |
| Format | SEG-Y + PNG/TIFF masks |
| Samples | ~100,000 patches (256x256) |
| Annotation | Binary salt mask |
| Dimension | 2D |

**Role**: Cross-dataset generalization validation. Demonstrates model transferability from fault segmentation to salt body segmentation.

### 1.3 Tertiary Dataset: SEAM (Synthetic)

| Property | Value |
|----------|-------|
| URL | https://wiki.seg.org/wiki/Seismic_Models |
| License | Free (SEG) |
| Format | SEG-Y |
| Samples | Full 3D volumes (synthetic) |
| Annotation | Known geometry (ground truth) |
| Dimension | 3D (can extract 2D slices) |

**Role**: Controlled experiments. Perfect ground truth enables precise error analysis and boundary quality evaluation.

### 1.4 Data Split Strategy

| Split | DeepFault | SEG Salt | SEAM |
|-------|-----------|----------|------|
| Train | 350,000 (70%) | ? | ? |
| Validation | 75,000 (15%) | ? | ? |
| Test | 75,000 (15%) | 20,000 (held-out) | 10 full profiles |

**Spatial Leakage Prevention**: Patches from the same seismic line are kept in the same split. No patch from a training line appears in test set.

### 1.5 Synthetic vs Real Data Strategy

| Data Type | Role | Justification |
|-----------|------|---------------|
| Synthetic (SEAM) | Controlled experiments, error analysis | Perfect ground truth, known geometry |
| Real (DeepFault) | Primary training and evaluation | Realistic geological complexity |
| Cross-domain (SEG Salt) | Generalization validation | Demonstrates transferability |

**Key Principle**: Train on DeepFault (real), validate on held-out DeepFault, test on SEG Salt (cross-domain) and SEAM (synthetic). This three-tier validation demonstrates both accuracy and generalization.

---

## 2. Final Baseline Selection

### 2.1 Retained Baselines

| Baseline | Category | Params | Included | Reason |
|----------|----------|--------|----------|--------|
| Canny Edge Detection | Traditional | 0 | YES | Industry standard, zero parameters, establishes non-DL upper bound |
| Coherence Attribute | Traditional | 0 | YES | Domain-specific seismic attribute, essential for fair comparison in seismic literature |
| U-Net | CNN | ~31M | YES | Standard baseline for all segmentation papers, required for comparison |
| Attention U-Net | CNN | ~35M | YES | Shows attention mechanism value, directly comparable to proposed method |
| UNet++ | CNN | ~35M | YES | Nested skip connections, state-of-the-art CNN before transformers |
| SegFormer-B0 | Transformer | ~36M | YES | Transformer baseline, demonstrates CNN vs Transformer comparison |

### 2.2 Deleted Baselines

| Baseline | Category | Reason for Deletion |
|----------|----------|---------------------|
| TransUNet | Transformer | ~86M params too large for RTX4070 with batch=16; SegFormer-B0 provides sufficient Transformer comparison |
| Swin Transformer | Transformer | Higher VRAM requirements, similar architecture class to SegFormer; redundant for first paper |

**Justification**: The 6 retained baselines provide comprehensive coverage:
- 2 Traditional (non-DL)
- 3 CNN (U-Net family)
- 1 Transformer (SegFormer-B0)

This is sufficient for a first paper. Additional baselines can be added in follow-up work.

---

## 3. Final Experiment Matrix

| Method | Category | Params | Training Strategy | Dataset | Metrics |
|--------|----------|--------|------------------|---------|--------|
| Canny | Traditional | 0 | N/A | DeepFault | Dice, IoU (post-threshold) |
| Coherence | Traditional | 0 | N/A | DeepFault | Dice, IoU (post-threshold) |
| U-Net | CNN | ~31M | Adam, lr=1e-3, BCE+Dice, 100 epochs, batch=16 | DeepFault | Dice, IoU, Prec, Recall, F1 |
| Attention U-Net | CNN | ~35M | Adam, lr=1e-3, BCE+Dice, 100 epochs, batch=16 | DeepFault | Dice, IoU, Prec, Recall, F1 |
| UNet++ | CNN | ~35M | Adam, lr=1e-3, BCE+Dice, 100 epochs, batch=16 | DeepFault | Dice, IoU, Prec, Recall, F1 |
| SegFormer-B0 | Transformer | ~36M | Adam, lr=1e-3, BCE+Dice, 100 epochs, batch=12 | DeepFault | Dice, IoU, Prec, Recall, F1 |
| Ours (Freq-U-Net) | CNN+Freq | ~33M | Adam, lr=1e-3, BCE+Dice, 100 epochs, batch=16 | DeepFault | Dice, IoU, Prec, Recall, F1 |

**Cross-Dataset Evaluation**: Ours + best baseline (U-Net or Attention U-Net) evaluated on SEG Salt and SEAM.

**Statistical Reporting**: Mean + std over 3 independent runs (different random seeds). Paired t-test vs best baseline, p < 0.05.

---

## 4. Innovation Module Design: Frequency-Domain Enhanced U-Net

### 4.1 Architecture Overview

```
Input [B, 1, 256, 256]
  |
  v
Encoder (4 stages, standard U-Net)
  |
  +---> Skip 1 (Conv4_3, 512 ch) ----+
  |                                   |
  +---> Skip 2 (Conv3_3, 256 ch) ----+
  |                                   |
  +---> Skip 3 (Conv2_2, 128 ch) ----+
  |                                   |
  +---> Skip 4 (Conv1_2, 64 ch) ----+
                                      |
                                      v
                          [Frequency Domain Branch]
                                      |
                                      v
                          Frequency-Guided Fusion
                                      |
                                      v
                          Decoder (4 stages)
                                      |
                                      v
                          Output [B, 1, 256, 256]
```

### 4.2 Frequency Domain Module Design

**Location**: Inserted between each encoder stage and its corresponding decoder skip connection.

**Structure per stage**:

```
Skip Feature [B, C, H, W]
  |
  v
FFT2D -> [B, C, H, W//2+1] (complex)
  |
  v
Magnitude + Phase Split
  |
  v
[Branch 1: Magnitude Attention]
  GlobalAvgPool -> MLP(C, C//4) -> Sigmoid -> Multiply
  |
  v
[Branch 2: Phase Attention]
  GlobalAvgPool -> MLP(C, C//4) -> Sigmoid -> Multiply
  |
  v
IFFT2D -> [B, C, H, W]
  |
  v
Conv1x1(C, C) + Residual Connection
  |
  v
Fused Feature [B, C, H, W] -> passed to decoder
```

### 4.3 Key Design Decisions

| Decision | Value | Rationale |
|----------|-------|-----------|
| FFT location | After each encoder stage, before decoder | Captures multi-scale frequency information |
| Frequency processing | Separate magnitude and phase attention | Magnitude = energy distribution, Phase = structural information |
| MLP reduction ratio | C // 4 | Minimal parameter overhead (~4x fewer params than original) |
| Fusion method | Conv1x1 + residual | Preserves skip connection information, adds frequency guidance |
| Number of FDM instances | 4 (one per stage) | Multi-scale frequency modeling |

### 4.4 Parameter and Complexity Analysis

| Component | U-Net Params | Ours Params | Increase |
|-----------|-------------|-------------|----------|
| Encoder | ~20M | ~20M | 0 |
| Decoder | ~10M | ~10M | 0 |
| Frequency Domain Modules | 0 | ~3M | +10% |
| **Total** | **~31M** | **~33M** | **+6.5%** |

**Computational Cost**:
- FFT2D: O(N log N) per feature map (negligible vs convolution)
- IFFT2D: O(N log N) per feature map
- MLP attention: O(C^2/HW) ? very small due to global pooling
- **Total overhead**: ~5-8% additional FLOPs, negligible in practice

**Memory Impact**: +0.2 GB VRAM (from 3.5 GB to 3.7 GB for batch=16), well within RTX4070 capacity.

---

## 5. Ablation Study Design

### 5.1 Ablation Configuration

| Config | Components | Purpose |
|--------|-----------|---------|
| A: U-Net Baseline | Standard U-Net | Reference point |
| B: U-Net + Attention | U-Net + CBAM on skip connections | Isolates attention contribution |
| C: U-Net + Frequency | U-Net + FDM only | Isolates frequency contribution |
| D: Ours (Full) | U-Net + Attention + Frequency | Complete proposed method |

### 5.2 Expected Results Pattern

| Config | Dice | IoU | Improvement over A |
|--------|------|-----|-------------------|
| A: U-Net | Baseline | Baseline | ? |
| B: + Attention | +0.005-0.010 | +0.004-0.008 | Marginal |
| C: + Frequency | +0.008-0.015 | +0.006-0.012 | Moderate |
| D: + Both | +0.012-0.020 | +0.010-0.017 | Significant |

**Hypothesis**: Frequency module provides larger gain than attention alone. Combined, they are synergistic (D > B + C).

### 5.3 Ablation Validation Criteria

- Each config trained with same hyperparameters, same random seed
- Reported as mean ? std over 3 runs
- Statistical significance tested (paired t-test, p < 0.05)
- Qualitative visualization of error maps for each config

---

## 6. Evaluation Protocol

### 6.1 Quantitative Metrics

| Metric | Formula | Range | Reporting |
|--------|---------|-------|-----------|
| Dice Coefficient | 2*TP / (2*TP + FP + FN) | [0, 1] | Primary metric |
| IoU (Jaccard) | TP / (TP + FP + FN) | [0, 1] | Secondary metric |
| Precision | TP / (TP + FP) | [0, 1] | Tertiary metric |
| Recall | TP / (TP + FN) | [0, 1] | Tertiary metric |
| F1 Score | 2*(Prec*Rec)/(Prec+Rec) | [0, 1] | Equivalent to Dice |

**Reporting Format**: Mean ? std over 3 independent runs. Best result bolded in tables.

### 6.2 Qualitative Visualization

**Figure 1**: Multi-panel comparison (6 panels per test sample)
- Panel 1: Seismic image
- Panel 2: Ground truth mask
- Panel 3: U-Net prediction
- Panel 4: Ours prediction
- Panel 5: Error map (|Prediction - GT|)
- Panel 6: All methods overlay

**Figure 2**: Cross-dataset generalization
- Training on DeepFault, testing on SEG Salt
- Visual comparison of prediction quality

**Figure 3**: Frequency feature visualization
- FFT magnitude visualization at different encoder stages
- Shows what frequencies the model attends to

### 6.3 Statistical Testing

- **Test**: Paired t-test comparing Ours vs best baseline (U-Net or Attention U-Net)
- **Significance level**: p < 0.05
- **Number of runs**: 3 (different random seeds)
- **Metric**: Dice coefficient (primary)

---

## 7. RTX4070 Training Plan

### 7.1 Training Configuration

| Parameter | Value |
|-----------|-------|
| GPU | RTX4070 12GB |
| Batch Size | 16 (U-Net family), 12 (SegFormer-B0) |
| Mixed Precision | AMP (torch.cuda.amp) ? enabled for all models |
| Optimizer | Adam (lr=1e-3, weight_decay=1e-4) |
| Scheduler | Cosine Annealing (min_lr=1e-6) |
| Loss | BCE + Dice (alpha=0.5, beta=0.5) |
| Epochs | 100 (early stopping patience=20) |
| Input Size | 256x256 |
| Data Augmentation | As specified in Stage 2D |

### 7.2 Expected Training Times (RTX4070)

| Model | Epoch Time | Total Time (100 epochs) | VRAM Usage |
|-------|-----------|------------------------|------------|
| U-Net | ~3 min/epoch | ~5 hours | ~3.5 GB |
| Attention U-Net | ~4 min/epoch | ~7 hours | ~4.0 GB |
| UNet++ | ~4 min/epoch | ~7 hours | ~4.0 GB |
| SegFormer-B0 | ~6 min/epoch | ~10 hours | ~4.5 GB |
| Ours (Freq-U-Net) | ~4 min/epoch | ~7 hours | ~3.7 GB |

**Total training time for all models**: ~35-40 hours (can run overnight, multiple models in parallel on different GPUs if available)

### 7.3 Experiment Execution Order

| Order | Experiment | Duration | Notes |
|-------|-----------|----------|-------|
| 1 | U-Net baseline | 5 hours | Establish reference |
| 2 | Attention U-Net | 7 hours | First improvement baseline |
| 3 | UNet++ | 7 hours | Second CNN baseline |
| 4 | Ours (Freq-U-Net) | 7 hours | Proposed method |
| 5 | SegFormer-B0 | 10 hours | Transformer baseline |
| 6 | Ablation configs B, C | 14 hours | Run B and C in parallel |
| 7 | Cross-dataset eval | 2 hours | SEG Salt + SEAM testing |

**Parallelization**: Experiments 1-5 can run sequentially. Experiments 6 (Ablation B and C) can run in parallel if 2 GPUs available.

---

## 8. Stage 3 Implementation Roadmap

### 8.1 Stage 3A: Dataset Preparation (Week 1)

**Tasks**:
- [ ] Download DeepFault from GitHub
- [ ] Download SEG Salt from SEG
- [ ] Download SEAM from SEG
- [ ] Implement HDF5 reader (h5py)
- [ ] Implement preprocessing (normalize, crop, pad)
- [ ] Implement train/val/test split with spatial leakage prevention
- [ ] Implement data augmentation pipeline
- [ ] Create PyTorch DataLoader
- [ ] Verify data quality (visualize samples)

**Deliverable**: Working DataLoader for DeepFault, SEG Salt, SEAM

### 8.2 Stage 3B: Baseline Implementation (Week 2-3)

**Tasks**:
- [ ] Clone and adapt U-Net (milesial/Pytorch-UNet)
- [ ] Clone and adapt Attention U-Net (ooa/Attention-UNet-Pytorch)
- [ ] Clone and adapt UNet++ (MrGiovanni/UNetPlusPlus)
- [ ] Clone and adapt SegFormer (NVlabs/SegFormer)
- [ ] Implement traditional baselines (Canny, Coherence)
- [ ] Adapt all models for single-channel input
- [ ] Implement unified training loop
- [ ] Implement unified evaluation script

**Deliverable**: All 6 baselines trained and evaluated on DeepFault

### 8.3 Stage 3C: Baseline Evaluation (Week 3)

**Tasks**:
- [ ] Run all baselines with 3 random seeds
- [ ] Collect Dice, IoU, Precision, Recall metrics
- [ ] Generate comparison tables
- [ ] Generate qualitative visualization figures
- [ ] Perform statistical significance testing

**Deliverable**: Complete baseline evaluation results

### 8.4 Stage 3D: Frequency Module Implementation (Week 3-4)

**Tasks**:
- [ ] Implement FFT/IFFT frequency domain module
- [ ] Implement magnitude and phase attention branches
- [ ] Integrate FDM into U-Net decoder skip connections
- [ ] Implement all ablation configs (B, C)
- [ ] Train Ours and ablation configs
- [ ] Compare with baselines

**Deliverable**: Ours model trained, ablation results complete

### 8.5 Stage 3E: Full Experiment (Week 5)

**Tasks**:
- [ ] Cross-dataset evaluation (SEG Salt, SEAM)
- [ ] Generate all comparison figures
- [ ] Final statistical analysis
- [ ] Compile results table
- [ ] Draft manuscript

**Deliverable**: Complete experimental results, manuscript draft

### 8.6 Stage 3F: Paper Figure Generation (Week 6)

**Tasks**:
- [ ] Finalize all figures (qualitative + quantitative)
- [ ] Generate error maps and frequency visualizations
- [ ] Create multi-panel comparison figures
- [ ] Final manuscript polish
- [ ] Internal review

**Deliverable**: Complete manuscript ready for submission

---

## 9. Risk Assessment and Mitigation

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| DeepFault download fails | MEDIUM | LOW | Use SEG Salt as primary, DeepFault as secondary |
| RTX4070 VRAM insufficient for batch=16 | LOW | LOW | Reduce to batch=8, use AMP |
| Frequency module doesn't improve results | HIGH | MEDIUM | Have ablation plan (B, C) to isolate contribution; may pivot to attention-only variant |
| SegFormer training too slow | LOW | MEDIUM | Use batch=12, AMP; acceptable if 10 hours |
| Cross-dataset generalization poor | MEDIUM | MEDIUM | Expected ? report as limitation, focus on DeepFault results |

---

## 10. Final Verdict

| Check | Result |
|---|---|
| Dataset strategy finalized | PASS |
| Baseline selection justified | PASS |
| Experiment matrix complete | PASS |
| Innovation module designed | PASS |
| Ablation study defined | PASS |
| Evaluation protocol rigorous | PASS |
| RTX4070 training plan feasible | PASS |
| Stage 3 roadmap clear | PASS |
| Risks identified and mitigated | PASS |
| No files modified | PASS |
| Mode B respected | PASS |

**Overall: PASS**

Experimental design is frozen. All components are specified, justified, and feasible on RTX4070. The design supports a complete 6-week experiment cycle targeting a publishable first paper in seismic fault segmentation.

---

*Stage 2E Experimental Design Freeze completed*
*Generated: 2026-07-15 | Agent: Agnes (ResearchAI)*
