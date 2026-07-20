---
dataset_name: "Northern California Seismic Network"
domain: "Seismology / Earthquake Monitoring"
size: "~3M relocated events"
modality: "Relocated earthquake catalog + raw waveforms"
task: [phase-association, earthquake-detection, earthquake-location]
official_link: "https://bayarea.usgs.gov/"
related_papers: [mcbrearty2023_genie_note, si2024_plan_allinone_note, mousavi2020_eqtransformer_note]
source_type: mentioned_in_paper
tags: [northern-california, usgs, baysource, ml-ready, genies-dataset, plan-dataset]
created: 2026-07-19
---

# Dataset Overview / 数据集概述

The Northern California Seismic Network (NCSN), operated by USGS and affiliated institutions, is one of the world's densest and longest-running regional seismic networks. The dataset used by GENIE (Mousavi & Beroza 2023) consists of a catalog of ~3 million relocated earthquake events in Northern California, derived from decades of continuous monitoring.

- **Source / 来源**: USGS Northern California Seismic Network (NCSN); Bay Area Seismic Data Center (BASDC)
- **Purpose / 目的**: Regional earthquake monitoring; ML training for phase association and event detection
- **License / 许可**: Public domain (USGS data); redistribution permitted with attribution

# Data Format / 数据格式

- **File Format / 文件格式**: 
  - Catalog: CSV/SQLite with columns {event_id, lon, lat, depth, origin_time, magnitude, uncertainty}
  - Waveforms: SAC, MiniSeed (MSEED), or ASDF format (3-component: Z, N, E)
- **Directory Structure / 目录结构**: 
  ```
  NCSN/
    catalog/
      relocated_events.parquet    # ~3M events
      station_info.csv            # Station coordinates, network codes
    waveforms/
      BH[HZNE]/                   # Broadband vertical/north/east channels
        YYYY/MM/DD/HHMMSS.traces
  ```
- **Annotation Format / 标注格式**: 
  - Catalog events serve as ground truth for association/location evaluation
  - Manual phase picks from USGS analysts used as training labels
  - Synthetic events added for ML training (spiked waveforms at known locations)

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Train / 训练集 | ~2.5M events | Relocated catalog events (1984-2018); used for synthetic event generation |
| Val / 验证集 | ~100k events | Held-out real events for threshold tuning |
| Test / 测试集 | ~200k events | Recent events (2019-2021) for blind evaluation |

# Usage / 使用方式

- **Loading / 加载**: Parquet/CSV for catalog; ObsPy library for waveform loading
- **Preprocessing / 预处理**: 
  - Synthetic events created by spiking waveforms at known locations (GENIE training)
  - PhaseNet picks computed as input to GENIE association
  - Station adjacency built via K-nearest-neighbor (K=10 or K=15)
- **Data Location / 数据位置**: External; accessible via USGS BASDC API or AsDF archive

# Benchmark Results / 基准结果

| Method | Metric 1 | Metric 2 | Year |
|---|---|---|---|
| USGS Operational Catalog | Baseline | ~700k events detected | Ongoing |
| GENIE (Mousavi & Beroza, 2023) | ~96% re-detection rate | 4.2× more events than USGS | 2023 |
| PLAN (Si et al., 2024) | Multi-task joint optimization | Outperforms PhaseNet + Aggregated-GNN | 2024 |

# Related Papers / 相关论文

- [[mcbrearty2023_genie_note]] — Primary paper using this dataset; GENIE GNN-based associator
- [[si2024_plan_allinone_note]] — PLAN evaluated on this dataset alongside Japan Hi-net
- [[mousavi2020_eqtransformer_note]] — EQTransformer trained on synthetic events from this network

# Relationship to Current Research / 与当前研究的关系

**Provenance / 数据来源**:

- [x] Mentioned in paper only (仅在论文中出现)
- [ ] Personally used in experiments (已在实验中使用的数据集)
- [ ] Planned for use (计划使用的数据集)
- [ ] Reproduced from paper (复现的论文数据集)

**Notes / 说明**:

This dataset is referenced by GENIE, PLAN, and EQTransformer papers for phase association, earthquake detection, and location evaluation. It is NOT personally used in any ResearchAI experiment. Access requires USGS data download. The catalog is publicly available but waveform data may require registration.

# Limitations / 局限性

- Geographic coverage limited to Northern California; generalization to other tectonic settings unverified
- Catalog completeness varies by decade (earlier periods have fewer small events)
- Synthetic training data (spiked waveforms) may not capture all real-world complexities
- Station geometry is optimized for California; methods trained here may not transfer to sparse networks
- No surface deformation data (GPS/inSAR) included — limits aseismic slip analysis

## Tasks Using This Dataset / 使用该数据集的任务
- [[Phase Association]] — Used by GENIE for source-arrival assignment
- [[Earthquake Location]] — High-quality catalog for validation (~3M events)
- [[Earthquake Sequence Analysis]] — BayAreaQuakeCAT; ML-ready catalog
