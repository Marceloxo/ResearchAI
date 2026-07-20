# SKILL: Paper Logic

## Purpose

Generate Level 3 Argument Mining analysis for papers that have completed Level 1 (Literature Card) and Level 2 (Paper Note). Extracts argument structure, builds evidence mapping tables, justifies each module design, and identifies limitations.

## Input

```
Zotero Item Key
```

Example:
```
6VTKJ8W2
```

## Output

Creates a Paper Logic file in:
```
02_KnowledgeVault/09_Paper_Logic/{author}{year}_{keyword}_logic.md
```

Uses `Paper_Logic_Template.md` as the output format.

## Preconditions

1. Literature Card exists in `02_KnowledgeVault/01_Papers/` (Level 1 complete)
2. Paper Note exists in `02_KnowledgeVault/01_Papers/` (Level 2 complete)
3. Paper is classified as a research article (NOT a survey/review)
4. Paper Intake determined Level 3 eligibility
5. full.md exists in MinerU output

If any precondition is not met: STOP and report the missing prerequisite.

## Source Files

- `02_KnowledgeVault/01_Papers/<slug>_card.md` — Literature Card (Level 1)
- `02_KnowledgeVault/01_Papers/<slug>_note.md` — Paper Note (Level 2)
- `D:\ResearchAI_Data\Paper\MinerU_md/<folder>/full.md` — Raw paper text
- `08_Agent_Config/Paper_Processing_Decision_Framework.md` — Level determination criteria

## Workflow

### Step 1 — Locate Sources

Verify all precondition files exist:
1. Check Literature Card exists
2. Check Paper Note exists
3. Check full.md exists
4. Confirm paper is NOT a survey/review type

If any file is missing: STOP with specific error message.

### Step 2 — Extract Argument Structure

From the Paper Note and full.md, extract:
1. Main claim the paper makes
2. Each supporting claim (numbered list)
3. Evidence type for each claim (experimental, theoretical, comparative)
4. Experiment or result that supports each claim
5. Metrics used for validation
6. Whether the evidence fully supports, partially supports, or contradicts the claim

### Step 3 — Identify Research Gap

From the full.md Introduction and the card's "Why This Paper Matters":
1. Classify gaps into categories: Methodological, Empirical, Theoretical
2. List at least 3 specific gaps the paper addresses
3. Describe how the paper argues each gap exists (evidence from literature)

### Step 4 — Module Justification

For each major module/component in the paper's method:
1. Motivation — what problem does this module solve?
2. Design Choice — why this specific design?
3. Evidence — which experiment or result supports this design?
4. Alternatives Considered — what other designs were evaluated? Why were they rejected?

### Step 5 — Limitation Analysis

Identify limitations from two perspectives:
1. Author-admitted limitations (from Discussion/Conclusion sections)
2. Agent-identified limitations (claims lacking sufficient evidence, unsupported assertions)
3. For each limitation, note the severity (critical, moderate, minor)

### Step 6 — Evidence Mapping Table

Generate a structured table mapping claims to evidence:

| # | Claim | Evidence Type | Experiment | Metric | Result | Supported? |
|---|-------|--------------|------------|--------|--------|------------|
| 1 | | | | | | ✔ / ✘ / ⚠️ |

Supporting legend:
- ✔ = fully supported by experimental evidence
- ✘ = not supported or contradicted by evidence
- ⚠️ = partially supported with limitations

### Step 7 — Generate Execution Plan

Present plan to human:

```
Execution Plan:

Input:
  Zotero Item Key: <key>
  Source: full.md + Paper Note

Will create:
  02_KnowledgeVault/09_Paper_Logic/<filename>_logic.md

Will analyze:
  - Research problem and gap classification
  - Core claims and supporting evidence
  - Module-by-module justification
  - Limitation analysis (author-admitted + agent-identified)
  - Evidence mapping table (Claim -> Evidence -> Result)

Waiting for confirmation.
```

### Step 8 — Execute (After Confirmation)

1. Create Paper Logic file using `Paper_Logic_Template.md`
2. Fill all sections with extracted analysis
3. Append row to `MinerU_Zotero_Mapping.md`
4. Update `Paper_Index.md` with paper_logic entry
5. Update the existing card's reading_status if needed

## Validation Rules

After creating the Paper Logic file, verify:

1. Evidence mapping table has at least 2 rows
2. Each claim has at least one evidence entry
3. Limitation section has at least 1 identified limitation
4. Module justification covers all major modules (at least 1)
5. File is valid UTF-8 without BOM
6. No U+FFFD replacement characters
7. All wikilinks follow [[WikiLink]] format

## Failure Handling

| Condition | Action |
|---|---|
| No Literature Card exists | STOP — run Paper Intake first |
| No Paper Note exists | STOP — run Deep Read first |
| Paper is a survey/review | STOP — use Survey Process instead |
| full.md missing | STOP — report incomplete processing |
| Paper type unclear | FLAG for human review |
| Evidence mapping has fewer than 2 rows | WARNING — flag incomplete analysis |

## Human Confirmation Points

1. After Step 7 (before Step 8): Present execution plan and wait for approval
2. If evidence mapping is incomplete: Flag for human review before proceeding

## Constraints

- **Mode B (Semi-Automatic)**: No modifications before human confirmation
- **Requires Literature Card**: Cannot run without Level 1 completion
- **Requires Paper Note**: Cannot run without Level 2 completion
- **Cannot replace Deep Read**: Deep Read must run first; Paper Logic is a downstream analysis
- **Cannot process survey papers**: Survey papers use Survey Process instead
- **Do NOT fabricate**: All evidence must come from the paper; if evidence is not found, mark as "Not Found Yet"
- **Do NOT modify templates**: Use Paper_Logic_Template.md as-is
- **All claims must be traceable** to existing KV files (card, note, full.md)
