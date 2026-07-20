# Stage 5.5 — Paper Processing Registry Design Report

> **Generated**: 2026-07-17 23:42
> **Purpose**: Automated registry of all Zotero papers and their processing state
> **Output**: `Paper_Processing_State.yaml`

---

## 1. Design Overview

The Paper Processing Registry is a single YAML file that tracks every paper in the ResearchAI pipeline:

```
Zotero DB → Paper_Processing_State.yaml → Agent decisions
```

**Key properties:**
- **Read-only scan**: Does not modify Zotero, MinerU, or KnowledgeVault
- **Auto-generated**: Produced by scanning both databases
- **Machine-readable**: YAML format for Agent consumption
- **Source of truth**: Replaces manual tracking in MinerU_Zotero_Mapping.md

---

## 2. Current State Snapshot

| Metric | Count |
| --- | --- |
| Total Zotero papers | 33 |
| PDFs available | 27 |
| MinerU complete (full.md + images/) | 27 |
| MinerU partial | 0 |
| MinerU pending | 6 |

### Papers by State

#### MinerU Complete (27 papers)
All required files present: `full.md` + `images/`

| Paper Key | Title | MinerU Folder |
|---|---|---|
| 3HB6LAR9 | LandslideSegNet: an effective deep learning networ | Şener和Ergen - 2024 - LandslideSegNet an effective deep learn... |
| 43PF2JMB | Machine-Learning-Based High-Resolution Earthquake  | Tan 等 - 2021 - Machine-Learning-Based High-Resolution Earthq... |
| 5JGQ7YTL | A high-resolution seismic catalog for the 2021 MS6 | Zhou 等 - 2021 - A high-resolution seismic catalog for the 20... |
| 5L2QLL47 | Using a Deep Neural Network and Transfer Learning  | Chai 等 - 2020 - Using a Deep Neural Network and Transfer Lea... |
| 6HWKP8EC | A deeply supervised image fusion network for chang | Zhang 等 - 2020 - A deeply supervised image fusion network fo... |
| 79AR33SX | BUILDING DISASTER DAMAGE ASSESSMENT IN SATELLITE I | Weber和Kan - 2020 - BUILDING DISASTER DAMAGE ASSESSMENT IN SA... |
| 7JZTDVB3 | An all-in-one seismic phase picking, location, and | Si 等 - 2024 - An all-in-one seismic phase picking, location,... |
| 89DCUBSH | High-resolution seismicity imaging and early after | Ding 等 - 2023 - High-resolution seismicity imaging and early... |
| 8PQBD3RU | Seismic Facies Segmentation via a Segformer-Based  | Seismic Facies Segmentation via a Segformer-Based Specific E... |
| CY43XIQN | Automated deformation detection and interpretation | Abdallah 等 - 2024 - Automated deformation detection and inte... |
| D98KRK3B | Machine‐Learning‐Based Analysis of the Guy‐Greenbr | Park 等 - 2020 - Machine‐Learning‐Based Analysis of the Guy‐G... |
| FAA4JYRC | Rapid Characterization of the July 2019 Ridgecrest | Liu 等 - 2020 - Rapid Characterization of the July 2019 Ridge... |
| FGFVQ8EP | Landslide Detection and Segmentation Using Remote  | 2312.16717v1.pdf-02e09c3b-9eb7-431d-bd0a-4f99cd221909... |
| JCKZQTYW | DTPP:An efficient depthwise separable TCN for seis | Lv和Peng - 2026 - DTPPAn efficient depthwise separable TCN fo... |
| JM2US4DM | Deep Learning for Automatic Detection of Volcanic  | Liu 等 - 2025 - Deep Learning for Automatic Detection of Volc... |
| KGC7EEQX | 3D fault architecture controls the dynamism of ear | Ross 等 - 3D fault architecture controls the dynamism of eart... |
| LY282M9N | Remote Sensing Image Change Detection With Transfo | Chen 等 - 2022 - Remote Sensing Image Change Detection With T... |
| N7UP2CZT | A Transformer-Based Siamese Network for Change Det | Bandara和Patel - 2022 - A Transformer-Based Siamese Network f... |
| RIGVWYL3 | Seismological Characterization of the 2021 Yangbi  | Zhou 等 - 2022 - Seismological Characterization of the 2021 Y... |
| SQT45NJU | Hybrid lightweight transformer for efficient lands | Yadav 等 - 2025 - Hybrid lightweight transformer for efficien... |
| TSQGFMA2 | SNUNet-CD: A Densely Connected Siamese Network for | Fang 等 - 2022 - SNUNet-CD A Densely Connected Siamese Networ... |
| VDGWT3R3 | Earthquake Phase Association with Graph Neural Net | McBrearty和Beroza - 2023 - Earthquake Phase Association with ... |
| VSG3K538 | PhaseNet: A Deep-Neural-Network-Based Seismic Arri | Zhu和Beroza - 2018 - PhaseNet A Deep-Neural-Network-Based Sei... |
| XYZBCLGH | Machine Learning in Earthquake Seismology | Mousavi和Beroza - 2023 - Machine Learning in Earthquake Seism... |
| YQDJU2Y6 | Landslide4Sense: Reference Benchmark Data and Deep | Ghorbanzadeh 等 - 2022 - Landslide4Sense Reference Benchmark ... |
| YUB9FY6Q | Literature review on deep learning for the segment | Literature review on deep learning for the segmentation of s... |
| ZN6HHVJ7 | Earthquake transformer—an attentive deep-learning  | Mousavi 等 - 2020 - Earthquake transformer—an attentive deep-... |

#### MinerU Pending (6 papers)
PDF exists but no MinerU output folder found.

| Paper Key | Title | PDF Exists |
|---|---|---|
| FL6TSZPA | QuakeFlow: a scalable machine-learning-based earth | No |
| H9LQNVTM | Generalized Seismic Phase Detection with Deep Lear | No |
| II3UGDYS | SeisBench -- A Toolbox for Machine Learning in Sei | No |
| PW86NPCG | OBSTransformer: a deep-learning seismic phase pick | No |
| YW7ADGN9 | CRED: A Deep Residual Network of Convolutional and | No |
| YXFR9DZT | PickBlue: Seismic Phase Picking for Ocean Bottom S | No |

#### No PDF (6 papers)
Paper exists in Zotero but PDF not found in storage.

| Paper Key | Title |
|---|---|
| FL6TSZPA | QuakeFlow: a scalable machine-learning-based earth |
| H9LQNVTM | Generalized Seismic Phase Detection with Deep Lear |
| II3UGDYS | SeisBench -- A Toolbox for Machine Learning in Sei |
| PW86NPCG | OBSTransformer: a deep-learning seismic phase pick |
| YW7ADGN9 | CRED: A Deep Residual Network of Convolutional and |
| YXFR9DZT | PickBlue: Seismic Phase Picking for Ocean Bottom S |

---

## 3. YAML Schema

```yaml
registry:
  version: '1.0'
  generated: 'ISO-8601 timestamp'
  source: 'Stage 5.5 automated scan'
  zotero_db: '/path/to/zotero.sqlite'
  mineru_md: '/path/to/MinerU_md'
  knowledgevault_dir: '/path/to/KV/01_Papers'

summary:
  total_zotero_papers: N
  pdfs_available: N
  mineru_complete: N
  mineru_partial: N
  mineru_pending: N
  knowledgevault_processed: N
  knowledgevault_pending: N

papers:
  - paper_key: 'XXX'
    att_key: 'YYY'
    title: 'Paper Title'
    type: 'journalArticle'
    date_added: 'YYYY-MM-DD HH:MM:SS'
    pdf_exists: true/false
    mineru_folder: 'Folder name or null'
    mineru_state: 'MINERU_COMPLETE|MINERU_PARTIAL|MINERU_PENDING'
```

---

## 4. Agent Skill Integration Proposal

### Proposed Skill: `Registry_Scan`

**Purpose**: Allow any agent to query the current processing state of all papers.

**Integration Points:**

1. **Batch Processing Pre-Check**
   - Before running `batch_process.py`, scan `Paper_Processing_State.yaml`
   - Identify papers with `mineru_state: MINERU_PENDING` and `pdf_exists: true`
   - Auto-generate processing queue

2. **Duplicate Prevention**
   - Check `mineru_folder` field before creating new output
   - Prevent re-processing of `MINERU_COMPLETE` papers

3. **KnowledgeVault Gap Analysis**
   - Compare `papers[]` entries against `02_KnowledgeVault/01_Papers/`
   - Generate list of papers that have MinerU output but no KV notes

4. **Automated Status Updates**
   - After each paper is processed, update `mineru_state` in YAML
   - No manual registry maintenance required

### Example Agent Workflow

```
1. Agent receives task: "Process all unprocessed papers"
2. Reads Paper_Processing_State.yaml
3. Filters: mineru_state == MINERU_PENDING AND pdf_exists == true
4. Generates processing queue
5. Runs batch_process.py --execute
6. Re-scans registry to update states
7. Reports completion
```

### File Placement

```
08_Agent_Config/
├── Paper_Processing_State.yaml    ← Auto-generated, read by agents
├── Skills/
│   ├── SKILL_Registry_Scan.md     ← New skill definition
│   └── SKILL_Batch_Process.md     ← Updated to use registry
```

---

## 5. Maintenance

**Regeneration**: Run the scan script whenever:
- New papers are added to Zotero
- Batch MinerU processing completes
- Manual state corrections are needed

**Automation candidate**: This scan can be wrapped as a Codex skill for one-shot regeneration.

---

## 6. Files Created

| File | Purpose |
| --- | --- |
| `08_Agent_Config/Paper_Processing_State.yaml` | Main registry (auto-generated) |
| `08_Agent_Config/Migration/Stage_5.5_Report.md` | This report |

## 7. Files NOT Modified

- [x] Zotero database (read-only)
- [x] MinerU pipeline scripts (unchanged)
- [x] KnowledgeVault notes (unchanged)
- [x] Existing MinerU output folders (unchanged)
- [x] MinerU_Zotero_Mapping.md (unchanged — registry supersedes)

---

## 8. Next Steps

1. **Wrap scan as reusable script** → `04_Tools/mineru/scan_registry.py`
2. **Create SKILL_Registry_Scan.md** → Agent skill definition
3. **Integrate with batch_process.py** → Auto-update registry after processing
4. **Add KnowledgeVault gap detection** → Cross-reference with KV papers directory
