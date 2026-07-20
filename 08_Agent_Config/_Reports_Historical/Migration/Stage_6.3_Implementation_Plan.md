# Stage 6.3 - KnowledgeVault Processing Pipeline Implementation Plan

**Date**: 2026-07-18
**Type**: Implementation Plan (READ-ONLY audit then plan)
**Preceded by**: Stage 6.2 (Config Path Remediation - COMPLETE)

---

## 1. Current State Audit

### 1.1 Zotero Inventory

| Metric | Count |
|---|---|
| Total Zotero papers | 33 |
| Papers with PDFs available | 27 |
| Papers without PDFs (MINERU_PENDING) | 6 |

**Pending papers (no PDF)**: FL6TSZPA (QuakeFlow), H9LQNVTM (Generalized Seismic Phase Detection), II3UGDYS (SeisBench), PW86NPCG (OBSTransformer), YW7ADGN9 (CRED), YXFR9DZT (PickBlue)

### 1.2 MinerU Processing Coverage

| Metric | Count |
|---|---|
| MinerU complete (full.md exists) | 27 |
| MinerU partial | 0 |
| MinerU pending | 6 |

MinerU output directory: /home/lco/ResearchAI_Data/Paper/MinerU_md/ contains 109 directories (includes non-paper folders, legacy outputs, and 27 valid paper outputs).

### 1.3 KnowledgeVault Processing Coverage

| Stage | Count | Percentage |
|---|---|---|
| Literature Card (COMPLETE) | 27 | 100% of MinerU-complete |
| Deep Read Note (COMPLETE) | 7 | 26% of MinerU-complete |
| Deep Read Note (PENDING) | 20 | 74% of MinerU-complete |
| Method Extraction (COMPLETE) | 0 | 0% |
| Paper Logic (COMPLETE) | 2 | ~29% of deep-read papers |

**Detailed breakdown by agent_state (from Paper_Processing_State.yaml)**:

- Literature Cards: 27 COMPLETE, 6 PENDING (the 6 without PDFs)
- Deep Read: 7 COMPLETE (5L2QLL47, 6HWKP8EC, CY43XIQN, FAA4JYRC, FGFVQ8EP, N7UP2CZT, TSQGFMA2), 20 PENDING among MinerU-complete papers
- Method Extraction: 33 PENDING (no extraction has been attempted)
- Obsidian Note: 33 PENDING (not yet started)

### 1.4 Mapping Registry Status

MinerU_Zotero_Mapping.md contains:
- 6 PROCESSED entries (early batch)
- 12 C1/C2 entries (batch 11 papers from Stage 1.5-7C)
- 1 LEVEL_1_DONE entry (DTPP)
- 7 PENDING_MINERU entries (outdated - these papers ARE MinerU-complete)
- Unprocessed Papers section with 7 entries (some overlap with existing papers)

**Issue**: The PENDING_MINERU section lists papers that already have MinerU output and are in the registry. These are stale entries from an earlier state.

### 1.5 Skills Inventory

| Skill | Status | Location |
|---|---|---|
| SKILL_Registry_Scan.md | EXISTS | 08_Agent_Config/Skills/ |
| researchai (full skill) | EXISTS | 08_Agent_Config/Skills/researchai/ |
| Paper Intake reference | EXISTS | Skills/researchai/references/literature/paper_intake.md |
| Deep Read reference | EXISTS | Skills/researchai/references/literature/paper_deep_read.md |
| Batch Process reference | EXISTS | Skills/researchai/references/literature/paper_batch_process.md |
| Paper Logic reference | EXISTS | Skills/researchai/references/literature/paper_logic.md |
| Survey Process reference | EXISTS | Skills/researchai/references/literature/survey_process.md |
| Architecture Audit reference | EXISTS | Skills/researchai/references/system/architecture_audit.md |
| Knowledge Node Check reference | EXISTS | Skills/researchai/references/knowledge/node_check.md |
| Research Map Update reference | EXISTS | Skills/researchai/references/knowledge/research_map_update.md |
| Literature Synthesis reference | EXISTS | Skills/researchai/references/writing/literature_synthesis.md |
| Method Node reference | EXISTS | Skills/researchai/references/knowledge/method_node.md |
| Encoding Audit reference | EXISTS | Skills/researchai/references/system/encoding_audit.md |
| Paper Update reference | EXISTS | Skills/researchai/references/literature/paper_update.md |

**Assessment**: All required skills and references exist. No new skills need to be created.

### 1.6 Templates Inventory

All 10 templates exist in 02_KnowledgeVault/Templates/:
- Literature_Card_Template.md, Paper_Template.md, Survey_Template.md, Paper_Logic_Template.md
- Method_Template.md, Task_Template.md, Dataset_Template.md, Experiment_Template.md
- Idea_Template.md, Writing_Template.md

**Assessment**: All templates exist and are current. Stage 6.2 already fixed Windows path issues in Dataset_Template.md and Experiment_Template.md.

### 1.7 Decision Framework & Guidelines

All governance documents are in place:
- Paper_Processing_Decision_Framework.md - 3-level strategy fully defined
- Paper_Card_Guideline.md - Card vs Note roles clarified
- Paper_Logic_Guideline.md - Argument Mining standard defined
- Batch_Processing_Guideline.md - Batch workflow with duplicate prevention
- Paper_File_Naming_Rules.md - Naming conventions defined

**Assessment**: All governance documents are in place and consistent.

---

## 2. Gap Analysis

### 2.1 Identified Gaps

| Gap | Severity | Description |
|---|---|---|
| Stale PENDING_MINERU entries in mapping | LOW | 7 entries in MinerU_Zotero_Mapping.md claim PENDING_MINERU status but papers are actually MINERU_COMPLETE |
| 20 deep-read papers unprocessed | MEDIUM | 20 papers have Literature Cards but no Deep Read Notes. This is expected - deep read requires human selection per the Decision Framework |
| MinerU output has non-paper directories | LOW | Legacy folders exist but are not in Zotero. Should be ignored unless researcher wants to process them |
| Paper_Index.md encoding issues | LOW | Contains garbled Chinese characters due to UTF-8 BOM. Does not affect functionality |

### 2.2 What Is NOT a Gap

- **No orchestration layer needed**: The Skills system IS the orchestration (per Stage 6.3 Architecture Review)
- **No priority index needed yet**: With 33 papers, manual priority ordering is sufficient. Priority index is a Stage 6.4 concern
- **No archive mechanism needed yet**: At 33 papers, active queue management is trivial. Archive is a Stage 6.5 concern
- **No new skills needed**: The 9-skill system covers all operations (per architecture review)
- **No directory restructuring needed**: The frozen architecture is correct

### 2.3 Core Assessment: Pipeline Operational Status

The pipeline is **partially operational**:
- Level 1 (Literature Cards): OPERATIONAL - all 27 MinerU-complete papers have cards
- Level 2 (Deep Read Notes): PARTIALLY OPERATIONAL - 7/27 papers have notes, 20 remain pending
- Level 3 (Paper Logic): PARTIALLY OPERATIONAL - 2/7 deep-read papers have logic notes

Per the Decision Framework, Level 2 (Deep Read) requires human selection. The pipeline is considered operational once:
1. All 27 papers have Literature Cards (DONE)
2. The skill references and templates can produce notes correctly (VERIFIED)
3. The registry state accurately reflects processing (PARTIALLY - needs cleanup)
4. The mapping registry is consistent (NEEDS UPDATE)

---

## 3. Minimal Implementation Plan

### 3.1 Scope Definition

Stage 6.3 focuses on making the existing paper processing pipeline **operationally verified** - not on processing all remaining papers.

**IN SCOPE**:
1. Verify the registry accurately reflects KnowledgeVault file state
2. Clean up stale entries in MinerU_Zotero_Mapping.md
3. Verify all skill references are consistent with current file paths
4. Document the operational pipeline status
5. Identify which papers are candidates for next-level processing

**OUT OF SCOPE** (explicitly NOT in Stage 6.3):
- Paper_Priority_Index.yaml (future Stage 6.4)
- scan_priority.py (future Stage 6.4)
- Archive mechanism (future Stage 6.5)
- New orchestration layer (violates frozen architecture)
- New skills (unnecessary per architecture review)
- Processing all 20 remaining deep-read papers (requires human selection)
- Modifying any Stage reports or historical documents

### 3.2 Execution Steps

#### Step 1: Registry Verification

Regenerate Paper_Processing_State.yaml via scan_registry.py and verify it matches the actual KnowledgeVault state.

**Verification target**: For each of the 27 MinerU-complete papers:
- agent_state.literature_card = COMPLETE (already confirmed)
- agent_state.deep_read matches actual _note.md files in 01_Papers/
- No phantom entries (papers in registry but no MinerU output)

#### Step 2: Mapping Registry Cleanup

Update MinerU_Zotero_Mapping.md:
- Correct the 7 PENDING_MINERU entries (papers are actually PROCESSED or have cards)
- Ensure all 27 MinerU-complete papers have consistent status entries
- Do NOT modify existing PROCESSED or C1/C2 entries (they are historical records)

#### Step 3: Skill Path Verification

Verify all skill references use correct paths. Note: Skill reference files contain Windows path examples for documentation. Per Stage 6.2 precedent, only MODIFY files that are READ by tools/scripts. Documentation examples in skill references are informational and should be preserved as-is.

#### Step 4: Pipeline Status Report

Document:
- Current processing coverage by level
- Papers ready for deep-read selection
- Papers ready for paper-logic creation
- Any blocking issues

#### Step 5: Next-Action Recommendation

Provide clear recommendation for what Stage 6.3+ should do next.

---

## 4. Files That Will Be Modified

| File | Action | Reason |
|---|---|---|
| Migration/Stage_6.3_Implementation_Plan.md | CREATE | This document |
| MinerU_Zotero_Mapping.md | UPDATE (if confirmed needed) | Clean up stale PENDING_MINERU entries |
| Paper_Processing_State.yaml | READ-VERIFY | Confirm registry accuracy |

**Total files modified**: 0-2 (depends on verification results)

---

## 5. Files That Must Remain Untouched

| Category | Examples |
|---|---|
| Stage reports | All Stage_*.md in 08_Agent_Config/ |
| Migration reports | All files in 08_Agent_Config/Migration/ except new plan |
| Historical logs | Batch_Processing_Log.md, Stress_Test_Execution_Log.md |
| Templates | All files in 02_KnowledgeVault/Templates/ |
| Existing KV files | All files in 02_KnowledgeVault/01_Papers/ |
| Skill references | All files in Skills/researchai/references/ |
| Python scripts | 04_Tools/mineru/scan_registry.py, batch_process.py |
| Design documents | Paper_Processing_Decision_Framework.md, Batch_Processing_Guideline.md |

---

## 6. Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Registry state mismatch | Medium | Medium | scan_registry.py provides ground truth; cross-check manually |
| Mapping cleanup removes valid history | Low | Medium | Only update status columns; never delete rows (per maintenance rules) |
| Incorrect deep-read classification | Low | Low | Deep-read requires human selection; agent cannot auto-promote |
| Encoding issues in new files | Low | Medium | All files written as UTF-8 without BOM (per encoding policy) |
| Duplicate file creation | Low | High | Duplicate prevention gate enforced by all skills |

**Overall Risk**: LOW

---

## 7. Execution Order

1. Read-only verification (current step): Audit all state files
2. Registry cross-check: Compare Paper_Processing_State.yaml against actual 01_Papers/ files
3. Mapping cleanup (if needed): Update stale entries in MinerU_Zotero_Mapping.md
4. Generate status report: Document pipeline health
5. Recommend next actions: Provide clear path forward

---

## 8. Rollback Strategy

All Stage 6.3 changes are reversible:

| Change | Rollback |
|---|---|
| Mapping status updates | Revert to previous entries (git history available) |
| New plan document | Delete Stage_6.3_Implementation_Plan.md |
| No file modifications | If verification shows everything is correct, no rollback needed |

**No data loss risk**: All modifications are status updates or additions. No existing content is deleted.

---

## 9. Success Criteria

Stage 6.3 is complete when:

- [ ] Paper_Processing_State.yaml accurately reflects KnowledgeVault file existence
- [ ] MinerU_Zotero_Mapping.md has no stale PENDING_MINERU entries for completed papers
- [ ] Pipeline status is documented with clear coverage numbers
- [ ] Next-action recommendations are provided
- [ ] No files outside the defined scope were modified

---

*This is a planning document. Implementation begins after Stage 6.2 verification confirms the foundation is solid.*
