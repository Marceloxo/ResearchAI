# Stage 9 — Research Direction Validation & Dataset Pipeline

## Objective

Execute the first paper's experimental pipeline: **Seismic Image Segmentation** using Transformer/CNN architectures on F3 Netherlands, Thebe, and SEG Salt datasets.

**NOT in scope**: PhaseNet/EQTransformer reproduction (P3 — secondary).

---

## Stage 9.1 — Environment Setup

**Goal**: Python environment with GPU support, clone baseline repos.

- [ ] Create conda environment (Python 3.10, CUDA 12.x)
- [ ] Install PyTorch 2.x with CUDA support
- [ ] Verify RTX 4070 detection: `torch.cuda.is_available()`
- [ ] Create project directory: `03_Projects/seismic_seg_pipeline/`
- [ ] Clone/pull baseline code: SegFormer (official), U-Net (standard implementation)

**Reference experiment**: [[exp_dataset_pipeline_seg]]

---

## Stage 9.2 — Dataset Download & Standardization

**Goal**: All 5 target datasets downloaded, preprocessed, and split consistently.

- [ ] **F3 Netherlands** — Download from SEG Wiki or alternative source
  - Facies labels (7 classes)
  - Standardize: create train/val/test split (70/15/15)
  - Document: file format, dimensions, class distribution
- [ ] **Thebe** — Download from GitHub (Thebe Fault Benchmark)
  - Binary fault labels
  - Document: training methodology from original paper
- [ ] **SEG Salt** — Download from Kaggle TGS Salt Challenge
  - Binary salt labels
  - Note: this is a 2D slice dataset, not 3D
- [ ] **Parihaka** — Download (if publicly available)
  - Facies labels
- [ ] **Penobscot** — Download from SEG Wiki
  - Facies labels

**For each dataset**:
- [ ] Create data loader script with standardized interface
- [ ] Implement preprocessing: normalization, patching, augmentation
- [ ] Verify with random sample visualization
- [ ] Document: dataset statistics, split ratios, preprocessing choices

**Reference experiment**: [[exp_dataset_pipeline_seg]]

---

## Stage 9.3 — Baseline: U-Net on F3 Facies

**Goal**: Lowest baseline — reproduce standard U-Net result on F3 Netherlands facies.

- [ ] Implement U-Net (standard 2D, 4-level encoder-decoder)
- [ ] Train on F3 facies: measure IoU per class, mIoU
- [ ] Log: training curves, final metrics, inference speed
- [ ] Document: hyperparameters, training time on RTX 4070

**Expected deliverable**: Reproducible U-Net baseline with known metrics.

---

## Stage 9.4 — Baseline: SegFormer on F3 Facies

**Goal**: Transformer baseline — reproduce wang2024 U-SegFormer-Hyper results.

- [ ] Implement SegFormer (MiT-B0, B1, B2 backbones)
- [ ] Implement U-SegFormer-Hyper (SegFormer + hypercolumn fusion)
- [ ] Train on F3 facies: compare with U-Net baseline
- [ ] Profile GPU memory and inference speed for each variant
- [ ] Document: which variant fits on RTX 4070 12GB?

**Expected deliverable**: SegFormer baseline with RTX 4070 resource profile.

---

## Stage 9.5 — Cross-Dataset Validation

**Goal**: Verify that baselines generalize to other seismic datasets.

- [ ] Train U-Net + SegFormer on Thebe (fault)
- [ ] Train U-Net + SegFormer on SEG Salt (salt)
- [ ] Compare: does architecture ranking hold across tasks?
- [ ] Document: cross-dataset performance analysis

---

## Stage 9.6 — Paper Candidate Assessment

**Goal**: Determine if results justify a paper.

- [ ] Compare all 5 architectures across 3 tasks
- [ ] Analyze: which architecture is best for which task?
- [ ] Analyze: RTX 4070 optimal configuration
- [ ] Draft paper outline based on [[writing_seismic_seg_survey]]
- [ ] Decision: proceed to paper writing? Or need more experiments?

---

## Priority Reference

| Experiment | Priority | Stage |
|-----------|----------|-------|
| Dataset pipeline | **P1** | 9.1–9.2 |
| U-Net baseline | **P2** | 9.3 |
| SegFormer baseline | **P2** | 9.4 |
| Cross-dataset validation | **P2** | 9.5 |
| Paper assessment | **P1** | 9.6 |
| PhaseNet reproduction | **P3** | not in Stage 9 |
| EQTransformer reproduction | **P3** | not in Stage 9 |

---
**See**: [[Research_Roadmap]] for full priority framework and dependency graph.