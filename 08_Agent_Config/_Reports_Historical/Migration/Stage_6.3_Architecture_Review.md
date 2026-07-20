# Stage 6.3 Architecture Review

**Date**: 2026-07-18
**Type**: Design Review (READ-ONLY, no modifications)
**Preceded by**: Stage 6.1 (agent_state), Stage 6.1.1 (Audit), Stage 6.1.2 (Proposal)

---

## Executive Summary

This review evaluates whether the current ResearchAI architecture is sufficient for a long-term AI research assistant system capable of scaling from 33 papers to thousands. Five critical design questions are analyzed against the existing architecture, decision frameworks, and skills system.

**Key Finding**: The current architecture is fundamentally sound for its intended purpose (seismic AI research), but has three scaling concerns:

1. `agent_state` tracks file existence only — missing paper priority/relevance metadata needed for intelligent scheduling
2. Literature Card generation for ALL papers is correct per the decision framework, but batch processing lacks automation
3. `process_paper.py` should remain manual — adding an orchestration layer would violate the frozen architecture
4. The 9-skill system is sufficient for 33 papers but would need a **routing layer** for 1000+ papers
5. The Decision Framework's 3-level strategy is the correct scaling mechanism — it should be enhanced, not replaced

---

## Question 1: Should agent_state only represent file existence, or include priority/value/relevance?

### Current State

The `agent_state` field tracks only file existence:

| Field | Values | Purpose |
|---|---|---|
| `literature_card` | PENDING / COMPLETE | Does `_card.md` exist? |
| `deep_read` | PENDING / COMPLETE | Does `_note.md` exist? |
| `method_extraction` | PENDING / COMPLETE | Does `_method.md` exist? |
| `obsidian_note` | PENDING / COMPLETE | Does `_logic.md` exist? |

The Decision Framework tracks relevance/novelty/value in the **Literature Card itself**, not in the registry.

### Analysis

**Problem**: When scaling to hundreds of papers, an agent needs to know WHICH papers to process next. Currently, `scan_registry.py` can only answer "have cards been created?" — it cannot answer "which unprocessed papers are most important?"

**Example scenario with 500 papers**:
- 200 have MinerU output but no card
- Which 20 should the agent process first?
- Currently: no way to prioritize — agent must scan all 200 titles manually
- With priority metadata: agent sorts by relevance score and processes top 20

**However**: Adding priority fields to `agent_state` creates a design conflict:

| Concern | Argument For | Argument Against |
|---|---|---|
| Simplicity | Current schema is clean and minimal | Adding fields increases complexity |
| Source of truth | Decision Framework already captures relevance | Should registry reflect that? |
| Stability | File existence is permanent | Relevance scores change as research direction evolves |
| Scalability | Priority enables intelligent batching | Priority metadata requires periodic re-evaluation |

### Recommendation: TWO-LAYER APPROACH

**Do NOT modify `agent_state`**. Instead, add a **separate paper priority index** that sits alongside the registry.

```
Paper_Processing_State.yaml (immutable file-existence tracking)
    |
    +-- agent_state.literature_card = COMPLETE/ PENDING
    +-- agent_state.deep_read = PENDING
    |
Paper_Priority_Index.yaml (dynamic relevance tracking)
    +-- paper_key: JCKZQTYW
    +-- relevance: direct / tangential / unrelated
    +-- novelty: significant / moderate / incremental
    +-- potential_value: high / medium / low
    +-- processing_priority: 1 (highest) to 5 (lowest)
    +-- last_scored: 2026-07-18
    +-- scored_by: agent / human
```

**Why this works**:
1. `agent_state` remains a stable, immutable record of file existence
2. Priority index is dynamic and can be re-scored as research direction evolves
3. The Decision Framework's scoring rubric (Section C) maps directly to priority fields
4. Batch processing can query priority index to determine processing order
5. No changes to existing skills or registry schema

**Implementation**: The priority index can be auto-populated by `SKILL_Paper_Intake.md` during Level 1 screening (the card already records relevance/novelty/value). A future `scan_priority.py` script could extract these fields from Literature Cards and build the index automatically.

### Verdict

**agent_state should remain file-existence only.** Add a separate priority index for scheduling intelligence.

---

## Question 2: Should Literature Card generation be performed for all papers, or should a decision framework classify papers before deep processing?

### Current State

The Decision Framework (Section A) is explicit:

> **Level 1 — Literature Card (Screening)**
> Applied to: Every paper entering the system. Non-optional.

The Batch Processing Guideline reinforces:

> **Batch Processing Rule**: In batch mode, ALL papers go through Level 1.

### Analysis

**This is correct.** The Decision Framework's design is specifically intended to prevent unnecessary deep processing. The three-tier structure is:

| Level | Scope | Token Cost | Purpose |
|---|---|---|---|
| Level 1 (Card) | 100% of papers | ~300 tokens/paper | Rapid classification |
| Level 2 (Note) | ~20-30% of papers | ~1,500 tokens/paper | Deep analysis of selected papers |
| Level 3 (Logic) | ~5-10% of papers | ~4,000 tokens/paper | Argument mining for core papers |

**Scaling projection** (1,000 papers):

| Level | Expected Count | Token Cost |
|---|---|---|
| Level 1 | 1,000 papers | ~300,000 tokens |
| Level 2 | ~250 papers | ~375,000 tokens |
| Level 3 | ~50 papers | ~200,000 tokens |
| **Total** | | ~875,000 tokens |

Without Level 1 filtering, naive deep analysis of 1,000 papers would cost ~4,000,000+ tokens. The framework saves ~78%.

**However**, there is a practical concern: generating 1,000 Literature Cards is still expensive (~300,000 tokens). For very large corpora, consider:

1. **Threshold filtering**: Skip Level 1 for papers clearly irrelevant (e.g., wrong domain, non-peer-reviewed)
2. **Batch optimization**: Process cards in groups of 10-20 rather than one-at-a-time
3. **Incremental scoring**: Use the priority index to process high-value papers first

### Verdict

**Keep the current approach.** Level 1 screening for all papers is the correct design. Enhance with batch optimization and priority-based ordering, but do not skip Level 1.

---

## Question 3: Should process_paper.py remain a standalone manual tool, or should ResearchAI introduce an agent orchestration layer?

### Current State

`process_paper.py` exists at `04_Tools/mineru/process_paper.py` and:
- Processes a single Zotero paper through MinerU + normalization
- Requires manual invocation: `python process_paper.py <Zotero_Item_Key>`
- Is NOT integrated into the batch pipeline
- The batch pipeline uses `batch_process.py` which calls MinerU directly

The Skills system (`SKILL_Paper_Intake.md`, `SKILL_Paper_Deep_Read.md`) handles KnowledgeVault note generation, not MinerU processing.

### Analysis

**Arguments for introducing an orchestration layer**:

| Benefit | Impact |
|---|---|
| Automated pipeline | Reduces manual agent intervention |
| Error recovery | Retries failed papers automatically |
| Progress tracking | Real-time status updates |
| Parallel processing | Process multiple papers simultaneously |

**Arguments against**:

| Risk | Impact |
|---|---|
| Violates frozen architecture | The three-layer structure (Zotero → MinerU → KnowledgeVault) is explicit and permanent |
| Adds complexity | A new orchestration layer introduces failure modes |
| Reduces transparency | Manual invocation makes debugging easier |
| Skill system already handles workflow | SKILL_Paper_Intake.md provides structured, auditable workflow |

**Critical insight**: The architecture already has a form of orchestration — **the Skills system**. Each skill defines a structured, step-by-step workflow with:
- Prerequisites checking
- Human confirmation gates
- Error handling
- Post-processing cleanup

Adding a separate orchestration layer would duplicate this functionality and create confusion about who controls the pipeline.

**Alternative approach**: Instead of a new orchestration layer, enhance the existing system:

1. **Batch skill**: Create a `SKILL_Paper_Batch_Intake.md` that wraps multiple `SKILL_Paper_Intake.md` invocations with progress tracking
2. **Registry hook**: Make `scan_registry.py` auto-trigger after any KnowledgeVault file creation
3. **Priority queue**: Use the priority index (Question 1 recommendation) to determine processing order

### Verdict

**Do NOT introduce an orchestration layer.** The Skills system IS the orchestration. Enhance batch capabilities within the existing skill framework. Keep `process_paper.py` as a standalone tool for manual/single-paper processing.

---

## Question 4: Evaluate whether the current Skills architecture is sufficient for scaling from 33 papers to thousands of papers.

### Current Skills Inventory

| Skill | Directory | Purpose | Scaling Concern |
|---|---|---|---|
| `SKILL_Paper_Intake.md` | 01_Literature | Level 1 screening | Fine for 100s, needs batching for 1000s |
| `SKILL_Paper_Deep_Read.md` | 01_Literature | Level 2 analysis | Token-intensive, needs priority filtering |
| `SKILL_Paper_Batch_Process.md` | 01_Literature | Batch card generation | Designed for batches, good for scaling |
| `SKILL_Paper_Update.md` | 01_Literature | Update existing records | Scales well (one-at-a-time) |
| `SKILL_Knowledge_Node_Check.md` | 02_Knowledge | Prevent duplicates | Essential at scale |
| `SKILL_Research_Map_Update.md` | 02_Knowledge | Update navigation | Needs automation for large growth |
| `SKILL_Literature_Synthesis.md` | 03_Writing | Generate writing material | Scales well (topic-based) |
| `SKILL_Architecture_Audit.md` | 04_System | System integrity | Essential at scale |
| `SKILL_Registry_Scan.md` | Skills | Registry regeneration | Essential at scale |

### Scaling Analysis

**At 33 papers**: Each skill is invoked manually by an agent. The overhead is low because there are few papers to process.

**At 300 papers**: Manual invocation becomes impractical. The batch processing skill (`SKILL_Paper_Batch_Process.md`) is essential here.

**At 1,000+ papers**: Three scaling challenges emerge:

1. **Token cost**: Level 1 screening of 1,000 papers = ~300,000 tokens. This is manageable but requires budget planning.
2. **Duplicate detection**: `SKILL_Knowledge_Node_Check.md` becomes critical — without it, the Methods/Tasks/Datasets directories would become cluttered with redundant nodes.
3. **Priority routing**: Without a priority index, the agent wastes time processing low-value papers first.

### Missing Capabilities at Scale

| Gap | Current State | Needed for Scale |
|---|---|---|
| Paper triage | Manual (agent decides order) | Priority-index-based ordering |
| Batch progress tracking | Log file only | Real-time dashboard or registry view |
| Cross-paper analysis | Manual (Literature Synthesis skill) | Automated topic clustering |
| Knowledge node deduplication | SKILL_Knowledge_Node_Check.md | Needs to be mandatory pre-step |
| Archive old/completed papers | Not implemented | Auto-archive papers with 100% agent_state |

### Recommendation

**The current 9-skill system is sufficient IF enhanced with:**

1. **Priority index** (from Question 1) — determines processing order
2. **Mandatory node-check pre-step** — `SKILL_Knowledge_Node_Check.md` must run before any Method/Task/Dataset creation
3. **Batch aggregation** — `SKILL_Paper_Batch_Process.md` should be the primary invocation method, not individual intake
4. **Archive mechanism** — Papers with all `agent_state` fields COMPLETE should be moved to an archive directory to reduce scan time

**No new skills are needed.** The existing skills cover all required operations. The scaling challenge is organizational, not functional.

### Verdict

**Skills architecture is sufficient for scaling.** Enhancement needed: priority index + mandatory node-check + batch-first workflow.

---

## Question 5: Propose Stage 6.3 Revised Architecture

### 5.1 Current Architecture (As-Is)

```
Zotero DB (33 papers)
    |
    | scan_registry.py
    v
Paper_Processing_State.yaml (agent_state tracking)
    |
    | batch_process.py + MinerU CLI
    v
MinerU_md/ (27 valid outputs)
    |
    | SKILL_Paper_Intake.md (manual invocation)
    v
KnowledgeVault/01_Papers/ (18/33 papers with cards)
    |
    | scan_registry.py (manual re-scan)
    v
agent_state updated in registry
```

**Problems**:
- No priority-based processing order
- Manual invocation of skills (no batching)
- No knowledge node deduplication enforcement
- Registry re-scan is manual

### 5.2 Proposed Architecture (Stage 6.3)

```
Zotero DB (N papers)
    |
    | scan_registry.py
    v
Paper_Processing_State.yaml (agent_state + paper_key)
    |
    | Paper_Priority_Index.yaml (NEW — relevance/novelty/value)
    v
    | Sort by processing_priority ASC
    |
    | SKILL_Paper_Batch_Process.md (PRIMARY invocation)
    |   |-- For each paper in priority order:
    |   |   |-- SKILL_Knowledge_Node_Check.md (MANDATORY pre-step)
    |   |   |-- SKILL_Paper_Intake.md (Level 1 screening)
    |   |   |   |-- Writes: Literature Card
    |   |   |   |-- Records: relevance, novelty, value
    |   |   |-- scan_registry.py (auto-update agent_state)
    |   |
    |   |-- Papers marked "Deep Read":
    |   |   |-- SKILL_Paper_Deep_Read.md (Level 2)
    |   |   |   |-- Writes: Paper Note
    |   |   |   |-- Creates: Method/Task/Dataset nodes (if needed)
    |   |   |-- scan_registry.py (auto-update agent_state)
    |   |
    |   |-- Papers meeting Level 3 triggers:
    |       |-- SKILL_Paper_Deep_Read.md (Level 3)
    |           |-- Writes: Paper Logic
    |
    v
KnowledgeVault/01_Papers/ + 03_Methods/ + 04_Tasks/ + 05_Datasets/
    |
    | scan_registry.py (periodic re-scan)
    v
Paper_Processing_State.yaml (updated agent_state)
    |
    | scan_priority.py (NEW — extracts relevance from cards)
    v
Paper_Priority_Index.yaml (updated priorities)
    |
    v
Next batch cycle begins
```

### 5.3 Key Changes

| Component | Before | After | Rationale |
|---|---|---|---|
| Processing order | Arbitrary | Priority-index sorted | Efficient use of token budget |
| Primary skill | SKILL_Paper_Intake.md | SKILL_Paper_Batch_Process.md | Batch mode reduces overhead |
| Node creation | Ad-hoc | Mandatory node-check pre-step | Prevents directory clutter |
| Registry update | Manual | Auto-triggered after each batch | Keeps state current |
| Priority tracking | None | Paper_Priority_Index.yaml | Enables intelligent scheduling |
| Archive | None | Auto-archive completed papers | Reduces scan overhead |

### 5.4 New Artifacts

| Artifact | Purpose | Created By |
|---|---|---|
| `Paper_Priority_Index.yaml` | Dynamic paper relevance scoring | `scan_priority.py` (extracts from cards) |
| `scan_priority.py` | Extracts relevance/novelty/value from Literature Cards | Agent (post-processing) |
| Enhanced `SKILL_Paper_Batch_Process.md` | Batch processing with priority ordering | Agent (invoked) |
| Archive directory mechanism | Move 100%-complete papers out of active scan | `scan_registry.py` enhancement |

### 5.5 State Machine (Enhanced)

```
                    ┌─────────────────────────────────────────┐
                    │           Paper Lifecycle (Enhanced)     │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  Phase 0: Intake                         │
                    │  - Zotero verified                       │
                    │  - PDF exists                            │
                    │  - agent_state: all PENDING              │
                    └─────────────────────────────────────────┘
                                      │
                                      │ MinerU processing
                                      ▼
                    ┌─────────────────────────────────────────┐
                    │  Phase 1: Screening (Level 1)            │
                    │  - Literature Card created               │
                    │  - Relevance/novelty/value scored        │
                    │  - Priority index updated                │
                    │  - Decision: Ignore / Keep Ref / Deep Rd │
                    └─────────────────────────────────────────┘
                                      │
                          ┌───────────┼───────────┐
                          │           │           │
                    Ignore     Keep Ref     Deep Read
                    (Stop)     (Stop)        │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │  Phase 2: Deep Analysis (Level 2)        │
                    │  - Paper Note created                    │
                    │  - Method/Task/Dataset nodes checked     │
                    │  - Reproducibility analysis              │
                    │  - Decision: Proceed to Level 3?         │
                    └─────────────────────────────────────────┘
                                      │
                          ┌───────────┼───────────┐
                          │           │           │
                     No Trigger   Flag for     Proceed
                     (Stop)       Human Review  ▼
                                    │    ┌─────────────────────────────────────────┐
                                    └───►│  Phase 3: Argument Mining (Level 3)      │
                                         │  - Paper Logic created                   │
                                         │  - Evidence mapping                    │
                                         │  - Writing strategy analysis           │
                                         │  - Research gap identification         │
                                         └─────────────────────────────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────────────────────────────┐
                                    │  Phase 4: Archive                        │
                                    │  - All agent_state = COMPLETE            │
                                    │  - Move to KnowledgeVault/10_Archive/    │
                                    │  - Remove from active processing queue   │
                                    └─────────────────────────────────────────┘
```

### 5.6 File Modification Plan

| File | Action | Reason |
|---|---|---|
| `Paper_Processing_State.yaml` | No change | Already supports agent_state |
| `Paper_Priority_Index.yaml` | **CREATE** | Dynamic relevance tracking |
| `scan_priority.py` | **CREATE** | Extract priority from cards |
| `SKILL_Paper_Batch_Process.md` | **ENHANCE** | Add priority-based ordering |
| `SKILL_Knowledge_Node_Check.md` | **ENHANCE** | Make mandatory pre-step |
| `scan_registry.py` | **ENHANCE** | Add auto-trigger after batch |
| `research_config.yaml` | **UPDATE** | Fix Windows paths (Stage 6.2) |
| Templates | **UPDATE** | Fix Windows path examples (Stage 6.2) |

### 5.7 Rollback Plan

If Stage 6.3 enhancements cause issues:

1. **Priority index**: Delete `Paper_Priority_Index.yaml` — papers revert to arbitrary processing order
2. **Batch skill enhancement**: Revert `SKILL_Paper_Batch_Process.md` to original — use individual intake
3. **Registry auto-trigger**: Remove auto-trigger — revert to manual `scan_registry.py` invocation
4. **Archive mechanism**: Remove archive directory — all papers remain in active processing

**No data loss**: All changes are additive. Existing KnowledgeVault files, registry entries, and skills remain untouched.

---

## 6. Long-Term Architecture Assessment

### 6.1 Strengths

| Aspect | Rating | Notes |
|---|---|---|
| Three-layer separation | Excellent | Zotero → MinerU → KnowledgeVault is clean and maintainable |
| Decision Framework | Excellent | 3-level strategy prevents token waste |
| Skills system | Good | 9 skills cover all workflow stages |
| Registry tracking | Good | agent_state provides clear processing visibility |
| Duplicate prevention | Good | Multiple checks (mapping, index, directory) |
| Human-in-the-loop | Excellent | Semi-automatic mode (Mode B) ensures oversight |

### 6.2 Weaknesses

| Aspect | Risk | Mitigation |
|---|---|---|
| No priority indexing | Medium | Add Paper_Priority_Index.yaml |
| Manual batch invocation | Low | Enhance SKILL_Paper_Batch_Process.md |
| No archive mechanism | Low | Auto-archive completed papers |
| research_config.yaml paths | High (Stage 6.2) | Fix Windows paths |
| Template path examples | Low (Stage 6.2) | Fix template examples |

### 6.3 Scaling Projection

| Paper Count | Token Cost (Level 1) | Token Cost (Level 2) | Token Cost (Level 3) | Total |
|---|---|---|---|---|
| 33 (current) | ~10,000 | ~5,000 | ~2,000 | ~17,000 |
| 100 | ~30,000 | ~15,000 | ~5,000 | ~50,000 |
| 300 | ~90,000 | ~45,000 | ~15,000 | ~150,000 |
| 1,000 | ~300,000 | ~150,000 | ~50,000 | ~500,000 |
| 3,000 | ~900,000 | ~450,000 | ~150,000 | ~1,500,000 |

**Key insight**: The Decision Framework's 3-level structure naturally limits token costs. Even at 3,000 papers, total cost is ~1.5M tokens, which is manageable with modern LLM pricing.

### 6.4 Recommended Evolution Path

```
Stage 6.2: Config path remediation (HIGH priority)
    ↓
Stage 6.3: KnowledgeVault processing pipeline (MEDIUM priority)
    ↓
Stage 6.4: Priority index + batch automation (LOW priority)
    ↓
Stage 6.5: Archive mechanism + periodic audits (ONGOING)
```

---

## 7. Conclusion

### Is the current architecture sufficient for a long-term AI research assistant?

**Yes, with three enhancements**:

1. **Priority index** — Enables intelligent scheduling as paper count grows
2. **Batch-first workflow** — Reduces per-paper overhead through grouping
3. **Archive mechanism** — Keeps active processing queue manageable

**The architecture does NOT need**:

- A new orchestration layer (Skills system fills this role)
- Modified directory structure (frozen architecture is correct)
- Additional skills (existing 9 cover all operations)
- Changes to the Decision Framework (3-level strategy is optimal)

**The system is designed for human-AI collaboration, not full autonomy.** This is a strength, not a limitation. The semi-automatic permission model (Mode B) ensures quality control while leveraging AI for repetitive screening tasks.

---

*This document is a design review only. No files have been modified.*
