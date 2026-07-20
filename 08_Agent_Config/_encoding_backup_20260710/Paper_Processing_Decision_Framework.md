# Paper Processing Decision Framework

## Purpose

This framework defines a permanent decision mechanism for determining how deeply each paper should be processed through the ResearchAI pipeline. It prevents unnecessary token consumption and ensures deep analysis is reserved for high-value papers.

**All AI agents MUST follow this framework when processing new papers.**

---

## A. Three-Level Processing Strategy

### Level 1 â€?Literature Card (Screening)

**Purpose:** Rapid classification of incoming papers.

**Applied to:** Every paper entering the system. Non-optional.

**Pre-condition (sequential):

1. **Zotero verification** ¡ª Paper MUST be registered in Zotero. If no Zotero record: STOP and request import.
2. **Mapping verification** ¡ª Check MinerU_Zotero_Mapping.md for existing entries.
3. **Duplicate check** ¡ª Verify Paper_Index.md and 01_Papers/ directory for existing files.
4. **Processing level decision** ¡ª Apply Decision Criteria Matrix.

If any pre-condition fails (Zotero missing, duplicate detected): STOP file creation.
Input:** Processed Markdown from MinerU output.

**Output:** `Literature Card` note in `02_KnowledgeVault/01_Papers/`.

**Processing Depth:** Low (~300-500 tokens of analysis per paper).

**Required Fields:**
- Research topic relevance (direct / tangential / unrelated)
- Novelty (incremental / moderate / significant)
- Potential value to current research (high / medium / low)
- **Reproducibility Status** (code availability, data availability, checkpoint, preprocessing, environment, feasibility assessment)
- **Code verification status**: Confirmed Available / Confirmed Missing / Not Found Yet / Not Checked
- **Evidence location**: where in the paper was code availability mentioned?
- **Repository URL**: only if status is Confirmed Available
Reading decision:
  - **Ignore** â€?no further processing
  - **Keep Reference** â€?Literature Card only, revisit if research direction shifts
  - **Deep Read** â€?proceed to Level 2


**Critical Rule**: Agents must NOT mark code as "Unavailable" or "Missing" unless full-text verification confirms absence. "Not Found Yet" is the default when code is not explicitly mentioned.
**Decision Criteria Matrix:**

| Relevance | Novelty | Value | Decision |
|---|---|---|---|
| Unrelated | Any | Any | Ignore |
| Tangential | Incremental | Low | Ignore |
| Tangential | Moderate | Medium | Keep Reference |
| Direct | Incremental | Medium | Keep Reference |
| Direct | Moderate | High | Deep Read |
| Direct | Significant | High | Deep Read |

**Token Budget:** ~300 tokens/paper. Can screen 100 papers for the cost of 2 deep analyses.

---

### Level 2 â€?Paper Note (Deep Analysis)

**Purpose:** Full understanding of selected papers. Extract methods, tasks, datasets, and insights.

**Applied to:** Papers marked "Deep Read" at Level 1.

**Input:** Processed Markdown from Level 1 screening.

**Output:**
- `Paper Note` in `02_KnowledgeVault/01_Papers/`
- `Method` notes in `03_Methods/` (if novel or relevant methods are introduced)
- `Task` notes in `04_Tasks/` (if new task definitions emerge)
- `Dataset` notes in `05_Datasets/` (if new datasets are documented)
- `Topic` updates in `02_Topics/` (if existing topics need expansion)

**Processing Depth:** Medium (~1,500-2,000 tokens of analysis per paper).

**Required Fields:**
- Problem definition (input/output/formulation)
- Method overview (architecture, key modules)
- Dataset description (scale, format, provenance)
- Experimental setup (baselines, metrics)
- Main contributions (quantified where possible)
- Limitations (author-admitted + agent-identified)
- Transferable ideas (what can be applied to our research)

**Differentiation by Paper Type:**

| Paper Type | Focus |
|---|---|
| Research Article | Method, experiment, results, ablation |
| Survey / Review | Taxonomy, coverage, future directions |
| Benchmark | Evaluation methodology, baseline comparisons |
| Technical Report | Implementation details, engineering insights |

**Token Budget:** ~1,500 tokens/paper.

**Reproducibility Analysis at Level 2:**
- Expand Level 1 code status into full reproducibility feasibility assessment.
- Verify repository accessibility and analyze reproduction difficulty.
- May analyze checkpoints, preprocessing, hyperparameters, environment, and hardware requirements.
- Distinguish between "code exists" and "paper is reproducible."

---

### Level 3 â€?Argument Mining Paper Logic (Core Analysis)

**Purpose:** Deep structural deconstruction of core papers for writing assistance and research gap discovery.

**Applied to:** Only papers that meet ALL trigger conditions below.

**Input:** Paper Note from Level 2.

**Output:**
- `Paper Logic` note in `02_KnowledgeVault/09_Paper_Logic/` using Argument Mining template
- Cross-linked Method, Task, Dataset, Experiment notes
- Writing Strategy Analysis for manuscript planning
- Paper-to-Own-Research Bridge with action items

**Processing Depth:** High (~3,000-5,000 tokens of analysis per paper).

**Trigger Conditions (ALL must be met):**

1. **Directly influences own research direction** â€?the paper's findings would change how we approach our current work.
2. **Contains novel architecture or design** â€?introduces a genuinely new component, module, or paradigm (not just application of existing method to new data).
3. **SOTA benchmark paper** â€?establishes a new state-of-the-art on a benchmark relevant to our tasks.
4. **Highly cited foundational paper** â€?a paper that many others cite (check citation count in Zotero/Web of Science).

**Additional discretionary triggers (agent may recommend Level 3 for these):**

- The paper solves a problem we are actively trying to solve.
- The paper's methodology could be directly adapted to seismic image segmentation.
- The paper contains a particularly well-structured argument worth studying for writing purposes.

**Required Sections (per Paper_Logic_Template.md):**
- Evidence Mapping table (Claim â†?Evidence â†?Experiment â†?Metric â†?Result â†?Support)
- Method Justification for each core module
- Hidden Limitation Analysis (reviewer perspective)
- Writing Strategy Analysis (intro, method presentation, experiment design)
- Transferable Research Ideas with feasibility assessment
- Paper-to-Own-Research Bridge with specific action items

**Token Budget:** ~3,000-5,000 tokens/paper. Reserve for the top 10-20% of papers.

**Reproducibility Limitations at Level 3:**
- Analyze whether the paper's experimental claims are reproducible.
- Document reproducibility risks and limitations.
- Note claims that cannot be independently verified.

---

## B. Decision Tree

```
New paper enters Zotero
    â”?    â–?[Level 1] Read Processed Markdown
    â”?    â”œâ”€â”€ Is the paper unrelated to seismic AI / deep learning / computer vision?
    â”?  â””â”€â”€ YES â†?Decision: IGNORE
    â”?             Action: Literature Card with "Ignore"
    â”?             Skip Levels 2 and 3.
    â”?    â”œâ”€â”€ Is the paper tangential (e.g., medical imaging, remote sensing)?
    â”?  â”œâ”€â”€ YES, and novelty is incremental?
    â”?  â”?  â””â”€â”€ Decision: KEEP REFERENCE
    â”?  â”?    Action: Literature Card with "Keep Reference"
    â”?  â”?    Skip Levels 2 and 3.
    â”?  â”?    â”?  â””â”€â”€ YES, and novelty is moderate or higher?
    â”?      â””â”€â”€ Decision: DEEP READ
    â”?        Action: Proceed to Level 2
    â”?    â””â”€â”€ Is the paper directly relevant (seismic AI / CV / deep learning)?
        â”?        â”œâ”€â”€ Is the methodological novelty LOW?
        â”?  â””â”€â”€ (Application paper, no new architecture)
        â”?      â”œâ”€â”€ Is it a SOTA benchmark?
        â”?      â”?  â””â”€â”€ YES â†?DEEP READ (proceed to Level 2)
        â”?      â”?  â””â”€â”€ NO â†?KEEP REFERENCE
        â”?      â”?        â”?      â””â”€â”€ Does it use a dataset we plan to use?
        â”?          â””â”€â”€ YES â†?DEEP READ
        â”?          â””â”€â”€ NO â†?KEEP REFERENCE
        â”?        â”œâ”€â”€ Is the methodological novelty MODERATE?
        â”?  â””â”€â”€ (Modified existing method, new combination)
        â”?      â”œâ”€â”€ Does it solve a problem we are actively working on?
        â”?      â”?  â””â”€â”€ YES â†?DEEP READ
        â”?      â”?  â””â”€â”€ NO â†?KEEP REFERENCE
        â”?      â”?        â”?      â””â”€â”€ Can the approach transfer to seismic image segmentation?
        â”?          â””â”€â”€ YES â†?DEEP READ
        â”?          â””â”€â”€ NO â†?KEEP REFERENCE
        â”?        â””â”€â”€ Is the methodological novelty HIGH?
            â””â”€â”€ (New architecture, new paradigm, significant innovation)
                â”œâ”€â”€ DEEP READ (proceed to Level 2)
                â”?                â””â”€â”€ After Level 2 analysis:
                    â”œâ”€â”€ Does it meet ALL Level 3 trigger conditions?
                    â”?  â””â”€â”€ YES â†?ARGUMENT MINING (proceed to Level 3)
                    â”?  â””â”€â”€ NO â†?Level 2 only
                    â”?                    â””â”€â”€ Should the agent RECOMMEND Level 3 to the human?
                        â””â”€â”€ YES â†?Flag for human review
                        â””â”€â”€ NO â†?Level 2 only
```

---

## C. Scoring Rubric (Optional Quantitative Aid)

For agents that need a more systematic approach, use this scoring rubric. Sum the scores for each criterion:

| Criterion | Score 0 | Score 1 | Score 2 | Score 3 |
|---|---|---|---|---|
| **Relevance to Current Research** | Unrelated | Tangential | Direct | Core to current work |
| **Methodological Novelty** | Application only | Minor modification | New combination | New architecture/paradigm |
| **Experimental Importance** | No experiments | Weak baseline | Standard baselines | Comprehensive + ablation |
| **Citation Influence** | < 10 citations | 10-50 citations | 50-200 citations | > 200 citations |
| **Reproducibility Value** | No code/data | Code only | Code + data | Reproducible SOTA |

**Scoring Interpretation:**

| Total Score | Recommendation |
|---|---|
| 0-3 | **Ignore** â€?Literature Card only, mark Ignore |
| 4-7 | **Keep Reference** â€?Literature Card only, mark Keep Reference |
| 8-11 | **Deep Read** â€?Proceed to Level 2 |
| 12-15 | **Deep Read + Recommend Level 3** â€?Proceed to Level 2, flag for potential Argument Mining |

**Note:** The scoring rubric is a decision aid, not a replacement for agent judgment. Human review is always recommended before committing to Level 3 processing.

---

## D. Enforcement Rules
### Duplicate Prevention Gate (Rule 0)

Before any paper file is created, the agent MUST verify no duplicate exists.

Checks (in order):
1. Search MinerU_Zotero_Mapping.md for matching Zotero Item Key.
2. Search Paper_Index.md for matching Paper ID or filename.
3. Search 01_Papers/ directory for matching {author}{year}_* filename pattern.

If any match found: STOP creation. Update existing file if content is incomplete. Log duplicate in Batch_Processing_Log.md.

### For AI Agents

1. **Zotero-first: Every paper MUST be registered in Zotero before processing.** If no Zotero record exists, STOP and request import. No exceptions.
2. **Every paper MUST go through Level 1.** No exceptions.
3. **Agents MUST NOT auto-promote papers to Level 2 or Level 3.** The decision must follow this framework.
4. **Agents MUST NOT generate Paper Logic notes without explicit trigger conditions being met.**
5. **When in doubt, escalate to the human researcher.** Mark the paper with a "recommend human review" flag.
6. **Agents MUST record the decision rationale** in the Literature Card (why Ignore / Keep Reference / Deep Read).

### For Human Researchers

1. The human can override any agent decision.
2. The human can manually promote any paper to a deeper level.
3. The human should periodically review "Keep Reference" papers as research direction evolves.

---

## E. Token Cost Summary

| Level | Papers | Tokens/Paper | Total for 100 Papers |
|---|---|---|---|
| Level 1 only (Ignore/Keep Ref) | ~70 papers | ~300 | ~21,000 |
| Level 2 (Deep Read) | ~25 papers | ~1,500 | ~37,500 |
| Level 3 (Argument Mining) | ~5 papers | ~4,000 | ~20,000 |
| **Total estimated** | **100 papers** | | **~78,500 tokens** |

Without this framework, naive deep analysis of all 100 papers would cost ~400,000+ tokens. This framework saves approximately **80% in token cost** while concentrating depth where it matters most.

---

## F. Future Evolution

As the knowledge base grows, this framework may evolve:

- **Automated scoring:** Zotero citation counts and venue impact factors can auto-populate parts of the scoring rubric.
- **Cluster-aware filtering:** As topic clusters grow, papers may be evaluated relative to existing cluster density rather than absolute novelty.
- **Human feedback loop:** The human's overrides of agent decisions should be tracked to refine the decision criteria over time.















