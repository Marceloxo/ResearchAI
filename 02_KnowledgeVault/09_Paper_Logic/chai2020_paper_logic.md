> **DEPRECATED: v1 format.** This file uses the old Paper Logic template (pre-Stage 1.5-4). Do not use for new papers. See chai2020_using_logic.md for the current Argument Mining format.
---
paper: "chai2020_using"
venue: "Geophysical Research Letters"
research_field: "Seismic Phase Picking"
tags: [paper-logic, transfer-learning, phasenet]
created: 2026-07-09
---

# Research Question
Can a deep neural network phase picker trained on kilometer-scale natural earthquake data be successfully transferred to meter-scale hydraulic fracturing monitoring data?

# Paper Story
```
Problem: Manual phase picking is labor-intensive
  鈫?Gap: DL pickers work on natural earthquakes but unknown on industrial/small-scale data
  鈫?Hypothesis: Transfer learning can bridge the scale gap with minimal retraining
  鈫?Method: TL-aided double-difference tomography (TADT) workflow
  鈫?Validation: Compare TL model vs AR picker, original PhaseNet, human expert
  鈫?Impact: Human-level accuracy at 1,900x speed, better seismic catalogs
```

# Introduction Logic

## Paragraph 1: Importance
Seismic monitoring is critical for oil/gas, mining, CCS, geothermal. Accurate locations depend on precise phase picking 鈥?a labor-intensive task.

## Paragraph 2: Existing Methods
Traditional auto-pickers (STA/LTA, AR-AIC) require human refinement. Recent DL pickers (PhaseNet) show remarkable accuracy for natural earthquakes but whether they work for industrial monitoring is unclear.

## Paragraph 3: Research Gap
Whether DL phase pickers generalize to industrial/small-scale data is unknown. Training from scratch requires huge labeled datasets.

## Paragraph 4: Our Solution
Apply PhaseNet to EGS Collab data + transfer learning to bridge the scale gap. Propose TADT workflow combining DL with double-difference tomography.

## Contribution Statement
1. Demonstrate successful transfer learning across 3 orders of magnitude in scale
2. Design TADT workflow combining TL with double-difference tomography
3. Show TL model outperforms original PhaseNet (+10%) and matches human performance

# Method Logic
```
Problem / 闂
    鈫?(scale mismatch between training and target data)
Motivation / 鍔ㄦ満 (need to adapt PhaseNet to meter-scale data)
    鈫?Design / 璁捐 (transfer learning with 3,500 retrained waveforms)
    鈫?Evidence / 璇佹嵁 (TL model beats original PhaseNet and matches human)
```

## Design Decisions
| Design Choice | Rationale | Evidence |
|---|---|---|
| Bandpass filter 3-20kHz | Removes system noise, improves DNN performance | Filtered data > raw data |
| Adam optimizer, lr=0.01 | Standard for DNN fine-tuning | Converges well |
| 100 epochs | Sufficient for convergence | F1 improves with more data |
| Exclude 9% incorrect picks | Remove bad training data | Visual inspection |

# Experiment Logic

## Research Question 1: Can PhaseNet be transferred across scales?
- **Experiment**: Apply original PhaseNet to EGS Collab data
- **Result**: Acceptable but not optimal
- **Claim Supported**: Transfer is possible but needs fine-tuning

## Research Question 2: Does transfer learning improve performance?
- **Experiment**: Retrain PhaseNet with 3,478 seismograms
- **Result**: +10% precision/recall over original PhaseNet
- **Claim Supported**: TL significantly improves performance

## Research Question 3: Does TL model match human performance?
- **Experiment**: Compare TL model vs 3 human analysts
- **Result**: TL model slightly better on S waves, slightly worse on P waves
- **Claim Supported**: TL achieves human-level performance

# Writing Lessons
- **Story Structure**: Clear problem 鈫?gap 鈫?hypothesis 鈫?method 鈫?validation 鈫?impact narrative
- **Figure Design**: Multiple comparison figures (TL vs AR vs PhaseNet vs Human)
- **Argument Flow**: Each claim supported by specific experiment
- **Language**: Direct, quantitative, avoids overclaiming



