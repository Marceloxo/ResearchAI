# Literature Processing Strategy

## Overview

This document defines how ResearchAI processes academic papers. The strategy follows a **three-level filtering pipeline** that balances depth of analysis against token cost and knowledge quality.

---

## Current Processing Mode

### Manual Pipeline (Current)

```
PDF (from 01_Literature/PDFs/ or 00_Inbox/)
    ↓
MinerU Desktop GUI → Manual Export
    ↓
full.md output (manually organized)
    ↓
AI agent reads full.md for analysis
    ↓
KnowledgeVault notes created
```

**Limitations:**
- One PDF at a time
- Manual file management
- No automated trigger from Inbox to KnowledgeVault

**Advantages:**
- Full control over which papers enter the pipeline
- No dependency on CLI tooling
- Validated on real paper content (see Stage 1.4A Test Report)

---

## Three-Level Processing Pipeline

### Level 1: Literature Screening

**Purpose:** Rapid classification of 50-100 papers to decide which deserve deep analysis.

**Input:** MinerU `full.md` output

**Output:** `Literature Card` note in `01_Papers/`

**Decision Tree:**
```
Read Literature Card
    ↓
Is this paper directly relevant to current research?
    ├─ Yes → Mark "Read deeply" → Proceed to Level 2
    ├─ Maybe → Mark "Keep reference" → Revisit later
    └─ No → Mark "Ignore" → Skip
```

**Token Cost:** Low (~200-300 tokens per paper for analysis)

**Rule:** Never skip Level 1. Always screen before deep reading.

---

### Level 2: Deep Analysis

**Purpose:** Full understanding of selected papers. Extract methods, tasks, datasets, and insights.

**Input:** Papers marked "Read deeply" from Level 1

**Output:**
- `Paper Note` in `01_Papers/`
- `Method` notes in `03_Methods/` (if novel methods are introduced)
- `Task` notes in `04_Tasks/` (if new task definitions emerge)
- `Dataset` notes in `05_Datasets/` (if new datasets are documented)
- `Topic` updates in `02_Topics/` (if existing topics need expansion)

**Token Cost:** Medium (~1000-2000 tokens per paper for analysis)

**Rules:**
- Only process papers that passed Level 1 screening.
- Distinguish between papers that propose new methods vs. papers that review existing methods.
- For survey papers: extract taxonomy, not individual method details.
- For primary research: extract method, dataset, results, limitations.

---

### Level 3: Research Development

**Purpose:** Turn deep knowledge into research output — experiments, ideas, and writing.

**Input:** Core papers from Level 2

**Output:**
- `Experiment` notes in `06_Experiments/`
- `Idea` notes in `07_Ideas/`
- `Writing` notes in `08_Writing/`

**Token Cost:** High (variable, depends on research depth)

**Rules:**
- Only proceed to Level 3 for papers that inspire active research.
- Every experiment must link back to its originating idea and paper.
- Every idea must link back to the paper/method/task that inspired it.

---

## Token Optimization Principle

### Do NOT

- Generate a full knowledge graph for every paper.
- Create method/task/dataset notes for papers that will be ignored.
- Reproduce paper content verbatim in KnowledgeVault.
- Process papers in parallel without screening first.

### DO

- Screen first, expand later.
- Compress knowledge into structured summaries.
- Link to external sources instead of duplicating content.
- Use Literature Cards as a filter before investing in deep analysis.

### Estimated Token Budget Per Paper

| Level | Tokens Spent | Tokens Saved (vs. full paper) |
|---|---|---|
| Level 1 (Screening) | ~300 | 95%+ |
| Level 2 (Deep Read) | ~1500 | 85%+ |
| Level 3 (Research Dev) | ~5000+ | Variable |

---

## Future: Automated Pipeline

When MinerU CLI is available, the pipeline will evolve to:

```
Watch Folder (00_Inbox/*.pdf)
    ↓
MinerU CLI → full.md (batch)
    ↓
Auto Level 1 Screening (AI agent)
    ↓
Level 2 Deep Read (selected papers)
    ↓
Level 3 Research (core papers)
```

This is a future goal. Current validation proves the manual pipeline works correctly.
