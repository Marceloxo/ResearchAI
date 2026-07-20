# Stage 6.2-6.3 Architecture Proposal

**Date**: 2026-07-18
**Type**: Design Proposal (READ-ONLY, no modifications)
**Prerequisites**: Stage 5.5 (Registry) + Stage 6.1 (agent_state) + Stage 6.1.1 (Audit)

---

## 1. Current Architecture State

### 1.1 Paper Processing Pipeline

```
Zotero DB (33 papers, 27 with PDFs)
    |
    | scan_registry.py
    v
Paper_Processing_State.yaml (agent_state tracking)
    |
    | batch_process.py + MinerU CLI
    v
MinerU_md/ (27 valid outputs: full.md + images/)
    |
    | process_paper.py (MANUAL — not in batch pipeline)
    v
KnowledgeVault/01_Papers/ (18/33 papers processed)
    |
    | scan_registry.py (re-scan)
    v
agent_state updated in registry
```

### 1.2 Current Coverage

| Stage | Count | Status |
|---|---|---|
| Zotero registered | 33 | 100% |
| PDFs available | 27 | 82% |
| MinerU processed | 27 | 100% of available PDFs |
| Literature Card | 11 | 41% of MinerU-complete |
| Deep Read Note | 7 | 26% of MinerU-complete |
| Method/Logic | 0 | Not started |
| Fully processed (card+note) | 5 | 19% of MinerU-complete |

### 1.3 Existing Skills

| Skill | Level | Coverage |
|---|---|---|
| SKILL_Paper_Intake.md | Level 1 | Literature Card generation |
| SKILL_Paper_Deep_Read.md | Level 2 | Deep Read Note generation |
| SKILL_Paper_Batch_Process.md | Level 1 | Batch card generation |
| SKILL_Paper_Update.md | Maintenance | Update existing records |
| SKILL_Knowledge_Node_Check.md | System | Prevent duplicate nodes |
| SKILL_Research_Map_Update.md | System | Update navigation maps |
| SKILL_Literature_Synthesis.md | Level 3 | Writing material generation |
| SKILL_Architecture_Audit.md | System | Read-only integrity checks |
| SKILL_Registry_Scan.md | System | Registry regeneration |

---

## 2. Stage 6.2: Config Path Remediation

### 2.1 Problem Statement

The architecture audit identified `research_config.yaml` as a HIGH risk item.
It contains Windows paths (`C:\` / `D:\`) that will cause failures if any tool reads it.

### 2.2 Files to Modify

| File | Current State | Required Change | Risk |
|---|---|---|---|
| `research_config.yaml` | Windows paths on lines 5, 9-21 | Replace with Linux paths | HIGH — breaking if read by tools |
| `Templates/Dataset_Template.md:46` | `D:\ResearchAI_Data\datasets\` | Replace with `/home/lco/ResearchAI_Data/datasets/` | LOW — template example only |
| `Templates/Experiment_Template.md:35` | `C:\ResearchAI\03_Projects\` | Replace with `/home/lco/ResearchAI/03_Projects/` | LOW — template example only |

### 2.3 Files to Preserve (No Changes)

| File | Reason |
|---|---|
| All `Stage_*.md` reports in `08_Agent_Config/` | Historical audit records |
| All `Stage_*.md` files in `08_Agent_Config/Migration/` | Historical migration records |
| `Skills/researchai/references/*` | Documentation examples (not executable) |
| `Skills/01_Literature/*.md` | Docstring references (not executable) |
| `MinerU_Zotero_Mapping.md` | Contains Windows paths in historical context |
| `Batch_Processing_Log.md` | Historical log entries |

**Rule**: Only modify files that are READ by tools/scripts. Historical reports and documentation examples are informational and should be preserved as-is.

### 2.4 Proposed `research_config.yaml` (Before/After)

**Before**:
```yaml
workspace:
  root: C:\ResearchAI
data:
  root: D:\ResearchAI_Data
  paper:
    origin_pdf: D:\ResearchAI_Data\Paper\Origin_pdf
    mineru_output: D:\ResearchAI_Data\Paper\MinerU_md
  datasets: D:\ResearchAI_Data\Datasets
  experiment_results: D:\ResearchAI_Data\Experiment_Results
  model_checkpoints: D:\ResearchAI_Data\Model_Checkpoints
```

**After**:
```yaml
workspace:
  root: /home/lco/ResearchAI
  description: Primary workspace — contains documentation, code, experiments, and agent configs

data:
  root: /home/lco/ResearchAI_Data
  description: External data layer — large files only

  paper:
    origin_pdf: /home/lco/ResearchAI_Data/Paper/Origin_pdf
    mineru_output: /home/lco/ResearchAI_Data/Paper/MinerU_md

  datasets: /home/lco/ResearchAI_Data/Datasets
  experiment_results: /home/lco/ResearchAI_Data/Experiment_Results
  model_checkpoints: /home/lco/ResearchAI_Data/Model_Checkpoints

# Note: All external data paths are under /home/lco/ResearchAI_Data/.
# The /home/lco/ResearchAI workspace does not store large files (PDFs, datasets, models).
```

### 2.5 Risk Control

| Risk | Mitigation |
|---|---|
| Breaking tools that read config | Verify no tool currently reads `research_config.yaml` — current tools use hardcoded paths |
| Accidentally modifying historical files | Only modify 3 files: config + 2 templates |
| Template changes breaking existing notes | Templates are references only; existing notes are not affected |

**Verification**: No Python script in `04_Tools/mineru/` imports or reads `research_config.yaml`. All scripts use hardcoded `Path()` constants. This makes the config file safe to update with zero regression risk.

---

## 3. Stage 6.3: KnowledgeVault Processing Pipeline

### 3.1 Problem Statement

Only 18/33 papers (55%) have any KnowledgeVault processing. Of the 27 papers with MinerU output, only 11 have literature cards and 7 have deep-read notes. The `process_paper.py` script exists but is not integrated into the batch pipeline.

### 3.2 Proposed Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Stage 6.3: KV Processing Pipeline             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Paper_Processing_State.yaml                                    │
│  ├── agent_state.literature_card = PENDING                       │
│  ├── agent_state.deep_read = PENDING                             │
│  └── mineru_state = MINERU_COMPLETE                              │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  AGENT: Paper Intake (SKILL_Paper_Intake.md)            │    │
│  │  - Reads registry for PENDING literature_card papers    │    │
│  │  - Verifies: Zotero PDF + MinerU full.md exist          │    │
│  │  - Checks: No duplicate KV files                        │    │
│  │  - Classifies: paper type, decision framework level     │    │
│  │  - Generates: Literature Card using template            │    │
│  │  - Updates: agent_state.literature_card = COMPLETE      │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  AGENT: Deep Read (SKILL_Paper_Deep_Read.md)            │    │
│  │  - Trigger: Human selects paper for deep analysis       │    │
│  │  - Reads: full.md + existing card                       │    │
│  │  - Generates: Paper Note with method/results analysis   │    │
│  │  - Updates: agent_state.deep_read = COMPLETE            │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  AGENT: Registry Sync (scan_registry.py)                │    │
│  │  - Re-scans KnowledgeVault/01_Papers/                   │    │
│  │  - Matches KV files to Zotero papers by title           │    │
│  │  - Updates agent_state in registry                      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 Literature Card Auto-Generation Flow

**Trigger**: Registry scan finds papers where `mineru_state = MINERU_COMPLETE` AND `agent_state.literature_card = PENDING`.

**Process**:
```
1. scan_registry.py generates registry
   ↓
2. Agent reads registry, filters:
   WHERE mineru_state = 'MINERU_COMPLETE'
     AND agent_state.literature_card = 'PENDING'
     AND pdf_exists = TRUE
   ↓
3. For each matched paper:
   a. Verify MinerU output exists (full.md + images/)
   b. Read full.md to extract title, authors, year, abstract
   c. Apply Paper_Processing_Decision_Framework:
      - Default: Level 1 (Card) for all papers
      - Flag for Level 2 if: high-importance, seismic-AI relevant
   d. Generate Literature Card using SKILL_Paper_Intake
   e. Update agent_state.literature_card = COMPLETE
   ↓
4. scan_registry.py re-scans to confirm
```

**Files Created**: `02_KnowledgeVault/01_Papers/{author}{year}_{keyword}_card.md`
**Files Modified**: `Paper_Processing_State.yaml` (agent_state), `MinerU_Zotero_Mapping.md` (status column)

### 3.4 Deep Read Trigger Conditions

Based on the Paper Processing Decision Framework, a paper qualifies for deep read when:

| Criterion | Condition | Example |
|---|---|---|
| **Direct relevance** | Paper addresses seismic phase picking, fault segmentation, or landslides | DTPP (Lv 2026) |
| **Method novelty** | Introduces a novel architecture not yet in KV | ViT for InSAR |
| **Benchmark value** | Provides benchmark results usable for comparison | PhaseNet, EqTransformer |
| **Human selection** | Explicitly flagged by human reviewer | Any paper |

**Implementation**: The deep_read trigger is NOT automatic. It requires:
1. Literature Card already exists (`agent_state.literature_card = COMPLETE`)
2. Human marks paper as "Deep Read" (via decision framework or explicit command)
3. Agent generates note using `SKILL_Paper_Deep_Read.md`

### 3.5 Registry State Update Mechanism

**Current state machine** for `agent_state`:

```
literature_card:
  PENDING → (Intake skill creates card) → COMPLETE
  
deep_read:
  PENDING → (Human selects for deep analysis) → COMPLETE
  
method_extraction:
  PENDING → (No files created yet) → PENDING
  
obsidian_note:
  PENDING → (No files created yet) → PENDING
```

**Update mechanism**:
1. `scan_registry.py` runs AFTER each batch of paper processing
2. It scans `02_KnowledgeVault/01_Papers/` for new/updated files
3. Matches files to Zotero papers by title
4. Updates `agent_state` in the YAML registry
5. Agent reads updated registry to determine next action

**Automation opportunity**: A post-processing hook could trigger `scan_registry.py` automatically after any KnowledgeVault file is created. This would eliminate the manual re-scan step.

### 3.6 Agent Call Chain

```
User/Agent Request: "Process paper JCKZQTYW"
    │
    ▼
scan_registry.py (read registry)
    │
    ▼
Check: agent_state.literature_card for JCKZQTYW
    │
    ├─ If PENDING → Run SKILL_Paper_Intake → Create Card → Set COMPLETE
    │
    ├─ If COMPLETE AND deep_read = PENDING AND human_selected → Run SKILL_Paper_Deep_Read → Create Note → Set COMPLETE
    │
    └─ If all COMPLETE → Paper fully processed
    │
    ▼
scan_registry.py (update registry)
    │
    ▼
Next paper in queue
```

---

## 4. Skills Sufficiency Evaluation

### 4.1 Coverage Matrix

| Pipeline Stage | Required Capability | Available Skill | Gap |
|---|---|---|---|
| Paper intake | Verify Zotero + MinerU + generate card | SKILL_Paper_Intake.md | None |
| Batch processing | Process multiple papers | SKILL_Paper_Batch_Process.md | None |
| Deep read | Generate paper note | SKILL_Paper_Deep_Read.md | None |
| Paper update | Update existing records | SKILL_Paper_Update.md | None |
| Duplicate check | Prevent node duplication | SKILL_Knowledge_Node_Check.md | None |
| Registry scan | Scan and update state | SKILL_Registry_Scan.md | None |
| Research map | Update navigation | SKILL_Research_Map_Update.md | None |
| Literature synthesis | Generate writing material | SKILL_Literature_Synthesis.md | None |
| Architecture audit | System integrity checks | SKILL_Architecture_Audit.md | None |
| **Method extraction** | Generate method node | **MISSING** | Low priority |
| **Logic generation** | Generate argument mining | **MISSING** | Low priority |

### 4.2 Assessment

**Existing skills are sufficient for the immediate next stage (6.3).**

The 9 existing skills cover:
- All Level 1 operations (intake, batch, update)
- All Level 2 operations (deep read)
- System operations (registry scan, node check, map update, audit)
- Level 3 operations (literature synthesis)

**Missing skills** (method_extraction, obsidian_note/logic) are not needed immediately because:
1. No KnowledgeVault method or logic files exist yet
2. These are Level 3 operations requiring significant human judgment
3. The decision framework explicitly gates Level 2→3 progression

**Recommendation**: Do NOT create new skills for method_extraction or logic generation. If needed in the future, they can be derived from SKILL_Paper_Deep_Read.md with additional output sections.

---

## 5. Data Flow Diagram

### 5.1 Before Stage 6.2/6.3

```
research_config.yaml (Windows paths)
    ↓ [NOT USED by any tool — hardcoded paths everywhere]

KnowledgeVault processing:
  MinerU output → MANUAL agent invocation → KV files → MANUAL registry rescan
    ↑                                    ↓
    └──── process_paper.py exists but is not connected ────┘
```

### 5.2 After Stage 6.2/6.3

```
research_config.yaml (Linux paths)
    ↓ [Available for future tools that want to use it]

KnowledgeVault processing:
  registry (agent_state=PENDING)
    ↓ [scan_registry.py]
  Filter papers by agent_state
    ↓ [SKILL_Paper_Intake]
  Generate Literature Cards (automated batch)
    ↓
  agent_state.literature_card = COMPLETE
    ↓ [scan_registry.py re-scan]
  Registry updated
    ↓ [Human selection]
  SKILL_Paper_Deep_Read → Generate Notes
    ↓
  agent_state.deep_read = COMPLETE
    ↓
  Full paper processing pipeline operational
```

---

## 6. State Machine Design

### 6.1 Paper Processing States

Each paper moves through a state machine defined by `agent_state`:

```
                    ┌─────────────────────────────────────────┐
                    │           Paper Lifecycle                │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  mineru_state: MINERU_PENDING            │
                    │  (No PDF in Zotero)                      │
                    │  → Block: Cannot process                 │
                    └─────────────────────────────────────────┘
                                      │
                                      │ PDF acquired
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  mineru_state: MINERU_COMPLETE           │
                    │  agent_state.literature_card: PENDING    │
                    │  → Action: Run SKILL_Paper_Intake        │
                    └─────────────────────────────────────────┘
                                      │
                                      │ Card created
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  agent_state.literature_card: COMPLETE   │
                    │  agent_state.deep_read: PENDING          │
                    │  → Decision: Human selects for deep read │
                    └─────────────────────────────────────────┘
                                      │
                                      │ Deep read selected
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  agent_state.deep_read: COMPLETE         │
                    │  agent_state.method_extraction: PENDING  │
                    │  → Optional: Future method documentation │
                    └─────────────────────────────────────────┘
                                      │
                                      │ Method extracted
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  agent_state.obsidian_note: COMPLETE     │
                    │  → Paper fully processed                 │
                    └─────────────────────────────────────────┘
```

### 6.2 State Transitions

| Transition | Trigger | Actor | File Updated |
|---|---|---|---|
| MINERU_PENDING → MINERU_COMPLETE | batch_process.py completes | Automated | registry.mineru_state |
| literature_card PENDING → COMPLETE | SKILL_Paper_Intake creates card | Agent | registry.agent_state |
| deep_read PENDING → COMPLETE | SKILL_Paper_Deep_Read creates note | Agent | registry.agent_state |
| method_extraction COMPLETE | Method node created | Agent | registry.agent_state |
| obsidian_note COMPLETE | Logic node created | Agent | registry.agent_state |

### 6.3 Registry Update Frequency

| Scenario | Update Method |
|---|---|
| After batch MinerU processing | `scan_registry.py` (manual or hook) |
| After each card/note creation | `scan_registry.py` (recommended as post-processing step) |
| Before starting new processing | `scan_registry.py --report` (always read fresh state) |

---

## 7. File Modification Summary

### 7.1 Stage 6.2: Files to Modify

| File | Action | Lines Changed |
|---|---|---|
| `research_config.yaml` | Replace Windows paths with Linux paths | ~10 lines |
| `Templates/Dataset_Template.md:46` | Replace `D:\` with Linux path | 1 line |
| `Templates/Experiment_Template.md:35` | Replace `C:\` with Linux path | 1 line |

**Total files modified**: 3
**Total lines changed**: ~12

### 7.2 Stage 6.2: Files to Preserve

| Category | Count | Examples |
|---|---|---|
| Stage reports | ~50 | `Stage_1.5_*.md`, `Stage_2A_*.md`, etc. |
| Migration reports | ~8 | `Stage_4B_*.md`, `Stage_5_*.md`, etc. |
| Design documents | ~10 | `ADR_*.md`, `Zotero_Integration_Design.md` |
| Skill references | ~15 | `Skills/researchai/references/*` |

**Rule**: All historical documents are preserved as-is. They serve as audit trails and decision records.

### 7.3 Stage 6.3: Files to Create

| File | Source | Count |
|---|---|---|
| `*_card.md` | SKILL_Paper_Intake + full.md | ~16 new cards |
| `*_note.md` | SKILL_Paper_Deep_Read + full.md | Variable (human-selected) |

**Files modified by Stage 6.3**:
- `Paper_Processing_State.yaml` — agent_state updates
- `MinerU_Zotero_Mapping.md` — status column updates
- `Paper_Index.md` — new entries
- `Batch_Processing_Log.md` — processing records

---

## 8. Risk Analysis

### 8.1 Stage 6.2 Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Config change breaks nothing (no tool reads it) | Certain | None | Already verified: no tool reads config |
| Template change affects existing notes | Impossible | None | Templates are references only |
| Accidentally modifying historical files | Low | Low | Clear file modification list |

**Overall Stage 6.2 Risk**: NEGLIGIBLE

### 8.2 Stage 6.3 Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Duplicate card creation | Medium | High | SKILL_Paper_Intake has duplicate check |
| Wrong paper type classification | Low | Medium | Decision framework provides criteria |
| Over-processing (creating notes without human selection) | Low | Low | Deep read requires human trigger |
| Registry state desync | Medium | Medium | scan_registry.py runs after each batch |
| Template inconsistency (old templates with Windows paths) | Certain | Low | Stage 6.2 fixes this first |

**Overall Stage 6.3 Risk**: LOW (mitigated by existing skills and decision framework)

---

## 9. Rollback Plan

### 9.1 Stage 6.2 Rollback

If `research_config.yaml` causes issues:
```bash
# The config is not read by any tool, so rollback is trivial
# Simply restore the original content or delete the file
# No tool depends on it
```

If templates cause issues:
```bash
# Restore from backup files
cp Templates/Dataset_Template.md.backup_linux_migration Templates/Dataset_Template.md
cp Templates/Experiment_Template.md.backup_linux_migration Templates/Experiment_Template.md
```

### 9.2 Stage 6.3 Rollback

If paper processing creates unwanted files:
```bash
# Remove created KV files
rm 02_KnowledgeVault/01_Papers/<unwanted_file>.md

# Reset registry state
# Edit Paper_Processing_State.yaml to set agent_state fields back to PENDING
# Or regenerate from scratch:
python 04_Tools/mineru/scan_registry.py
```

---

## 10. Implementation Order

### Phase 1: Stage 6.2 (Config Fix) — Priority: HIGH

1. Update `research_config.yaml` with Linux paths
2. Update `Dataset_Template.md` path example
3. Update `Experiment_Template.md` path example
4. Verify no tool reads the config (confirm existing verification)

**Estimated effort**: 15 minutes
**Risk**: Negligible

### Phase 2: Stage 6.3 (KV Processing) — Priority: MEDIUM

1. Run `scan_registry.py` to get current state
2. Filter papers: `mineru_state = MINERU_COMPLETE AND literature_card = PENDING`
3. Process remaining ~16 papers through SKILL_Paper_Intake (batch mode)
4. Run `scan_registry.py` to update agent_state
5. Select high-value papers for deep read (SKILL_Paper_Deep_Read)
6. Repeat registry scan

**Estimated effort**: 2-4 hours (depending on paper count and human review time)
**Risk**: Low (existing skills handle all edge cases)

### Phase 3: Automation (Optional) — Priority: LOW

1. Create a post-processing hook: after any KV file creation, auto-run `scan_registry.py`
2. Integrate `process_paper.py` into batch pipeline
3. Add `agent_state.IN_PROGRESS` transitional state for active processing

---

## 11. Success Criteria

### Stage 6.2 Success

- [ ] `research_config.yaml` uses only Linux paths
- [ ] Template path examples use Linux paths
- [ ] No tool functionality affected
- [ ] All historical documents preserved

### Stage 6.3 Success

- [ ] All 27 MinerU-complete papers have literature cards
- [ ] Registry agent_state accurately reflects KV file existence
- [ ] At least 5 papers have deep-read notes (human-selected)
- [ ] No duplicate files created
- [ ] Paper_Index.md updated with all new entries

---

*This document is a design proposal only. No files have been modified.*
