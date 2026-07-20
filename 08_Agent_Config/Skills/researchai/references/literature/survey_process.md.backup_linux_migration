# SKILL: Survey Process

## Purpose

Generate survey/review paper analysis with taxonomy construction, coverage analysis, and research direction identification. This skill is an alternative branch to Deep Read for survey/review papers classified at Level 1.

## Input

```
Zotero Item Key
```

Example:
```
46C4TYYR
```

## Output

Creates a Survey paper file in:
```
02_KnowledgeVault/01_Papers/{author}{year}_{keyword}_survey.md
```

Uses `Survey_Template.md` as the output format. Sets `paper_type: survey` in frontmatter.

## Preconditions

1. Literature Card exists in `02_KnowledgeVault/01_Papers/` (Level 1 complete)
2. Paper is classified as survey/review type by Paper Intake
3. full.md exists in MinerU output
4. Paper is NOT a research article (those use Deep Read)

If any precondition is not met: STOP and report the missing prerequisite.

## Source Files

- `02_KnowledgeVault/01_Papers/<slug>_card.md` — Literature Card (Level 1)
- `D:\ResearchAI_Data\Paper\MinerU_md\<folder>\full.md` — Raw paper text

## Workflow

### Step 1 — Locate Sources

Verify all precondition files exist:
1. Check Literature Card exists
2. Confirm paper type is survey/review
3. Check full.md exists

If any file is missing: STOP with specific error message.

### Step 2 — Extract Survey Taxonomy

From the full.md, construct structured taxonomies:

1. **Task Taxonomy**: Identify all task categories the survey covers
   - Extract task names and brief descriptions
   - Note which tasks are most discussed vs. barely mentioned

2. **Method Taxonomy**: Identify all method families discussed
   - Group methods by architectural family (e.g., CNN-based, Transformer-based, hybrid)
   - Note key innovations in each family

3. **Dataset Taxonomy**: Identify all datasets reviewed
   - List dataset names, sizes, and domains
   - Note which datasets are most commonly used

### Step 3 — Coverage Analysis

Analyze the depth of coverage in each taxonomy area:

1. **Well-Covered Areas**: Topics with extensive discussion, multiple papers cited, detailed comparisons
2. **Under-Researched Areas**: Topics mentioned briefly or absent despite relevance
3. **Emerging Trends**: New directions identified by the survey authors

### Step 4 — Key Findings Extraction

Extract the survey's main conclusions:
1. Summarize the 3-5 key findings from the Conclusion section
2. Note any consensus or disagreement in the field
3. Identify methodological patterns across surveyed papers

### Step 5 — Research Direction Analysis

From the survey's Future Research Directions section:
1. List each proposed research direction
2. Assess feasibility (high/medium/low)
3. Identify potential connections to current research interests
4. Note any research gaps that could become personal research directions

### Step 6 — Generate Execution Plan

Present plan to human:

```
Execution Plan:

Input:
  Zotero Item Key: <key>
  Source: full.md

Will create:
  02_KnowledgeVault/01_Papers/<filename>_survey.md

Will analyze:
  - Task, method, and dataset taxonomies
  - Coverage analysis (well-covered vs. under-researched areas)
  - Key findings and consensus points
  - Future research directions with feasibility assessment
  - Transferable insights for current research

Waiting for confirmation.
```

### Step 7 — Execute (After Confirmation)

1. Create Survey file using `Survey_Template.md`
2. Fill all sections with extracted analysis
3. Append row to `MinerU_Zotero_Mapping.md`
4. Update `Paper_Index.md` with survey entry
5. Update the existing card's reading_status if needed

## Validation Rules

After creating the Survey file, verify:

1. Taxonomy has at least 3 categories per dimension (task, method, dataset)
2. Coverage analysis identifies both well-covered and under-researched areas
3. At least 2 key findings extracted
4. At least 1 future research direction identified
5. File is valid UTF-8 without BOM
6. No U+FFFD replacement characters
7. paper_type field is set to "survey"

## Failure Handling

| Condition | Action |
|---|---|
| No Literature Card exists | STOP — run Paper Intake first |
| Paper is not a survey/review | STOP — use Deep Read instead |
| full.md missing | STOP — report incomplete processing |
| Taxonomy cannot be constructed | FLAG for human review |

## Human Confirmation Points

1. After Step 6 (before Step 7): Present execution plan and wait for approval

## Constraints

- **Survey/review papers only**: This skill must NOT be used for research articles
- **Alternative branch to Deep Read**: Paper Intake classification determines which path to take
- **Requires Literature Card**: Cannot run without Level 1 completion
- **Mode B (Semi-Automatic)**: No modifications before human confirmation
- **Do NOT fabricate**: All taxonomy entries and findings must come from the survey paper
- **Do NOT modify templates**: Use Survey_Template.md as-is
- **All claims must be traceable** to existing KV files (card, full.md)
