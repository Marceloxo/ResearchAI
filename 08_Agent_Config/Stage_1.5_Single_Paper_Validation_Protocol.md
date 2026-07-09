# Stage 1.5 — Single Paper Validation Protocol

## Purpose

Define a structured two-phase validation protocol for testing the complete ResearchAI pipeline. Each phase uses a different paper type to validate different aspects of the system.

---

## Test Papers

### Phase 1: Survey Paper

| Field | Value |
|---|---|
| Paper ID | `2024_Monteiro_LiteratureReview` |
| Title | Literature review on deep learning for the segmentation of seismic images |
| Type | Survey / Review |
| Purpose | Validate survey paper processing pipeline |

### Phase 2: Research Article

| Field | Value |
|---|---|
| Paper ID | `2020_Chai_SeismicPhasePicking` |
| Title | Seismic phase picking using deep learning |
| Type | Research Article |
| Purpose | Validate research article processing pipeline |

---

## Phase 1: Survey Paper Test

### Objective

Validate that the pipeline correctly processes a survey/review paper, which has fundamentally different structure from a primary research paper.

### Verification Checklist

| # | Check | Pass Criteria |
|---|---|---|
| 1.1 | Zotero metadata | Title, authors, year, DOI match exactly |
| 1.2 | MinerU output | `full.md` generated without errors |
| 1.3 | Processed Markdown | Cleaned markdown with proper structure |
| 1.4 | Literature Card | Created with survey-appropriate assessment |
| 1.5 | Paper Note | Created with survey-specific sections (taxonomy, coverage, gaps) |
| 1.6 | Method extraction | Key method families extracted (CNN, U-Net, Transformer, etc.) |
| 1.7 | Task extraction | Research tasks identified (fault segmentation, facies classification, etc.) |
| 1.8 | Dataset extraction | Benchmark datasets documented (F3 Netherlands, Parihaka, etc.) |
| 1.9 | Wikilink generation | All cross-links created correctly |
| 1.10 | Obsidian graph | Connected cluster with no orphans |

### Survey-Specific Validation

Unlike research articles, survey papers should produce:

- **Taxonomy extraction**: Classification of methods, tasks, datasets covered
- **Coverage analysis**: Which areas are well-covered, which are gaps
- **Future directions**: Identified research opportunities
- **No single method note**: Survey papers discuss many methods, not one

### Success Criteria

All 10 checks pass. Survey-specific validation produces ≥3 method families, ≥3 tasks, ≥3 datasets documented.

---

## Phase 2: Research Article Test

### Objective

Validate that the pipeline correctly processes a primary research article with novel methods, experiments, and results.

### Verification Checklist

| # | Check | Pass Criteria |
|---|---|---|
| 2.1 | Zotero metadata | Title, authors, year, DOI match exactly |
| 2.2 | MinerU output | `full.md` generated without errors |
| 2.3 | Processed Markdown | Cleaned markdown with proper structure |
| 2.4 | Literature Card | Created with research-article assessment |
| 2.5 | Paper Note | Created with full analysis sections |
| 2.6 | Contribution extraction | All contributions clearly identified |
| 2.7 | Network architecture extraction | Model architecture described accurately |
| 2.8 | Experiment extraction | Experimental setup and results documented |
| 2.9 | Dataset benchmark extraction | Datasets and benchmarks correctly identified |
| 2.10 | Reproduction information | Key implementation details captured |
| 2.11 | Wikilink generation | All cross-links created correctly |
| 2.12 | Obsidian graph | Connected cluster with no orphans |

### Research Article-Specific Validation

Research articles should produce:

- **Single method focus**: One primary method/architecture
- **Specific experiments**: Concrete experimental setup
- **Quantitative results**: Measurable performance metrics
- **Ablation studies**: Component-level analysis
- **Reproduction details**: Enough information to reproduce

### Success Criteria

All 12 checks pass. Research article validation produces ≥1 method note, ≥1 task note, ≥1 dataset note, ≥1 experiment interpretation.

---

## Template Selection Strategy

### Paper Type Detection

Before processing, determine the paper type:

| Indicator | Likely Type |
|---|---|
| Title contains "review", "survey", "overview" | Survey / Review |
| Title contains "method", "network", "framework" + "for" | Research Article |
| Contains taxonomy tables and coverage analysis | Survey / Review |
| Contains ablation studies and single-method comparison | Research Article |
| References 20+ papers with synthesis | Survey / Review |
| References 5-15 papers with specific experiments | Research Article |

### Template Assignment

| Paper Type | Template |
|---|---|
| Survey / Review | `Survey_Template.md` (future) |
| Research Article | `Paper_Template.md` |
| Benchmark | `Paper_Template.md` with benchmark focus |

**Important**: Survey papers and research articles require different analysis approaches. The Paper_Template is designed for research articles. A Survey_Template should be created for survey papers.

---

## Automation Strategy

### Future Pipeline

When the pipeline is automated, the agent should:

1. Detect paper type from title/content
2. Select appropriate template
3. Process with type-specific extraction rules
4. Generate different knowledge node combinations based on type

### Current Manual Process

For now, the researcher or agent manually selects the template based on paper type assessment.

---

## Execution Order

1. **Phase 1 first**: Survey paper validates the pipeline's ability to handle non-standard papers
2. **Phase 2 second**: Research article validates the standard pipeline
3. **Compare results**: Note differences in template usage, node extraction, and graph structure

---

## Post-Test Actions

After both phases:

1. Update `Zotero_Deployment_Record.md` with lessons learned
2. Update `Zotero_Integration_Design.md` if any design changes needed
3. Create `Survey_Template.md` if not already done
4. Update `Single_Paper_End_to_End_Test.md` to reflect actual experience
5. Proceed to processing 3-5 more papers through the full pipeline
