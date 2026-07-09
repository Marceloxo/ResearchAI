# Paper Processing Decision Framework

## Purpose

This framework defines a permanent decision mechanism for determining how deeply each paper should be processed through the ResearchAI pipeline. It prevents unnecessary token consumption and ensures deep analysis is reserved for high-value papers.

**All AI agents MUST follow this framework when processing new papers.**

---

## A. Three-Level Processing Strategy

### Level 1 鈥?Literature Card (Screening)

**Purpose:** Rapid classification of incoming papers.

**Applied to:** Every paper entering the system. Non-optional.

**Input:** Processed Markdown from MinerU output.

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
  - **Ignore** 鈥?no further processing
  - **Keep Reference** 鈥?Literature Card only, revisit if research direction shifts
  - **Deep Read** 鈥?proceed to Level 2


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

### Level 2 鈥?Paper Note (Deep Analysis)

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

### Level 3 鈥?Argument Mining Paper Logic (Core Analysis)

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

1. **Directly influences own research direction** 鈥?the paper's findings would change how we approach our current work.
2. **Contains novel architecture or design** 鈥?introduces a genuinely new component, module, or paradigm (not just application of existing method to new data).
3. **SOTA benchmark paper** 鈥?establishes a new state-of-the-art on a benchmark relevant to our tasks.
4. **Highly cited foundational paper** 鈥?a paper that many others cite (check citation count in Zotero/Web of Science).

**Additional discretionary triggers (agent may recommend Level 3 for these):**

- The paper solves a problem we are actively trying to solve.
- The paper's methodology could be directly adapted to seismic image segmentation.
- The paper contains a particularly well-structured argument worth studying for writing purposes.

**Required Sections (per Paper_Logic_Template.md):**
- Evidence Mapping table (Claim 鈫?Evidence 鈫?Experiment 鈫?Metric 鈫?Result 鈫?Support)
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
    鈹?    鈻?[Level 1] Read Processed Markdown
    鈹?    鈹溾攢鈹€ Is the paper unrelated to seismic AI / deep learning / computer vision?
    鈹?  鈹斺攢鈹€ YES 鈫?Decision: IGNORE
    鈹?             Action: Literature Card with "Ignore"
    鈹?             Skip Levels 2 and 3.
    鈹?    鈹溾攢鈹€ Is the paper tangential (e.g., medical imaging, remote sensing)?
    鈹?  鈹溾攢鈹€ YES, and novelty is incremental?
    鈹?  鈹?  鈹斺攢鈹€ Decision: KEEP REFERENCE
    鈹?  鈹?    Action: Literature Card with "Keep Reference"
    鈹?  鈹?    Skip Levels 2 and 3.
    鈹?  鈹?    鈹?  鈹斺攢鈹€ YES, and novelty is moderate or higher?
    鈹?      鈹斺攢鈹€ Decision: DEEP READ
    鈹?        Action: Proceed to Level 2
    鈹?    鈹斺攢鈹€ Is the paper directly relevant (seismic AI / CV / deep learning)?
        鈹?        鈹溾攢鈹€ Is the methodological novelty LOW?
        鈹?  鈹斺攢鈹€ (Application paper, no new architecture)
        鈹?      鈹溾攢鈹€ Is it a SOTA benchmark?
        鈹?      鈹?  鈹斺攢鈹€ YES 鈫?DEEP READ (proceed to Level 2)
        鈹?      鈹?  鈹斺攢鈹€ NO 鈫?KEEP REFERENCE
        鈹?      鈹?        鈹?      鈹斺攢鈹€ Does it use a dataset we plan to use?
        鈹?          鈹斺攢鈹€ YES 鈫?DEEP READ
        鈹?          鈹斺攢鈹€ NO 鈫?KEEP REFERENCE
        鈹?        鈹溾攢鈹€ Is the methodological novelty MODERATE?
        鈹?  鈹斺攢鈹€ (Modified existing method, new combination)
        鈹?      鈹溾攢鈹€ Does it solve a problem we are actively working on?
        鈹?      鈹?  鈹斺攢鈹€ YES 鈫?DEEP READ
        鈹?      鈹?  鈹斺攢鈹€ NO 鈫?KEEP REFERENCE
        鈹?      鈹?        鈹?      鈹斺攢鈹€ Can the approach transfer to seismic image segmentation?
        鈹?          鈹斺攢鈹€ YES 鈫?DEEP READ
        鈹?          鈹斺攢鈹€ NO 鈫?KEEP REFERENCE
        鈹?        鈹斺攢鈹€ Is the methodological novelty HIGH?
            鈹斺攢鈹€ (New architecture, new paradigm, significant innovation)
                鈹溾攢鈹€ DEEP READ (proceed to Level 2)
                鈹?                鈹斺攢鈹€ After Level 2 analysis:
                    鈹溾攢鈹€ Does it meet ALL Level 3 trigger conditions?
                    鈹?  鈹斺攢鈹€ YES 鈫?ARGUMENT MINING (proceed to Level 3)
                    鈹?  鈹斺攢鈹€ NO 鈫?Level 2 only
                    鈹?                    鈹斺攢鈹€ Should the agent RECOMMEND Level 3 to the human?
                        鈹斺攢鈹€ YES 鈫?Flag for human review
                        鈹斺攢鈹€ NO 鈫?Level 2 only
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
| 0-3 | **Ignore** 鈥?Literature Card only, mark Ignore |
| 4-7 | **Keep Reference** 鈥?Literature Card only, mark Keep Reference |
| 8-11 | **Deep Read** 鈥?Proceed to Level 2 |
| 12-15 | **Deep Read + Recommend Level 3** 鈥?Proceed to Level 2, flag for potential Argument Mining |

**Note:** The scoring rubric is a decision aid, not a replacement for agent judgment. Human review is always recommended before committing to Level 3 processing.

---

## D. Enforcement Rules

### For AI Agents

1. **Every paper MUST go through Level 1.** No exceptions.
2. **Agents MUST NOT auto-promote papers to Level 2 or Level 3.** The decision must follow this framework.
3. **Agents MUST NOT generate Paper Logic notes without explicit trigger conditions being met.**
4. **When in doubt, escalate to the human researcher.** Mark the paper with a "recommend human review" flag.
5. **Agents MUST record the decision rationale** in the Literature Card (why Ignore / Keep Reference / Deep Read).

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









