# Stage 1.5-7E.3 Skill Implementation Specification

> **????**: 2026-07-10
> **????**: Stage 1.5-7E.1 (Architecture Review), Stage 1.5-7E.2 (Expansion Design)
> **????**: ?????????????????
> **???**: Agnes (ResearchAI Agent)

---

## Executive Summary

This document specifies the implementation design for 3 new ResearchAI skills identified in Stage 1.5-7E.1 and approved in Stage 1.5-7E.2:

| Skill | Command | Template | Storage | Blocking Workflow |
|-------|---------|----------|---------|-------------------|
| Paper Logic | `/SKILL Paper Logic` | Paper_Logic_Template.md | 09_Paper_Logic/ | Yes - Level 3 dead-end |
| Survey Process | `/SKILL Survey Process` | Survey_Template.md | 01_Papers/ | Yes - Survey classification |
| Method Node | `/SKILL Method Node` | Method_Template.md | 03_Methods/ | No - Manual creation works |

**Implementation constraint**: This stage only generates specifications. No files are created or modified.

---

## Skill 1: Paper Logic

### 1. Skill Identity

| Attribute | Value |
|-----------|-------|
| Command | `/SKILL Paper Logic` |
| Purpose | Generate Level 3 Argument Mining analysis for papers classified as Level 3 |
| Pipeline Position | Paper Intake -> Deep Read -> **Paper Logic** |
| Trigger Condition | Paper Intake determines Level 3 eligibility, OR user explicitly requests Level 3 analysis |
| Input | Zotero Item Key |
| Output | Paper_Logic_Template.md in 09_Paper_Logic/ |
| Permission Mode | Mode B (Semi-Automatic) |

### 2. Workflow Design

#### Preconditions
1. Literature Card exists for the paper (Level 1 complete)
2. Paper Note exists for the paper (Level 2 complete) ? Deep Read must have been executed
3. Paper Intake determined Level 3 eligibility
4. Paper is NOT a survey/review paper (those use Survey Process)

#### Source Files
- `02_KnowledgeVault/01_Papers/{slug}_card.md` ? Literature Card
- `02_KnowledgeVault/01_Papers/{slug}_note.md` ? Paper Note (Level 2 analysis)
- `D:\ResearchAI_Data\Paper\MinerU_md/{folder}/full.md` ? Raw paper text
- `08_Agent_Config/Paper_Processing_Decision_Framework.md` ? Level determination criteria

#### Processing Steps

```
Step 1: Locate Sources
  - Verify card exists
  - Verify note exists
  - Verify full.md exists
  - If any missing: STOP with error

Step 2: Extract Argument Structure from Paper Note
  - Read Level 2 note for: Research Problem, Contributions, Methods, Results
  - Identify each claim the paper makes
  - Identify each piece of evidence/experiment supporting claims
  - Map: Claim -> Evidence Type -> Experiment -> Metric -> Result

Step 3: Identify Research Gap
  - From Introduction section of full.md
  - From "Why This Paper Matters" in card
  - Classify gaps into: Methodological, Empirical, Theoretical

Step 4: Module Justification
  - For each module/component in the paper's method:
    - Extract motivation (why does it exist?)
    - Extract design choice (why this design?)
    - Extract evidence (which experiment supports it?)
    - Extract alternatives considered (what else was tried?)

Step 5: Limitation Analysis
  - Extract author-admitted limitations
  - Identify unsupported claims (evidence gap)
  - Identify claims with weak evidence

Step 6: Generate Evidence Mapping Table
  - Create structured table: Claim | Evidence Type | Experiment | Metric | Result | Supported?
  - Mark each: ? (fully supported), ? (not supported), ?? (partially supported)

Step 7: Generate Execution Plan
  - Present plan to human for confirmation

Step 8: Execute (After Confirmation)
  - Create Paper_Logic_Template.md in 09_Paper_Logic/
  - Fill all sections from extracted analysis
  - Update MinerU_Zotero_Mapping.md (add paper_logic entry)
  - Update Paper_Index.md (add paper_logic entry)
```

#### Validation Steps
1. Evidence mapping table has at least 2 rows
2. Each claim has at least one evidence entry
3. Limitation section has at least 1 identified limitation
4. Module justification covers all major modules
5. File is valid UTF-8 without BOM

#### Failure Handling
| Condition | Action |
|-----------|--------|
| No card exists | STOP ? run Paper Intake first |
| No note exists | STOP ? run Deep Read first |
| Paper is a survey | STOP ? use Survey Process instead |
| full.md missing | STOP ? report incomplete processing |
| Paper type unclear | FLAG for human review |

#### Human Confirmation Points
- After Step 7: Present execution plan with estimated output
- Before Step 8: Require explicit approval

### 3. Dependency Analysis

```
Zotero Item Key
    |
    v
Paper Intake (creates card)
    |
    v
Deep Read (creates note)
    |
    v
Paper Logic (creates argument analysis)
```

Paper Logic has a strict linear dependency on Paper Intake -> Deep Read. It cannot function without both upstream skills.

### 4. Template Mapping

**Template**: `02_KnowledgeVault/Templates/Paper_Logic_Template.md`

| Template Section | Skill Output | Data Source |
|-----------------|--------------|-------------|
| Research Problem | Extracted from full.md Introduction + card "Why This Paper Matters" | full.md, card |
| Research Gap | Extracted from full.md + card | full.md, card |
| Core Claim | Extracted from full.md + note | full.md, note |
| Evidence Mapping | Structured table from note + full.md experiments | note, full.md |
| Method Justification | Module-by-module analysis from note + full.md | note, full.md |
| Limitation Analysis | Author-admitted + agent-identified | full.md, note |

**Naming Convention**: `{author}{year}_{keyword}_logic.md`
**Storage Location**: `02_KnowledgeVault/09_Paper_Logic/`

### 5. Collision Check

| Existing Skill | Overlap? | Resolution |
|---------------|----------|------------|
| Paper Intake | No ? Intake creates cards, Logic analyzes arguments | Distinct purposes |
| Deep Read | No ? Deep Read creates notes, Logic consumes notes | Dependency, not overlap |
| Literature Synthesis | No ? Synthesis generates writing materials from multiple papers | Distinct output |
| Knowledge Node Check | No ? Check prevents duplication, Logic creates paper-specific analysis | Distinct purposes |

---

## Skill 2: Survey Process

### 1. Skill Identity

| Attribute | Value |
|-----------|-------|
| Command | `/SKILL Survey Process` |
| Purpose | Generate survey/review paper analysis with taxonomy construction |
| Pipeline Position | Paper Intake -> **Survey Process** (alternative to Deep Read for survey papers) |
| Trigger Condition | Paper Intake classifies paper as survey/review type |
| Input | Zotero Item Key |
| Output | Survey_Template.md in 01_Papers/ |
| Permission Mode | Mode B (Semi-Automatic) |

### 2. Workflow Design

#### Preconditions
1. Literature Card exists for the paper (Level 1 complete)
2. Paper is classified as survey/review type by Paper Intake
3. full.md exists in MinerU output

#### Source Files
- `02_KnowledgeVault/01_Papers/{slug}_card.md` ? Literature Card
- `D:\ResearchAI_Data\Paper\MinerU_md/{folder}/full.md` ? Raw paper text

#### Processing Steps

```
Step 1: Locate Sources
  - Verify card exists
  - Verify full.md exists
  - If any missing: STOP with error

Step 2: Extract Taxonomy from full.md
  - Identify all task categories the survey covers
  - Identify all method families discussed
  - Identify all datasets reviewed
  - Build structured taxonomies for each category

Step 3: Coverage Analysis
  - Identify well-covered areas (extensive discussion)
  - Identify under-researched areas (mentioned briefly or not at all)
  - Identify emerging trends noted by the survey

Step 4: Key Findings Extraction
  - Extract the survey's main conclusions
  - Extract future research directions proposed
  - Compare with other surveys if mentioned

Step 5: My Analysis
  - Identify transferable insights for current research
  - Identify research gaps that could become research directions
  - Assess relevance to current research projects

Step 6: Generate Execution Plan
  - Present plan to human for confirmation

Step 7: Execute (After Confirmation)
  - Create Survey_Template.md in 01_Papers/
  - Update MinerU_Zotero_Mapping.md
  - Update Paper_Index.md
```

#### Validation Steps
1. Taxonomy has at least 3 categories
2. Coverage analysis identifies both well-covered and under-researched areas
3. At least 2 key findings extracted
4. File is valid UTF-8 without BOM

#### Failure Handling
| Condition | Action |
|-----------|--------|
| No card exists | STOP ? run Paper Intake first |
| Paper is not a survey | STOP ? use Deep Read instead |
| full.md missing | STOP ? report incomplete processing |

#### Human Confirmation Points
- After Step 6: Present execution plan

### 3. Dependency Analysis

```
Zotero Item Key
    |
    v
Paper Intake (classifies as survey)
    |
    +---> Deep Read (for research articles)
    |
    +---> Survey Process (for survey papers)
```

Survey Process is an **alternative branch** to Deep Read, not a successor. It shares the Paper Intake dependency.

### 4. Template Mapping

**Template**: `02_KnowledgeVault/Templates/Survey_Template.md`

| Template Section | Skill Output | Data Source |
|-----------------|--------------|-------------|
| Taxonomy | Constructed from full.md method/task/dataset discussions | full.md |
| Coverage Analysis | Identified from discussion depth in full.md | full.md |
| Key Findings | Extracted from conclusion/discussion sections | full.md |
| Future Research | Extracted from survey's future directions | full.md |
| My Analysis | Agent-generated based on survey content | Agent judgment |

**Naming Convention**: `{author}{year}_{keyword}_survey.md`
**Storage Location**: `02_KnowledgeVault/01_Papers/`

### 5. Collision Check

| Existing Skill | Overlap? | Resolution |
|---------------|----------|------------|
| Paper Intake | No ? Intake classifies, Survey Process generates analysis | Distinct purposes |
| Deep Read | No ? Deep Read is for research articles, Survey for surveys | Alternative branches |
| Literature Synthesis | No ? Synthesis combines multiple papers, Survey analyzes one | Distinct scope |
| Knowledge Node Check | No ? Check prevents duplication, Survey creates paper analysis | Distinct purposes |

---

## Skill 3: Method Node

### 1. Skill Identity

| Attribute | Value |
|-----------|-------|
| Command | `/SKILL Method Node` |
| Purpose | Create Method knowledge nodes extracted from Paper Notes |
| Pipeline Position | Deep Read -> **Method Node** (knowledge graph growth) |
| Trigger Condition | Knowledge Node Check recommends "Create" for a method concept, OR user explicitly requests |
| Input | Concept name (from Knowledge Node Check) |
| Output | Method_Template.md in 03_Methods/ |
| Permission Mode | Mode B (Semi-Automatic) |

### 2. Workflow Design

#### Preconditions
1. At least one Paper Note exists that discusses the method
2. Knowledge Node Check has been run and recommends "Create" (or user explicitly requests)
3. Method name is unambiguous

#### Source Files
- `02_KnowledgeVault/01_Papers/*_note.md` ? All paper notes discussing the method
- `02_KnowledgeVault/00_Meta/Method_Map.md` ? Existing method map (for cross-reference)
- `02_KnowledgeVault/03_Methods/` ? Existing method nodes (for deduplication)

#### Processing Steps

```
Step 1: Locate Sources
  - Search all paper notes for mentions of the method
  - Check Method_Map.md for existing entries
  - Check 03_Methods/ for existing nodes
  - If node exists: STOP ? offer update instead

Step 2: Extract Method Definition
  - From paper notes: extract the method's core definition
  - Identify the key insight/innovation
  - Extract mathematical formulation if present

Step 3: Identify Architecture/Formula
  - Extract network structure description
  - Extract key equations
  - Extract architectural diagrams description

Step 4: List Advantages
  - Extract claimed advantages from paper notes
  - Extract comparative results (vs. other methods)

Step 5: Identify Limitations
  - Extract author-admitted limitations
  - Identify practical constraints

Step 6: Find Related Papers
  - Extract [[wikilinks]] to related papers from notes
  - Identify predecessor and successor methods

Step 7: Find Related Methods
  - Extract [[wikilinks]] to related methods
  - Identify variants and alternatives

Step 8: Generate Execution Plan
  - Present plan to human for confirmation

Step 9: Execute (After Confirmation)
  - Create Method_Template.md in 03_Methods/
  - Update Method_Map.md
  - Update relevant paper notes with back-links
```

#### Validation Steps
1. Definition is a single clear sentence
2. At least 1 advantage listed
3. At least 1 limitation identified
4. Related papers list has at least 1 entry
5. File is valid UTF-8 without BOM

#### Failure Handling
| Condition | Action |
|-----------|--------|
| Method name ambiguous | FLAG for human review |
| No source notes found | STOP ? no evidence to extract from |
| Method already exists | STOP ? offer update instead |

#### Human Confirmation Points
- After Step 8: Present execution plan
- Before Step 9: Require explicit approval

### 3. Dependency Analysis

```
Paper Notes (created by Deep Read)
    |
    v
Knowledge Node Check (recommends "Create")
    |
    v
Method Node (creates method node)
```

Method Node depends on Knowledge Node Check for the "Create" recommendation, but can also be triggered directly by user request.

### 4. Template Mapping

**Template**: `02_KnowledgeVault/Templates/Method_Template.md`

| Template Section | Skill Output | Data Source |
|-----------------|--------------|-------------|
| Definition | Extracted from paper notes | All notes mentioning method |
| Core Idea | Extracted from paper notes | All notes mentioning method |
| Architecture/Formula | Extracted from paper notes | All notes mentioning method |
| Advantages | Extracted from paper notes | All notes mentioning method |
| Limitations | Extracted from paper notes | All notes mentioning method |
| Typical Applications | Extracted from paper notes | All notes mentioning method |
| Related Papers | Extracted from [[wikilinks]] in notes | All notes mentioning method |
| Related Methods | Extracted from [[wikilinks]] in notes | All notes mentioning method |

**Naming Convention**: `{method_name}.md` (e.g., `Transformer.md`, `Attention Mechanism.md`)
**Storage Location**: `02_KnowledgeVault/03_Methods/`

### 5. Collision Check

| Existing Skill | Overlap? | Resolution |
|---------------|----------|------------|
| Knowledge Node Check | No ? Check is preventive, Node is generative | Complementary |
| Research Map Update | No ? Map Update maintains navigation, Node creates content | Distinct purposes |
| Deep Read | No ? Deep Read creates paper notes, Node extracts from notes | Dependency, not overlap |

---

## Dependency Graph

### Complete Dependency Structure

```
Paper Intake
    |
    +---> Deep Read -----> Paper Logic (NEW)
    |       |
    |       +---> Method Node (NEW)
    |
    +---> Survey Process (NEW) [alternative branch]
    |
    +---> Paper Update

Knowledge Node Check
    |
    +---> Method Node (NEW) [via "Create" recommendation]

Research Map Update
    (independent maintenance)

Literature Synthesis
    (independent ? consumes notes/cards)

Architecture Audit
    (independent ? read-only)

Encoding Audit
    (independent ? read-only)
```

### Dependency Properties

1. **Acyclic**: No circular dependencies exist
2. **Linear critical path**: Paper Intake -> Deep Read -> Paper Logic (3-step chain)
3. **Alternative branch**: Survey Process branches from Paper Intake
4. **Feedback loop**: Method Node -> Research Map Update (method nodes update the map)

---

## Template Mapping

### Template Coverage After Implementation

| Template | Before | After | Status |
|----------|--------|-------|--------|
| Literature_Card_Template.md | Paper Intake / Batch Process | Same | PASS |
| Paper_Template.md | Deep Read | Same | PASS |
| Paper_Logic_Template.md | **NONE** | Paper Logic | **NEW** |
| Survey_Template.md | **NONE** | Survey Process | **NEW** |
| Method_Template.md | **NONE** | Method Node | **NEW** |
| Task_Template.md | NONE | NONE | Deferred |
| Dataset_Template.md | NONE | NONE | Deferred |
| Idea_Template.md | NONE | NONE | Deferred |
| Experiment_Template.md | NONE | NONE | Deferred |
| Writing_Template.md | NONE | NONE | Deferred |

**Coverage**: 4/10 before -> 7/10 after (70%)

### Template Consistency Check

All three new templates follow the same structure:
- YAML frontmatter with metadata
- Bilingual section headers (English / Chinese)
- Wikilink support for cross-references
- Consistent naming conventions

---

## Implementation Roadmap

### Phase A: Create Reference Workflow Files

| # | File | Content | Dependencies |
|---|------|---------|-------------|
| 1 | references/literature/paper_logic.md | Paper Logic workflow | Deep Read reference exists |
| 2 | references/literature/survey_process.md | Survey Process workflow | Paper Intake reference exists |
| 3 | references/knowledge/method_node.md | Method Node workflow | Knowledge Node Check reference exists |

**Estimated effort**: 3 reference files, ~3000 chars each
**Risk**: LOW ? All upstream references exist

### Phase B: Update SKILL.md Manifest

| # | Action | Content |
|---|--------|---------|
| 1 | Add to Quick Reference table | 3 new rows |
| 2 | Add to Workflows section | 3 new workflow entries (10, 11, 12) |
| 3 | Update description field | Add "argument mining, survey processing, method node creation" |

**Estimated effort**: 3 table rows + 3 workflow entries + description update
**Risk**: LOW ? SKILL.md structure is flexible

### Phase C: Validation Tests

| # | Test Case | Expected Result |
|---|-----------|----------------|
| 1 | Paper Logic on chai2020_using (existing paper) | Logic file created with 3+ evidence rows |
| 2 | Survey Process on chen2022_rs_transformer_cd (existing survey) | Survey file created with 3+ taxonomy categories |
| 3 | Method Node for "Transformer" (existing method) | Node created or update offered |

**Risk**: MEDIUM ? Requires actual paper processing (read-only test mode recommended)

---

## Validation Plan

### Pre-Implementation Validation

| Check | Method | Pass Criteria |
|-------|--------|--------------|
| Reference files parse as valid Markdown | File read test | No syntax errors |
| SKILL.md Quick Reference table renders correctly | Markdown lint | Valid table format |
| No broken references in SKILL.md | Link check | All 12 references resolve |
| Templates exist and are readable | File existence check | All 3 templates found |

### Post-Implementation Validation

| Check | Method | Pass Criteria |
|-------|--------|--------------|
| Paper Logic produces valid output | Run on test paper | File created, UTF-8, no mojibake |
| Survey Process produces valid output | Run on test survey | File created, UTF-8, no mojibake |
| Method Node produces valid output | Run on test method | File created or update offered |
| Encoding compliance | UTF-8 decode test | 0 replacement characters |
| Permission model compliance | Mode B check | Human confirmation required |

### Regression Validation

| Check | Method | Pass Criteria |
|-------|--------|--------------|
| Existing skills still work | Run Paper Intake, Deep Read | No behavior change |
| No template modifications | Template diff | No changes |
| No directory structure changes | Directory listing | Same structure |
| No KnowledgeVault modifications | KV diff | No changes |

---

## Risk Assessment

| Risk | Severity | Probability | Mitigation |
|------|----------|------------|------------|
| Paper Logic depends on Deep Read existing | HIGH | Certain | Enforce precondition check in workflow |
| Survey Process conflicts with Deep Read | MEDIUM | Possible | Clear classification trigger from Paper Intake |
| Method Node creates duplicate nodes | MEDIUM | Possible | Deduplication check against existing 03_Methods/ |
| SKILL.md becomes too long | LOW | Possible | Keep descriptions concise, reference files handle detail |
| Permission model violated | HIGH | Possible | Mode B enforcement in each workflow |

### Critical Risks

1. **Paper Logic requires Deep Read first**: If Deep Read hasn't been run, Paper Logic will fail. Mitigation: Precondition check + clear error message.
2. **Survey Process vs Deep Read confusion**: User might confuse when to use each. Mitigation: Paper Intake classification determines the branch.

---

## Final Verdict

| Check | Result |
|---|---|
| Skill identity defined | **PASS** |
| Workflow design complete | **PASS** |
| Dependency analysis valid | **PASS** |
| Template mapping verified | **PASS** |
| Collision check clean | **PASS** |
| Implementation order logical | **PASS** |
| Testing plan adequate | **PASS** |

**Overall: PASS**

The implementation specification is complete and ready for execution. All 3 skills have:
- Clear identity and purpose
- Complete workflow designs with preconditions and failure handling
- Valid dependency chains (acyclic)
- Verified template mappings
- No overlap with existing skills
- Concrete testing plan

**Recommendation**: Proceed to Phase A (reference file creation) immediately.

---

*Stage 1.5-7E.3 Skill Implementation Specification completed*
*Generated: 2026-07-10 | Agent: Agnes (ResearchAI)*
