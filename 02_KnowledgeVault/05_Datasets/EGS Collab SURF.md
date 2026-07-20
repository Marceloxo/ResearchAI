---
dataset_name: "EGS Collab SURF"
domain: "Seismic / Enhanced Geothermal Systems"
size: "69,444 waveforms from 1,932 events"
modality: "Three-component seismograms"
task: ["Seismic Phase Picking", "Microseismic Monitoring"]
official_link: "https://www.egscollab.org/"
related_papers: ["Chai et al. (2020)", "Schoenball et al. (2020)"]
tags: [seismic, egs, microseismic, benchmark]
source_type: public_dataset
created: 2026-07-09
---

# Dataset Overview
EGS Collab SURF Experiment 1 is a meter-scale hydraulic fracturing monitoring dataset from the Sanford Underground Research Facility in South Dakota. It was used to demonstrate transfer learning for seismic phase picking.

- **Source**: EGS Collab Project
- **Purpose**: Hydraulic fracturing monitoring at meter scale
- **License**: Research use

# Data Format
- **File Format**: Seismogram waveforms (3-component)
- **Sampling Rate**: 100kHz
- **Sensor Array**: 35 sensors (24 hydrophones + 12 accelerometers) in 6 boreholes
- **Monitoring Volume**: 77脳83脳40m

# Dataset Scale
| Split | Count | Description |
|---|---|---|
| Total Waveforms | 69,444 | From 1,932 triggered events |
| Events (May 2018) | ~400+ | Multiple stimulations |
| Events (June 2018) | ~400+ | Single stimulation |
| Events (Dec 2018) | ~400+ | Multiple stimulations |

# Usage
- **Loading**: Standard seismogram format
- **Preprocessing**: Bandpass filter 3-20kHz recommended
- **Data Location**: `D:\ResearchAI_Data\Datasets\EGS_Collab_SURF\`

# Benchmark Results
| Method | P Precision | S Precision | Notes |
|---|---|---|---|
| TL Model | High | High | +10% over original PhaseNet |
| Original PhaseNet | Good | Good | Baseline DNN |
| AR Picker | Low | Low | Traditional |

# Related Papers
- [[chai2020_using_note]] 鈥?Primary paper using this dataset
- [[Schoenball_et_al_2020]] 鈥?Original seismic catalog processing

# Limitations
- Specific to meter-scale EGS system
- 100kHz sampling rate not typical for most seismic monitoring
- Limited geographic/geological context (single site)

## Tasks Using This Dataset / 使用该数据集的任务
- [[Phase Picking]] — Meter-scale hydraulic fracturing monitoring; 69,444 waveforms
