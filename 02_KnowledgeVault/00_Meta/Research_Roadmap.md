---
tags: [meta, roadmap, priority, navigation]
created: 2026-07-20
---

# ResearchAI Research Roadmap / 研究路线图

## Research Direction / 研究方向

### Primary: Deep Learning for Seismic Image Understanding

**Goal**: Develop and validate deep learning methods for seismic image segmentation (fault, facies, salt) using Transformer/CNN hybrid architectures, optimized for RTX 4070 (12GB VRAM).

**Core Tasks**:
- [[Seismic Image Segmentation]]
- [[Fault Segmentation]]
- [[Seismic Facies Segmentation]]

**Core Methods**:
- [[SegFormer]], [[U-SegFormer-Hyper]], [[Transformer]], [[CNN]], [[U-Net]]

**Core Datasets**:
- [[F3 Netherlands]], [[Thebe]], [[SEG Salt]], [[Parihaka]], [[Penobscot]], [[SEAM]], [[Marmousi]]

### Secondary: Seismic Phase Picking & Earthquake Monitoring

**Goal**: Baseline reproduction and methodology exploration for seismic phase picking. Not on the critical path for paper production.

**Core Tasks**:
- [[Seismic Phase Picking]], [[Phase Association]], [[Earthquake Location]]

**Core Methods**:
- [[PhaseNet]], [[EQTransformer]], [[GENIE]], [[PLAN]]

---

## Priority System / 优先级定义

| Level | Meaning | Resource Allocation | Gate |
|-------|---------|-------------------|------|
| **P0** | Active — currently being worked on | Highest priority, all resources | Must be in this stage |
| **P1** | Planned — ready to execute | Waiting for P0 prerequisites | Next in queue |
| **P2** | Designing — concept defined, plan needed | Requires experiment plan | After P1 |
| **P3** | Secondary — not on critical path | Low priority, explore when free | After P2 |
| **P4** | Deferred — postponed | No active work | Until re-evaluated |
| **Completed** | Executed and analyzed | Archived | — |

---

## Idea Priority / 想法优先级

### P0 — Active

(none yet — Stage 9 will start here)

### P1 — Planned

- [[idea_transformer_seismic_arch]] — Transformer architectures for seismic segmentation
  → **First paper candidate**: benchmark SegFormer, U-SegFormer-Hyper, U-Net on F3/Thebe/SEG Salt
  → Prerequisites: dataset pipeline, baseline experiment

### P2 — Designing

- [[idea_multi_task_seismic_interp]] — Multi-task seismic interpretation
  → Depends on: single-task baseline results from P1
- [[idea_transfer_learning_seismic]] — Transfer learning across scales for seismic DL
  → Depends on: P1 baseline established

### P3 — Secondary

- [[idea_self_supervised_seismic]] — SSL pre-training for seismic DL
  → Interesting but requires more data and compute than RTX 4070 can easily handle

### P4 — Deferred

- (none currently)

---

## Experiment Priority / 实验优先级

### P0 — Active

(none yet — Stage 9 will start here)

### P1 — Planned

- **Dataset Pipeline**: Build standardized data loading, preprocessing, and train/val/test split for F3 Netherlands, Thebe, SEG Salt, Parihaka
  → Prerequisite for ALL segmentation experiments
  → Estimated effort: 1-2 sessions

### P2 — Designing

- **Baseline: U-Net on F3 facies** — Reproduce basic U-Net result as lowest baseline
- **Baseline: SegFormer on F3 facies** — Reproduce wang2024 results as Transformer baseline
- **Benchmark: 5 architectures on 3 tasks** — Systematic comparison per [[idea_transformer_seismic_arch]]

### P3 — Secondary (not on critical path)

- [[exp_phasenet_repro]] — PhaseNet reproduction (seismic phase picking, not segmentation)
- [[exp_eqtransformer_repro]] — EQTransformer reproduction (seismic phase picking, not segmentation)

### Completed

- [[exp_chai2020_phase_picking]] — Chai 2020 transfer learning validation (historical record)

---

## Paper Pipeline / 论文管线

### First Paper Candidate (Target: ~2-3 months)

**Title**: "Benchmarking Transformer and CNN Architectures for Seismic Image Segmentation"

**Target Venue**: IEEE TGRS / GEOPHYSICS / SEG Annual Meeting

**Core Content**:
1. Systematic comparison of 5 architectures (U-Net, SegFormer, U-SegFormer-Hyper, Swin-T, ConvNeXt) on 3 tasks (facies, fault, salt)
2. Standardized evaluation protocol (same splits, same preprocessing, same metrics)
3. RTX 4070 resource profiling (memory, speed, accuracy trade-off)
4. Cross-dataset transfer analysis

**Prerequisites**:
- [ ] Dataset pipeline (P1)
- [ ] Baseline experiments (P2)
- [ ] Architecture benchmark (P2)
- [ ] Writing outline ([[writing_seismic_seg_survey]])

### Future Papers (Post-P1)

- Multi-task learning for seismic interpretation
- Transfer learning / domain adaptation for seismic segmentation
- Self-supervised pre-training for seismic DL

---

## Dependency Graph / 依赖关系

```
Dataset Pipeline (P1)
    ↓
U-Net Baseline (P2) → SegFormer Baseline (P2)
    ↓                         ↓
Architecture Benchmark (P2) ←─┘
    ↓
Paper Draft (P1 → Writing)
    ↓
Multi-task Learning (P2) → Transfer Learning (P2) → SSL Pre-training (P3)
```

---

## Current Stage Status

| Stage | Status | Description |
|-------|--------|-------------|
| Stage 0–6 | ✅ Complete | Infrastructure, pipeline, schema |
| Stage 6.8 | ✅ Complete | Reality audit, encoding fix |
| Stage 7 | ✅ Complete | Schema hardening, cleanup, skills |
| Stage 8 | ✅ Complete | Knowledge graph expansion, roadmap |
| **Stage 9** | **⬅️ Current** | **Dataset pipeline → Baseline → Paper candidate** |

---

## Navigation / 导航

- Back to [[Research_Map]]
- Explore [[Idea_Index]] for detailed idea descriptions
- Explore [[Experiment_Index]] for detailed experiment plans
- Explore [[Seismic_AI_Map]] for seismic AI knowledge graph