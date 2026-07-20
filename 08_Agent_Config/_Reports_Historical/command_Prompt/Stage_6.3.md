
# Stage 6.3 Implementation — KnowledgeVault Processing Pipeline

## Context

Stage 6.2 Config Path Remediation is COMPLETE.

Completed:
- research_config.yaml migrated to Linux paths
- Template path examples migrated
- No executable code modified
- Historical documents preserved

Current architecture baseline:
- Stage 5.5 Registry completed
- Stage 6.1 agent_state implemented
- Stage 6.1.1 Architecture Audit completed
- Stage 6.1.2 Architecture Proposal completed
- Stage 6.2 Config Remediation completed

Relevant documents:
- 08_Agent_Config/Migration/Stage_6.2_6.3_Architecture_Proposal.md
- 08_Agent_Config/Migration/Stage_6.3_Architecture_Review.md
- Paper_Processing_State.yaml
- SKILL_Paper_Intake.md
- SKILL_Paper_Batch_Process.md
- SKILL_Paper_Deep_Read.md
- SKILL_Registry_Scan.md

---

# Objective

Implement Stage 6.3:
Activate the KnowledgeVault paper processing pipeline.

The goal is NOT to redesign the architecture.

The goal is:

1. Complete missing Literature Cards for MinerU-complete papers
2. Ensure agent_state accurately reflects KnowledgeVault status
3. Establish a reliable paper processing workflow
4. Preserve the frozen architecture

---

# Architecture Constraints (IMPORTANT)

DO NOT:

- Create a new orchestration layer
- Modify the three-layer architecture:
  Zotero → MinerU → KnowledgeVault
- Modify agent_state schema
- Create unnecessary new skills
- Modify historical Stage reports
- Rewrite existing Skills architecture

The Skills system remains the workflow controller.

---

# Stage 6.3 Execution Plan

## Phase 1 — Registry Synchronization

First:

Run:

```

python 04_Tools/mineru/scan_registry.py

```

Generate the current processing state.

Report:

- Total papers
- PDFs available
- MinerU complete count
- Literature Card complete count
- Deep Read complete count
- Remaining pending papers

Do NOT modify files yet.

---

## Phase 2 — Identify Pending Literature Cards

Filter papers where:

```

mineru_state = MINERU_COMPLETE

AND

agent_state.literature_card = PENDING

AND

pdf_exists = TRUE

```

Generate a table:

| Paper Key | Title | Year | MinerU Status | Card Status |
|---|---|---|---|---|

Do not process yet.

Wait for confirmation.

---

## Phase 3 — Batch Literature Card Generation

After approval:

Use existing:

SKILL_Paper_Batch_Process.md

and

SKILL_Paper_Intake.md


Process papers sequentially.

For each paper:

1. Verify MinerU output:

```

ResearchAI_Data/Paper/MinerU_md/<paper_key>/full.md

```

2. Check duplicate:

Before creating:

```

02_KnowledgeVault/01_Papers/

```

verify no existing card.

3. Generate:

```

author_year_keyword_card.md

```

using existing template.

4. Update:

```

Paper_Processing_State.yaml

```

agent_state:

```

literature_card:
PENDING → COMPLETE

```

---

## Phase 4 — Registry Verification

After batch completion:

Run:

```

python 04_Tools/mineru/scan_registry.py

```

Verify:

- Every generated card is detected
- agent_state updated correctly
- No duplicate entries
- Paper_Index updated if applicable

---

# Deep Read Policy

Do NOT automatically generate Deep Read notes.

Deep Read requires:

1. Literature Card exists
2. Human selection
3. Explicit trigger

Follow:

SKILL_Paper_Deep_Read.md

Only process papers explicitly selected by user.

---

# Required Reports

After each phase provide:

## Phase Report

Include:

### Actions Taken

### Files Modified

### Files Created

### Validation Results

### Remaining Tasks

---

# Safety Rules

Before modifying any file:

Show:

1. Target file path
2. Modification purpose
3. Expected change

Wait for confirmation.

No bulk modification without approval.

---

Start with:

Phase 1 — Registry Synchronization only.
```



