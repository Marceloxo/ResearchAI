# Stage 1.5-6B 鈥?Real Paper Stress Test Protocol

## Objective

Validate whether the complete ResearchAI literature workflow works under realistic research conditions.

This is NOT a theoretical exercise. The stress test uses real papers from the researcher's actual reading list, processed through the full pipeline:

```
Zotero 鈫?MinerU 鈫?Processed Markdown 鈫?Literature Card 鈫?Paper Note 鈫?Knowledge Nodes 鈫?Paper Logic
```

The goal is to discover **workflow failures, template gaps, and agent mistakes** before scaling to batch processing.

---

## Test Categories

Four paper categories ensure the pipeline handles diversity in paper types, quality, and reproducibility status.

### Category A 鈥?Survey / Review Paper

**Purpose:** Validate taxonomy extraction and landscape analysis.

**Selection Criteria:**
- Recent (last 5 years) survey or review paper
- Relevant to seismic AI / deep learning / computer vision
- Covers a broad topic area (not narrowly scoped)
- Has clear taxonomies or classification schemes

**What to Validate:**
- Survey_Template.md usage (not Paper_Template.md)
- Research taxonomy extraction accuracy
- Method landscape mapping completeness
- Future direction identification quality
- No method-specific details incorrectly extracted (surveys don't propose methods)
- Coverage assessment is fair (not missing major subfields)

**Known Issue to Watch For:**
The agent may confuse survey papers with research articles. Ensure the template selection decision tree (from Paper_Processing_Decision_Framework.md) correctly routes surveys to Survey_Template.

---

### Category B 鈥?Classic Method Paper

**Purpose:** Validate method extraction and architectural understanding.

**Selection Criteria:**
- Well-known paper that introduced a widely-used method
- Clear architecture description with figures
- Reproducible (code available or implementation details sufficient)
- Has been cited extensively (established impact)

**What to Validate:**
- Method_Template.md generates accurate description
- Architecture understanding is correct (not hallucinated)
- Contribution identification matches the paper's own claims
- Paper Logic Argument Mining is thorough
- Evidence Mapping connects each claim to specific experiments
- Method Justification covers all major modules, not just the novelty

**Known Issue to Watch For:**
The agent may overstate the novelty or miss the actual contribution among multiple contributions. Cross-check against the paper's own contribution statement.

---

### Category C 鈥?Advanced Research Paper

**Purpose:** Validate analysis of advanced research papers beyond basic screening.

This category is split into two subcategories based on paper type.

#### C1 鈥?Application / Validation Study

**Purpose:** Evaluate real-world deployment, generalization, and reproducibility of existing methods.

**Selection Criteria:**
- Applies known methods to new data/regions/domains
- Tests generalization across different conditions
- Demonstrates practical utility or workflow validation
- May or may not propose new methodological improvements

**What to Validate:**
- Correctly identifies paper as application study (not method paper)
- Evaluates cross-domain generalization claims
- Assesses reproducibility in new context
- Identifies practical limitations not mentioned by authors
- Extracts transferable insights for own research

**Known Issue to Watch For:**
The agent may incorrectly classify an application paper as a method paper. Ensure the template selection correctly distinguishes "applies existing method" from "proposes new method."

#### C2 鈥?Method Innovation / SOTA Architecture

**Purpose:** Evaluate novel architecture design, module justification, ablation quality, and claim-evidence consistency.

**Selection Criteria:**
- Introduces genuinely new architecture or module design
- Has comprehensive ablation studies
- Reports state-of-the-art results on relevant benchmarks
- Contains detailed experimental validation

**What to Validate:**
- Novel contribution extraction distinguishes incremental from significant advances
- Experimental analysis captures all baselines and comparisons
- Ablation study extraction is complete and correctly attributed
- Reproducibility evaluation is honest (don't inflate "Available" if code is partial)
- Paper-to-Own-Research Bridge identifies actionable transfer ideas
- Hidden Limitations section catches real weaknesses (not just author-admitted ones)

**Known Issue to Watch For:**
The agent may accept the paper's claims at face value without critical analysis. The Limitation Analysis section should push back and identify gaps the paper itself doesn't acknowledge.

---

### Category D 鈥?Reproduction-Oriented Paper

**Purpose:** Validate the reproducibility metadata system introduced in Stage 1.5-6A.1.

**Selection Criteria:**
- Has publicly available code (GitHub, GitLab, or similar)
- Uses a well-known dataset
- Contains detailed implementation information
- Suitable for potential reproduction on RTX 4070 hardware

**What to Validate:**
- Literature Card correctly identifies code platform and URL
- Paper Note's Missing Details table is filled (not left blank)
- Reproduction Feasibility assessment is accurate (not overly optimistic)
- Dataset availability is correctly assessed (public vs. restricted vs. private)
- The "Found In" checkbox accurately reflects where code availability was mentioned
- Reproduction notes flag hardware constraints (e.g., "requires >12GB VRAM, RTX 4070 may struggle")

**Known Issue to Watch For:**
The agent may assume code is available when it's only "available upon request" (which is effectively unavailable). Strict criteria: code must be in a public repository with runnable scripts.

---

## Per-Paper Tracking Form

For each paper processed in the stress test, record the following information.

### Before Processing

| Field | Value |
|---|---|
| Paper ID | <!-- researchai identifier --> |
| Zotero Citation Key | <!-- from Better BibTeX --> |
| Zotero Item Key | <!-- immutable Zotero identifier --> |
| Title | <!-- full title --> |
| Authors | <!-- first author et al. --> |
| Year | <!-- publication year --> |
| Venue | <!-- conference/journal --> |
| Test Category | <!-- A / B / C / D --> |
| Research Relevance | <!-- direct / tangential / unrelated --> |
| Expected Processing Level | <!-- Level 1 only / Level 2 / Level 3 --> |
| Code Availability (expected) | <!-- available / partial / unavailable / unknown --> |
| Dataset Availability (expected) | <!-- public / restricted / private / unknown --> |

### During Processing

| Field | Value |
|---|---|
| Template Selected | <!-- Literature_Card / Paper / Survey / etc. --> |
| Processing Level Used | <!-- 1 / 2 / 3 --> |
| Knowledge Nodes Generated | <!-- list of node filenames --> |
| Manual Corrections Required | <!-- yes/no + count --> |
| Correction Details | <!-- what was wrong and how it was fixed --> |
| Token Consumption Estimate | <!-- rough estimate --> |
| Processing Errors | <!-- any crashes, failures, or hangs --> |

### After Processing 鈥?Evaluation

#### Knowledge Quality

| Criterion | Rating (1-5) | Notes |
|---|---|---|
| Accuracy | <!-- factual correctness --> | |
| Completeness | <!-- all required sections filled --> | |
| Link Quality | <!-- wikilinks are correct and useful --> | |
| No Hallucinations | <!-- no fabricated claims, numbers, or references --> | |

#### Workflow Quality

| Criterion | Pass/Fail | Notes |
|---|---|---|
| Correct processing level decision | <!-- Level 1/2/3 matched expectations --> | |
| Appropriate template selection | <!-- template matched paper type --> | |
| No agent mistakes detected | <!-- check for common failure modes --> | |
| Decision framework followed | <!-- scoring rubric was consulted --> | |

#### Reproducibility Quality

| Criterion | Pass/Fail | Notes |
|---|---|---|
| Code status accuracy | <!-- matches reality --> | |
| Dataset availability accuracy | <!-- matches reality --> | |
| Reproduction feasibility accuracy | <!-- realistic assessment --> | |
| Missing details table filled | <!-- not left blank --> | |

---

## Failure Categories

Document any issues found during the stress test using these categories.

### 1. Over-Analysis

**Definition:** The agent performed Level 2 or Level 3 processing on a paper that should have been Level 1 only.

**Example:** Generating a full Paper Note and Method nodes for a paper that was correctly classified as "Keep Reference" by the decision framework.

**Root Cause to Investigate:**
- Decision framework not consulted?
- Scoring rubric misapplied?
- Agent bypassed the decision tree?

### 2. Under-Analysis

**Definition:** The agent stopped at Level 1 for a paper that should have been Level 2 or Level 3.

**Example:** A paper with high novelty and direct relevance was marked "Keep Reference" instead of "Deep Read."

**Root Cause to Investigate:**
- Scoring rubric scores too low?
- Relevance assessment too conservative?
- Novelty undervalued?

### 3. Wrong Processing Level

**Definition:** The agent selected the wrong template or skipped required sections.

**Example:** Using Paper_Template.md for a survey paper instead of Survey_Template.md.

**Root Cause to Investigate:**
- Template selection guide unclear?
- Paper type not recognized?
- Survey vs. research article confusion?

### 4. Missing Knowledge Nodes

**Definition:** Required knowledge nodes were not created.

**Example:** A paper introduces a new method but no Method note was generated in 03_Methods/.

**Root Cause to Investigate:**
- Agent didn't recognize the method as novel?
- Template doesn't prompt for node creation?
- Decision framework doesn't mandate node creation at Level 2?

### 5. Incorrect Reproducibility Judgment

**Definition:** The reproducibility metadata is wrong.

**Example:** Code marked as "Available" when it's actually "Unavailable" or "Upon Request Only."

**Root Cause to Investigate:**
- Agent accepted vague statements ("code will be made available") as "Available"?
- Agent didn't verify the URL?
- Template doesn't require verification step?

### 6. Excessive Manual Correction

**Definition:** More than 3 corrections were needed per paper.

**Example:** The agent generated a Paper Note with wrong method description, wrong dataset name, hallucinated results, and broken wikilinks 鈥?all requiring manual fixing.

**Root Cause to Investigate:**
- Prompt/template too complex for agent?
- Agent context window exceeded?
- Insufficient source material (mineralU output incomplete)?

---

## Success Criteria

The stress test is considered **PASSED** when ALL of the following are true:

1. **No hallucinations detected** 鈥?all facts cross-checked against source paper.
2. **Correct template selection** 鈥?survey uses Survey_Template, research article uses Paper_Template.
3. **Processing level matches decision framework** 鈥?no over-analysis or under-analysis.
4. **Reproducibility metadata is accurate** 鈥?code/data status verified against actual sources.
5. **Knowledge nodes are complete** 鈥?all required sections filled, no blank placeholders remaining.
6. **Wikilinks are valid** 鈥?all [[links]] resolve to existing notes or are correctly left as placeholders for future creation.
7. **Less than 3 manual corrections per paper** 鈥?if more, the template or prompt needs revision.

If any criterion fails, document the failure, fix the root cause, and consider re-processing the same paper or a similar one.

---

## Execution Order

Recommended processing order for maximum learning:

1. **Category D first** 鈥?Tests the newest feature (reproducibility metadata). If this fails, fix it before proceeding.
2. **Category A second** 鈥?Tests template differentiation (survey vs. research article).
3. **Category B third** 鈥?Tests method extraction depth.
4. **Category C1 or C2 fourth** 鈥?Tests application/generalization or method innovation respectively

This order ensures the most fragile parts of the pipeline are tested first.

---

## Post-Stress-Test Deliverables

After completing the stress test with 4 papers (one per category):

1. **Stress Test Report** 鈥?summary of all findings, failures, and corrections.
2. **Template Revisions** 鈥?any changes to templates based on discovered gaps.
3. **Agent Prompt Refinements** 鈥?any adjustments to how agents interpret templates.
4. **Decision Framework Updates** 鈥?any refinements to the scoring rubric or decision tree.
5. **Pipeline Readiness Assessment** 鈥?go/no-go decision for batch processing.

---

## Constraints

**DO NOT:**
- Process more than 1 paper per session (allow careful review).
- Skip the Per-Paper Tracking Form.
- Assume success 鈥?document every issue, even minor ones.
- Modify the directory architecture.
- Install new tools or plugins.
- Process papers outside the four defined categories.

**DO:**
- Cross-check every fact against the source paper.
- Record manual corrections with specifics.
- Flag any ambiguity in template instructions.
- Escalate to the human researcher when the agent is uncertain.

