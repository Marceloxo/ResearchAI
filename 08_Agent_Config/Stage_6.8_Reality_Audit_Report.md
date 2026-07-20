# Stage 6.8 — ResearchAI Reality Audit Report

**Date**: 2026-07-20
**Audit Type**: Read-Only
**Auditor**: Hermes Agent
**Status**: COMPLETE — No files modified

---

## Executive Summary

ResearchAI is a **mature, extensively iterated research infrastructure** with 60+ sub-stages of development. The core paper intake pipeline (Zotero → MinerU → KnowledgeVault) is functional and well-documented. However, the system has **significant gaps between reported progress and actual state**, migration residuals, and an incomplete downstream pipeline.

### Key Metrics

| Metric | Value |
|--------|-------|
| Total files in repo | ~400+ |
| KnowledgeVault nodes | 123 files |
| Papers processed | 27 cards + 15 notes + 2 surveys = 44 paper files |
| Methods | 12 |
| Tasks | 7 |
| Datasets | 11 |
| Paper Logic | 2 |
| Experiments | 1 |
| Ideas | 0 (README only) |
| Writing notes | 0 (README only) |
| 30+ backup files in git | 33 `.backup_linux_migration` files |
| BOM-affected files | 15 |
| CRLF-affected files | 9+ |
| Files with Windows paths | 30+ |
| Git remote | **None** |

### Top Risks

1. **Encoding contamination** — BOM and CRLF in core templates → every new note inherits the problem
2. **Windows path remnants** — 30+ files still reference `D:\ResearchAI_Data\` or `C:\ResearchAI\`
3. **Backup file pollution** — 33 `.backup_linux_migration` files committed to git
4. **Downstream pipeline stalled** — 0 ideas, 1 experiment, 0 writing notes after 44 paper files
5. **No git remote** — single point of failure

---

## 1. Current Architecture Status

### Data Flow Reality

```
Raw Data Layer
  Zotero: ✅ Installed at /usr/local/bin/zotero
  Zotero DB: ✅ /home/lco/Zotero/zotero.sqlite (1.1MB)
  Zotero Storage: ✅ /home/lco/Zotero/storage/ (populated)
  MinerU Scripts: ✅ 5 Python scripts in 04_Tools/mineru/
  MinerU Output: ✅ 38 directories at /home/lco/ResearchAI_Data/Paper/MinerU_md/
  ↓
Processed Literature
  Literature Cards: 27 files
  Paper Notes: 15 files
  Survey Notes: 2 files
  Paper Logic: 2 files (1 deprecated, 1 argument-mining)
  ↓
KnowledgeVault Core
  Methods: 12 nodes
  Tasks: 7 nodes
  Datasets: 11 nodes
  Topics: 1 node
  ↓
Research Map
  Meta/Navigation: 12 files (MOC, Index, Maps)
  ↓
Experiment System
  Experiments: 1 node (chai2020)
  Code Projects: 0 (README only in 03_Projects/)
  ↓
Paper Production
  Writing: 0 (README only in 06_Writing/ and 08_Writing/)
  Ideas: 0 (README only in 07_Ideas/)
```

### Architecture Verdict

| Layer | Design Goal | Actual | Status |
|-------|-------------|--------|--------|
| Raw Data | Zotero → MinerU pipeline | Installed, populated, verified | ✅ Complete |
| Processed Literature | Cards + Notes + Logic | 44 paper files across 3 types | ✅ Complete |
| KnowledgeVault Core | Methods, Tasks, Datasets | 30 nodes, schema partially inconsistent | ⚠️ Partial |
| Research Map | Navigation, MOC, Indexes | 12 files, all functioning | ✅ Complete |
| Experiment System | Code, tracking, results | 1 experiment node, 0 code projects | 🔴 Not Started |
| Paper Production | Drafts, writing | 0 notes, 0 drafts | 🔴 Not Started |

**The pipeline is front-loaded**: intake and knowledge extraction work well, but the downstream research output stages (experiments → ideas → writing) are essentially unimplemented.

---

## 2. Documentation vs Filesystem Verification

### Stage Report Cross-Check

| Stage | Report Claim | Actual Filesystem | Status |
|-------|-------------|-------------------|--------|
| **6.5.3** (Audit) | Read-only audit of schema | Report exists. No files modified. | ✅ Verified |
| **6.6.1** (Schema Repair) | Renamed `Segformer`→`SegFormer`, `U-Segformer-Hyper`→`U-SegFormer-Hyper`, removed stray `Multi-task`, fixed Paper_Index.md encoding, added OpenFWI.md backlink | `SegFormer.md` ✅, `U-SegFormer-Hyper.md` ✅, no stray `Multi-task` ✅, Paper_Index.md no BOM ✅, OpenFWI.md has backlink ✅ | ✅ Verified |
| **6.6.1** (Schema Repair — Not Modified) | "Task YAML `domain` field — confirmed correct, no action needed" | Tasks have `domain` ✅, but `related_methods` missing from ALL 7 tasks | ⚠️ Partial |
| **6.6.1** (Schema Repair — Not Modified) | "Dataset section names — confirmed consistent, no action needed" | Datasets have consistent sections ✅, but `related_tasks` missing from ALL 11 datasets | ⚠️ Partial |
| **6.6.1** (Schema Repair — Not Modified) | "Templates — immutable, no changes" | Templates unchanged ✅ | ✅ Verified |
| **6.6.2** (Wikilink Audit) | Read-only audit. Found 0 P0 issues, 1 orphan `[[Schoenball_et_al_2020]]` | 1 orphan still exists. No structural corruption. | ✅ Verified |
| **6.6.2** (Detected Issues) | Detected orchestrated placeholders (Paper - , Dataset - , Method - , Exp - ) | Present in templates and some notes — intentional design | ✅ Acceptable |
| **6.7** (Graph Connectivity) | Added `## Related Methods` section to `Seismic Phase Picking.md` with 4 wikilinks | File exists, 4 wikilinks added, 0 new nodes created | ✅ Verified |
| **1.5-7D.1** (Encoding Repair) | Fixed 9 files (5 P0, 4 P1) with GBK corruption | Backups in `_encoding_backup_20260710/`. But BOM (15 files) and CRLF (9 files) were NOT in scope. | ⚠️ Partial |
| **1.5-7D.4** (Output Standardization) | Standardized encoding | BOM and CRLF issues remain — these were not addressed | ⚠️ Partial |
| **1.5-7C.1** (Batch Processing) | 11 new papers processed | 11 cards + 5 notes + 2 surveys + 1 benchmark exist ✅ | ✅ Verified |
| **1.5-7C.3** (Template Alignment) | Added Zotero section to Survey_Template + 3 files | Survey_Template.md has Zotero section ✅ | ✅ Verified |
| **1.5-8A** (Skill System) | 8 skills created | Files exist in `08_Agent_Config/Skills/` ✅ | ✅ Verified |
| **1.5-8A** (Skill Installation) | "PENDING INSTALLATION" | Skills NOT installed into Codex/Hermes as of last report | ⚠️ Partial |

### Key Finding: Encoding Repair Was Incomplete

The Stage 1.5-7D.x encoding repair (7D.1–7D.4) **only addressed GBK corruption** (Chinese text encoded as ISO-8859-1, MacRoman, cp850, cp437, cp1250). It did **not** fix:

- **UTF-8 BOM** in 15 files
- **CRLF line endings** in 9+ files
- **Garbled Chinese** in `Paper_Template.md` (e.g. `璁烘枃绫诲瀷` instead of `论文类型`)

Both the Stage 1.5-7D.1 report and the `_encoding_backup_20260710/` directory confirm: the repair scope was limited to GBK corruption only.

---

## 3. Windows → Ubuntu Migration Audit

### Path Problems

**30+ files** still reference Windows paths. Distribution by category:

| Category | Count | Examples |
|----------|-------|---------|
| KnowledgeVault Datasets | 11 | `SEAM.md`, `Marmousi.md`, `F3 Netherlands.md` — all have `D:\ResearchAI_Data\` paths |
| KnowledgeVault Meta | 1 | `Dataset_Map.md` — has `D:\ResearchAI_Data\` |
| KnowledgeVault HumanRead | 3 | `current_v1.0.md`, `v2.0.md`, `v2.0_中文介绍.md` — have `C:\ResearchAI\` + `D:\ResearchAI_Data\` |
| KnowledgeVault Vault_README | 1 | References `C:\ResearchAI\` |
| Core Agent Config | 2 | `AGENT_BOOTSTRAP.md` (`D:\ResearchAI_Data\`), `PROJECT_STATUS.md` (`D:\ResearchAI_Data\`) |
| Literature | 1 | `01_Literature/README.md` — architecture diagram uses `D:\ResearchAI_Data\` |
| Agent Reports | 10+ | `Workspace_Cleanup_Plan.md`, `Zotero_Test_Plan.md`, various `Migration/*.md` |
| **Total** | **30+** | |

### Critical path files (first-read by agents)

| File | Old Path | Severity |
|------|----------|----------|
| `AGENT_BOOTSTRAP.md` | `D:\ResearchAI_Data\` | 🔴 Every agent reads this first |
| `01_Literature/README.md` | `D:\ResearchAI_Data\Zotero\storage\`, `D:\ResearchAI_Data\Paper\MinerU_md\` | 🔴 Architecture reference |
| `02_KnowledgeVault/Vault_README.md` | `C:\ResearchAI\` | 🟠 Vault conventions doc |

### Zotero Data Path

- **Old**: `D:\ResearchAI_Data\Zotero\storage\`
- **Current**: Zotero data is at `/home/lco/Zotero/` (with `zotero.sqlite` and `storage/`) AND cross-linked to `/home/lco/ResearchAI_Data/Zotero/`
- **Issue**: The `research_config.yaml` correctly points to `/home/lco/ResearchAI_Data/`, but some migration reports reference the Windows Zotero path

### Codex Migration

| Component | Old Location (Windows) | Current Location (Linux) | Status |
|-----------|----------------------|------------------------|--------|
| Skills | `C:\ResearchAI\08_Agent_Config\Skills\` | `08_Agent_Config/Skills/` | ✅ Files exist, but NOT installed |
| Codex sessions | `~/.codex/sessions/` | `~/.codex/sessions/` | ✅ Session logs found |
| Codex config | `~/.codex/config.toml` | `~/.codex/config.toml` | Not checked |
| Codex skills | `~/.codex/skills/researchai/` | `~/.codex/skills/researchai/` | ✅ SKILL.md exists |
| Project `.codex/` dir | `C:\ResearchAI\.codex\` | `/home/lco/ResearchAI/.codex/` | ⚠️ Empty directory |
| Project `.agents/` dir | `C:\ResearchAI\.agents\` | `/home/lco/ResearchAI/.agents/` | ⚠️ Empty directory |

### Backup File Pollution

**33 `.backup_linux_migration` files** are committed to git:

| Location | Count | Notes |
|----------|-------|-------|
| Root files | 5 | AGENT_BOOTSTRAP, PROJECT_STATUS, README, research_config.yaml (×2) |
| Templates | 10 | Every template has a backup |
| Vault_README | 1 | |
| Zotero docs | 6 | Every Zotero doc has a backup |
| Skills | 5 | 4 literature skills + INSTALL_INSTRUCTIONS |
| researchai references | 4 | paper_intake, paper_deep_read, paper_batch_process, survey_process |
| Data_Flow_Architecture | 1 | |
| paper_logic | 1 | |
| **Total** | **33** | |

These are **dead weight** — the originals are already migrated.

---

## 4. Encoding Status

### Full Scan Results

| Encoding Issue | Count | Affected Paths |
|---------------|-------|---------------|
| UTF-8 BOM | 15 files | Templates (2), Papers (3), Paper Logic (2), Agent Config (6), Literature Index (1), Tools (1) |
| CRLF line endings | 9+ files | AGENT_BOOTSTRAP.md, Templates (2), Papers (5), Paper Logic (1) |
| GBK corruption | 0 (fixed) | 9 files repaired in Stage 1.5-7D.1 |
| Garbled Chinese | 1 file | `Paper_Template.md` — has `璁烘枃绫诲瀷` (should be `论文类型`) |

### BOM Files (Complete List)

```
02_KnowledgeVault/Templates/Literature_Card_Template.md
02_KnowledgeVault/Templates/Paper_Template.md
02_KnowledgeVault/01_Papers/monteiro2024_deep_learning_card.md
02_KnowledgeVault/01_Papers/mousavi2023_machine_learning_card.md
02_KnowledgeVault/01_Papers/zhu2018_phasenet_card.md
02_KnowledgeVault/09_Paper_Logic/chai2020_paper_logic.md
02_KnowledgeVault/09_Paper_Logic/chai2020_using_logic.md
01_Literature/04_Literature_Index/Literature_Index.md
04_Tools/Data_Storage_Architecture.md
08_Agent_Config/Literature_Intake_Workflow.md
08_Agent_Config/MinerU_Zotero_Mapping.md
08_Agent_Config/Paper_File_Naming_Rules.md
08_Agent_Config/Stage_1.5_6B_Real_Paper_Stress_Test.md
08_Agent_Config/Stage_1.5_7C1_Batch_Processing_Report.md
08_Agent_Config/Stress_Test_Execution_Log.md
```

**Impact**: Every new paper note created with `Literature_Card_Template.md` or `Paper_Template.md` inherits BOM. This is a **self-propagating encoding problem**.

### CRLF Files (Complete List)

```
AGENT_BOOTSTRAP.md
02_KnowledgeVault/Templates/Literature_Card_Template.md
02_KnowledgeVault/Templates/Paper_Template.md
02_KnowledgeVault/01_Papers/mousavi2023_machine_learning_card.md
02_KnowledgeVault/01_Papers/zhang2020_ds_ifn_cd_card.md
02_KnowledgeVault/01_Papers/zhu2018_phasenet_card.md
02_KnowledgeVault/01_Papers/zhang2020_ds_ifn_cd_note.md
02_KnowledgeVault/01_Papers/monteiro2024_deep_learning_card.md
02_KnowledgeVault/01_Papers/lv2026_dttp_note.md
```

---

## 5. Schema Status

### Methods — YAML Frontmatter

| Field | Expected | Actual | Missing Count |
|-------|----------|--------|---------------|
| `method_name` | ✓ | All 12 methods have it | 0 |
| `category` | ✓ | All 12 methods have it | 0 |
| `application` | ✓ | All 12 methods have it | 0 |
| `related_tasks` | ✓ | All 12 methods have it | 0 |
| `tags` | ✓ | All 12 methods have it | 0 |
| `created` | ✓ | All 12 methods have it | 0 |

**Verdict**: ✅ **Consistent** — all methods follow the template.

### Tasks — YAML Frontmatter

| Field | Expected | Actual | Missing Count |
|-------|----------|--------|---------------|
| `task_name` | ✓ | All 7 tasks have it | 0 |
| `domain` | ✓ | All 7 tasks have it | 0 |
| `related_methods` | Template specifies this | **ZERO tasks have it** | **7/7** |
| `related_datasets` | Not in template, but implied | **ZERO tasks have it** | **7/7** |
| `input` | Template specifies | **ZERO tasks have it** | **7/7** |
| `output` | Template specifies | **ZERO tasks have it** | **7/7** |
| `metrics` | Template specifies | **ZERO tasks have it** | **7/7** |
| `created` | Template specifies | **ZERO tasks have it** | **7/7** |

**Verdict**: 🟠 **Inconsistent** — tasks are missing key relational and metadata fields.

### Datasets — YAML Frontmatter

| Field | Expected | Actual | Missing Count |
|-------|----------|--------|---------------|
| `dataset_name` | ✓ | All 11 datasets have it | 0 |
| `domain` | ✓ | All 11 datasets have it | 0 |
| `source_type` | ✓ | All 11 datasets have it | 0 |
| `tags` | ✓ | All 11 datasets have it | 0 |
| `related_tasks` | Template specifies | **ZERO datasets have it** | **11/11** |
| `related_papers` | Template specifies | **ZERO datasets have it** | **11/11** |
| `size` | Template specifies | **ZERO datasets have it** | **11/11** |
| `modality` | Template specifies | **ZERO datasets have it** | **11/11** |
| `task` | Template specifies | **ZERO datasets have it** | **11/11** |
| `official_link` | Template specifies | **ZERO datasets have it** | **11/11** |

**Verdict**: 🟠 **Inconsistent** — datasets are missing key relational fields.

### Template vs Reality Gap

| Template | Fields in Template | Fields Used in Actual Nodes | Match |
|----------|-------------------|---------------------------|-------|
| `Method_Template.md` | 6 fields | 6 fields | ✅ Full |
| `Task_Template.md` | 8 fields | 2 fields (`task_name`, `domain`) | ❌ Partial |
| `Dataset_Template.md` | 10 fields | 4 fields (`dataset_name`, `domain`, `source_type`, `tags`) | ❌ Partial |

---

## 6. Knowledge Graph Status

### Bidirectional Connectivity Analysis

**Method ↔ Task**

| Direction | Connected | Broken |
|-----------|-----------|--------|
| Method → Task (via `related_tasks`) | ✅ 12/12 methods | 0 |
| Task → Method (via `related_methods`) | ❌ 0/7 tasks | **7** |

Analysis: Tasks know which methods they use (via wikilinks in content), but this is NOT reflected in YAML frontmatter. The `related_methods` field is entirely absent from the schema.

**Task ↔ Dataset**

| Direction | Connected | Broken |
|-----------|-----------|--------|
| Task → Dataset (via wikilinks) | ✅ 6/7 tasks reference datasets | 1 (Earthquake Sequence Analysis doesn't reference any dataset) |
| Dataset → Task (via wikilinks) | ✅ 9/11 datasets reference tasks | 2 (OpenFWI, Parihaka only reference `[[Paper - ]]` placeholder) |

Analysis: Content-level connectivity is reasonable. The gap is in YAML frontmatter — no `related_tasks` field in any dataset.

**Dataset ↔ Paper**

| Direction | Connected | Notes |
|-----------|-----------|-------|
| Dataset → Paper (via wikilinks) | ✅ 5/11 datasets reference specific papers | Others use `[[Paper - ]]` placeholder |
| Paper → Dataset (via wikilinks) | ⚠️ Minimal | Most papers only reference methods/tasks, not datasets |

### Wikilink Integrity

| Category | Count | Description |
|----------|-------|-------------|
| Real broken links | **1** | `[[Schoenball_et_al_2020]]` |
| Intentional placeholders | ~10 | `[[Paper - ]]`, `[[Dataset - ]]`, `[[Method - ]]` — template stubs |
| Case issues | 0 | No `Segformer` vs `SegFormer` problems (fixed in 6.6.1) |
| Total unique wikilinks | 216 | Across entire KnowledgeVault |

### Files with Spaces in Names

**19 files** have spaces in filenames — all in KnowledgeVault core directories:

- `03_Methods/` (4 files): `Attention Mechanism.md`, `Multi-task Learning.md`, `Transfer Learning.md`, `Vision Transformer.md`
- `04_Tasks/` (7 files): `Earthquake Location.md`, `Earthquake Sequence Analysis.md`, `Fault Segmentation.md`, `Phase Association.md`, `Seismic Facies Segmentation.md`, `Seismic Image Segmentation.md`, `Seismic Phase Picking.md`
- `05_Datasets/` (5 files): `EGS Collab SURF.md`, `F3 Netherlands.md`, `Japan Hi-net.md`, `Northern California Seismic Network.md`, `SEG Salt.md`
- Others (3 files): `Seismic AI.md`, `paper link.md`, `ResearchAI Skill System Initialization.md`

**Impact**: Spaces in filenames cause issues with git, shell commands, URL encoding, and some Linux tools. Obsidian handles them natively, but they add friction for AI agent tooling.

---

## 7. Agent System Status

### 08_Agent_Config Overview

| Subdirectory | File Count | Notes |
|-------------|-----------|-------|
| Top-level `.md` files | 62 | Core config, stage reports, workflow docs |
| `command Prompt/` | 17 | Historical task prompts (Stages 5–6) |
| `Migration/` | 22 | Windows→Linux migration reports |
| `Skills/` | 34 | 8 skills (flat format) + 8 (researchai MCP format) + backups |
| `_encoding_backup_20260710/` | 9 | Pre-repair backups |
| Other files | 3 | `Paper_Processing_State.yaml` (507 lines), `_semantic_audit_data.json`, `README.md` |
| **Total** | **147** | |

### Key Issues

1. **Dual skill system**: Skills exist in two parallel formats:
   - `08_Agent_Config/Skills/01_Literature/` — flat `.md` files (Paper Intake, Deep Read, Batch Process, Update)
   - `08_Agent_Config/Skills/researchai/` — Codex MCP format (SKILL.md + references/)
   - These are **not synchronized** — different content, different structure

2. **Skills not installed**: Stage 1.5-8A explicitly states "PENDING INSTALLATION". The 8 flat skills exist as files but are not registered in any agent system.

3. **Codex `researchai` skill**: A separate copy exists at `~/.codex/skills/researchai/SKILL.md`. It has a known failure: `unknown MCP server 'skill:researchai'` — the MCP reference is broken.

4. **Empty agent directories**: `.codex/`, `.agents/`, `08_Agent_Config/.codex/`, `08_Agent_Config/.agents/` — all empty stubs.

5. **Command Prompt bloat**: 17 historical stage prompts (Stages 5.1–6.8) are retained. No cleanup policy.

---

## 8. Git Status

| Metric | Value |
|--------|-------|
| Branch | `master` (single branch) |
| Remote | **None** |
| Total commits | 4 |
| Latest commit | `027d30a` (2026-07-20) |
| .gitignore | **None** |
| Working tree | Clean (1 untracked file: this audit prompt) |
| Backup files in git | 33 `.backup_linux_migration` files |
| Binary files in git | `.obsidian/plugins/plugins.tar` (12MB), `main.js` files (20K+ lines each) |

### Commit Analysis

```
027d30a chore: localize obsidian and bib paths, add seismic fault reference
  → 213 files changed, 164,723 insertions — HUGE commit
  → Includes: all Obsidian plugins (binary), all KnowledgeVault nodes, all MinerU scripts, all backup files
b594fe9 stage 1.5-8
ba4185b Stage 1.5-6F.1 Cleanup done
fc1f2f9 Initial commit
```

### Issues

1. **No remote**: No backup, loss risk.
2. **No .gitignore**: Binary files, `.pyc`, `__pycache__`, `plugins.tar`, backup files committed.
3. **Massive single commit**: 164K insertions in one commit — impossible to review or bisect.
4. **Binary plugin files**: `plugins.tar` (12MB) and `main.js` files (100K+ lines each) are committed. These should be platform-managed, not versioned.
5. **Backup files in git**: 33 `.backup_linux_migration` files permanently versioned.

---

## 9. Original Goal Alignment

### Original Design Goals

| Goal | Current Status | Assessment |
|------|---------------|------------|
| **1. Literature Intelligence** — acquire, screen, and organize papers | ✅ 44 paper files, 27 cards + 15 notes + 2 surveys, Zotero pipeline | **Complete** |
| **2. Deep Reading Automation** — automated paper analysis | ✅ 15 notes + 2 paper logic files, argument mining framework | **Complete** |
| **3. Knowledge Graph Construction** — methods, tasks, datasets connected | ⚠️ 30 nodes, but schema gaps (no `related_methods`/`related_tasks`) and weak bidirectional connectivity | **Partial** |
| **4. Research Direction Discovery** — identify gaps, form hypotheses | ❌ 0 idea nodes, 0 research gap analyses | **Not Started** |
| **5. Experiment Management** — track experiments, reproduce baselines | ❌ 1 experiment node, 0 code projects, 0 baselines | **Not Started** |
| **6. Paper Production** — writing pipeline, draft generation | ❌ 0 writing notes, 0 drafts | **Not Started** |

### Current Focus as Documented

The project claims focus on **Seismic AI + Deep Learning**. The KnowledgeVault content confirms this:

- **Seismic AI papers**: PhaseNet, EQTransformer, GENIE, PLAN, DTTP, Ridgecrest catalog — 15+ seismic papers
- **Remote sensing papers**: ChangeFormer, SNUNet-CD, InSAR — 8+ papers from batch processing
- **Landslide detection papers**: Landslide4Sense, Le2023, Yadav2025 — 5+ papers
- **Seismic facies**: Wang2024 (SegFormer), U-SegFormer-Hyper — 2 papers

**Observation**: The batch processing (Stage 1.5-7C.1) added 11 papers, but many are **remote sensing / change detection** (not seismic AI). The KnowledgeVault has drifted from pure seismic AI toward broader geoscience / remote sensing. This may be intentional (the project scope allows general geoscience), but it's worth noting.

### Maximum Risk

**The greatest risk is that the system is "architecturally frozen" but technically unstable.** The architecture freeze (Stage 1.5-7B) prevents directory changes, but the encoding problems, schema gaps, and path remnants mean every new agent session faces the same issues:

1. Agent reads `AGENT_BOOTSTRAP.md` → sees `D:\ResearchAI_Data\` → confused
2. Agent creates new paper note → inherits BOM from template → propagates encoding problem
3. Agent tries to navigate via `related_methods` in tasks → field doesn't exist → weak graph
4. Agent finds 30+ backup files → wastes context on irrelevant files

---

## 10. Recommended Next Steps

### Immediate (P0 — Blocking)

1. **Fix template encoding**: Remove BOM from `Literature_Card_Template.md` and `Paper_Template.md`. This stops the self-propagation of encoding issues.
2. **Fix Windows paths in AGENT_BOOTSTRAP.md**: Replace `D:\ResearchAI_Data\` with `/home/lco/ResearchAI_Data/`. This is the first file every agent reads.
3. **Remove backup files from git**: `git rm` all 33 `.backup_linux_migration` files.
4. **Create .gitignore**: Exclude backup files, `.pyc`, `__pycache__`, `plugins.tar`, `plugins/*/main.js`, `node_modules/`.

### High Priority (P1 — Before Batch Processing)

5. **Normalize CRLF→LF**: Fix 9+ files with CRLF line endings.
6. **Fix Paper_Template.md garbled Chinese**: The `璁烘枃绫诲瀷` corruption affects all new paper notes.
7. **Fix 01_Literature/README.md architecture diagram**: Replace `D:\ResearchAI_Data\` paths with Linux paths.
8. **Clean up 08_Agent_Config**: Archive historical reports, remove command prompts for completed stages.

### Medium Priority (P2 — Before Knowledge Graph Expansion)

9. **Add `related_methods` to Tasks**: Populate YAML frontmatter for all 7 task nodes.
10. **Add `related_tasks` to Datasets**: Populate YAML frontmatter for all 11 dataset nodes.
11. **Configure git remote**: Backup to GitHub/GitLab.
12. **Fix 12 KnowledgeVault dataset files**: Replace `D:\ResearchAI_Data\` paths with Linux paths.

### Low Priority (P3 — Future Cleanup)

13. **Rename space-containing filenames** to underscores (e.g., `Attention Mechanism.md` → `attention_mechanism.md`).
14. **Remove empty directories**: `.agents/`, `.codex/`, `08_Agent_Config/.agents/`, `08_Agent_Config/.codex/`.
15. **Remove `outputtest.txt`** (106KB Codex session dump) from project root.
16. **Remove `ResearchAI Skill System Initialization.md`** from project root.

---

## Appendices

### A. 30+ Files with Windows Paths

See `Stage_7_Project_Audit_Report.md` (Appendix A) for complete list.

### B. 15 BOM Files

See `Stage_7_Project_Audit_Report.md` (Appendix B) for complete list.

### C. 19 Files with Spaces in Names

See `Stage_7_Project_Audit_Report.md` (Appendix C) for complete list.

### D. 33 Backup Files

See `Stage_7_Project_Audit_Report.md` (Appendix D) for complete list.

---

**Report End**

*This report was generated by Hermes Agent on 2026-07-20. All findings are based on actual file inspection. No files were modified during the audit.*