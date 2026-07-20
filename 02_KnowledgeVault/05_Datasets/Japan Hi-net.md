---
dataset_name: "Japan Hi-net"
domain: "Seismology / Earthquake Monitoring"
size: "~100k catalog events; 700+ stations"
modality: "Continuous 3-component waveform catalog"
task: [phase-picking, phase-association, earthquake-location]
official_link: "https://www.hinet.bosai.go.jp/"
related_papers: [si2024_plan_allinone_note, zhu2018_phasenet_note]
source_type: mentioned_in_paper
tags: [japan, hi-net, dense-network, bosai, plan-dataset, phasenet-dataset]
created: 2026-07-19
---

# Dataset Overview / 数据集概述

Hi-net (High-sensitivity Seismic Observation Network) is a nationwide dense seismic network operated by Japan's National Research Institute for Earth Science and Disaster Resilience (NIED). It comprises over 700 stations deployed at ~150m depth in boreholes, providing exceptionally high-quality continuous seismic recordings across Japan.

- **Source / 来源**: NIED Hi-net network (https://www.hinet.bosai.go.jp/)
- **Purpose / 目的**: Nationwide earthquake monitoring; early warning system research; ML training for phase picking and association
- **License / 许可**: Public data (NIED); free access for research with registration

# Data Format / 数据格式

- **File Format / 文件格式**: 
  - Continuous waveforms: NWV (NIED proprietary binary); also available in MiniSeed
  - Catalog: CSV/SQLite with {event_id, lon, lat, depth, origin_time, magnitude}
  - Station metadata: CSV with station coordinates, depth, network code
- **Directory Structure / 目录结构**: 
  ```
  Hi-net/
    catalog/
      all_events.csv              # Full relocated catalog
      station_info.csv            # 700+ station coordinates
    waveforms/
      HH[ENZ]/                    # High-channel vertical/north/east
        YYYY/MM/HH.[NWV|MSEED]
  ```
- **Annotation Format / 标注格式**: 
  - Automated P/S picks from Hi-net operational pipeline
  - Manual review picks for catalog events
  - Synthetic events for ML training (spiked waveforms)

# Dataset Scale / 数据规模

| Split | Count | Description |
|---|---|---|
| Train / 训练集 | ~70k events | 2000-2015; used for PLAN synthetic training |
| Val / 验证集 | ~10k events | 2016-2017; threshold tuning |
| Test / 测试集 | ~15k events | 2018-2019; blind evaluation |

# Usage / 使用方式

- **Loading / 加载**: obspy.read() for NWV/MSEED; Pandas for catalog CSV
- **Preprocessing / 预处理**: 
  - Bandpass filter (1-20 Hz typical for phase picking)
  - Normalize each trace to zero mean, unit variance
  - 60-second windows centered on event origin time for training
  - Synthetic events created by spiking real waveforms at known locations
- **Data Location / 数据位置**: External; downloadable from NIED Hi-net archive (registration required)

# Benchmark Results / 基准结果

| Method | Metric 1 | Metric 2 | Year |
|---|---|---|---|
| PhaseNet (Zhu & Beroza, 2019) | P-wave F1 > 0.95 | S-wave F1 > 0.90 | 2019 |
| PLAN (Si et al., 2024) | Multi-station picking + location | Outperforms PhaseNet on Hi-net | 2024 |

# Related Papers / 相关论文

- [[si2024_plan_allinone_note]] — PLAN evaluated on Hi-net alongside Northern California
- [[zhu2018_phasenet_note]] — PhaseNet originally trained and tested on Hi-net

# Relationship to Current Research / 与当前研究的关系

**Provenance / 数据来源**:

- [x] Mentioned in paper only (仅在论文中出现)
- [ ] Personally used in experiments (已在实验中使用的数据集)
- [ ] Planned for use (计划使用的数据集)
- [ ] Reproduced from paper (复现的论文数据集)

**Notes / 说明**:

Hi-net is referenced by PLAN and PhaseNet papers as a benchmark dataset for phase picking and multi-station association. The borehole deployment at ~150m depth provides superior signal quality compared to surface stations, making it ideal for ML training. This dataset is NOT personally used in any ResearchAI experiment. Download requires NIED registration.

# Limitations / 局限性

- Japan-specific tectonic setting (subduction zone); methods may not transfer to strike-slip (California) or rift settings
- Dense network (700+ stations) is not representative of sparse regional networks
- Borehole deployment reduces cultural noise but adds depth-related corrections
- Catalog coverage is biased toward high-seismicity regions (more data in eastern Japan)
- No surface deformation data included

## Tasks Using This Dataset / 使用该数据集的任务
- [[Phase Association]] — High-density network; used by PLAN
- [[Earthquake Location]] — Dense network; excellent for location testing
