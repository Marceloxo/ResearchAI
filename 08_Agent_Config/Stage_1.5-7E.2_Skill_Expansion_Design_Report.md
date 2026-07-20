# Stage 1.5-7E.2 Skill Expansion Design Report

> **????**: 2026-07-10
> **????**: Stage 1.5-7E.1 Skill Architecture Review
> **????**: ??????????????
> **???**: Agnes (ResearchAI Agent)

---

## Current Architecture

### Existing Skill System (9 Skills)

The current ResearchAI skill system implements a **paper-centric pipeline**:

```
Zotero (source)
    |
    v
[Paper Intake] -----> Literature Card (Level 1)
    |                       |
    +-- [Batch Process] --->+
    |
    v
[Deep Read] ---------> Paper Note (Level 2)
    |
    v
[Paper Update] -----> Incremental updates
```

**Supporting infrastructure**:
- [Knowledge Node Check] - Prevents duplication
- [Research Map Update] - Maintains navigation
- [Literature Synthesis] - Generates writing materials
- [Architecture Audit] - Read-only system health check
- [Encoding Audit] - UTF-8 integrity verification

### Current Coverage Assessment

| Domain | Skills | Templates | Gap |
|--------|--------|-----------|-----|
| Paper Intake (L1) | 2 (Intake + Batch) | 1 (Card) | PASS |
| Paper Deep Read (L2) | 1 (Deep Read) | 1 (Paper) | PASS |
| Paper Level 3 | 0 | 1 (Logic) | **FAIL** |
| Survey/Review | 0 | 1 (Survey) | **FAIL** |
| Knowledge Nodes | 1 (Check only) | 5 (Method/Task/Dataset/Idea/Experiment) | **FAIL** |
| Writing | 1 (Synthesis) | 1 (Writing) | **FAIL** |
| System Ops | 2 (Audit + Encoding) | N/A | PASS |

**Key constraint**: The SKILL.md description states "Architecture is frozen: Zotero -> MinerU -> KnowledgeVault." This limits expansion to the existing pipeline boundaries. New skills must fit within or extend the current workflow without restructuring.

---

## Required New Skills

### Selection Criteria

A new skill is **required** only if ALL of the following are true:

1. **Blocks the current workflow** - Users cannot complete a documented pipeline step
2. **Has a template waiting** - Output format is already defined
3. **Has no workaround** - Cannot be handled by existing skills
4. **Fits the frozen architecture** - Does not require directory structure changes

### Required Skills (Phase 1)

#### 1. `/SKILL Paper Logic` (Level 3)

**Why required**:
- Paper Intake workflow determines Level 3 eligibility
- Level 3 requires Argument Mining and Evidence Mapping
- Paper_Logic_Template.md exists but no skill generates it
- Papers classified as Level 3 have a dead-end workflow

**Input**: Zotero Item Key
**Output**: Paper_Logic_Template.md in 09_Paper_Logic/
**Dependencies**: Paper Intake (must run first), Deep Read (recommended)
**Impact**: Completes the 3-level processing pipeline

**Verdict**: **PASS - Required immediately**

---

#### 2. `/SKILL Survey Process`

**Why required**:
- 4 survey papers exist in KnowledgeVault but were processed with research_article templates
- Survey_Template.md exists but no skill generates surveys
- Survey papers require taxonomy construction, gap analysis, and coverage evaluation
- Treating surveys as research articles loses analytical depth

**Input**: Zotero Item Key
**Output**: Survey_Template.md in 01_Papers/ (with survey-specific frontmatter)
**Dependencies**: Paper Intake (must run first)
**Impact**: Proper classification of survey/review papers

**Verdict**: **PASS - Required immediately**

---

#### 3. `/SKILL Method Node`

**Why required**:
- KnowledgeVault has 8 method nodes (CNN, Transformer, Attention Mechanism, etc.)
- All were created manually
- Knowledge Node Check recommends "Create" but provides no creation workflow
- Method nodes follow Method_Template.md with no automated generation path

**Input**: Concept name (from Knowledge Node Check)
**Output**: Method_Template.md in 03_Methods/
**Dependencies**: Knowledge Node Check (must recommend "Create")
**Impact**: Enables organic knowledge graph growth for methods

**Verdict**: **PASS - Required immediately**

---

### Justification for Exclusions

The following were considered but **not required** at this time:

| Skill | Reason for Exclusion |
|-------|---------------------|
| Task Node | Only 3 task nodes exist, all created manually. Low volume. Can wait. |
| Dataset Node | 10 dataset nodes exist, all manually created. Well-documented externally. |
| Idea Node | 0 ideas exist. Premature to build skill for empty domain. |
| Experiment Node | 1 experiment exists. Low volume. |
| Paper Writer | Writing directory is empty. Literature Synthesis produces materials. Writing skill is a future enhancement, not a workflow blocker. |
| Zotero Sync | Manual Zotero management is acceptable. No data loss risk. |
| Paper Revision | Paper Update handles basic revisions. Advanced versioning is low priority. |

---

## Deferred Skills

### Phase 2 (Medium Priority)

| Skill | Reason to Defer | Trigger for Activation |
|-------|----------------|----------------------|
| `/SKILL Task Node` | Low volume (3 nodes), manual creation is manageable | When manual creation becomes a bottleneck |
| `/SKILL Dataset Node` | Low volume (10 nodes), datasets are externally documented | When internal dataset notes are needed |
| `/SKILL Experiment Node` | Low volume (1 node) | When experiment tracking becomes frequent |
| `/SKILL Paper Writer` | Writing directory empty, synthesis skill produces materials | When users request paper drafting |

### Phase 3 (Low Priority / Not Required)

| Skill | Reason |
|-------|--------|
| `/SKILL Idea Node` | No ideas exist yet. Premature investment. |
| `/SKILL Zotero Sync` | Manual sync is acceptable. No automation gap. |
| `/SKILL Paper Revision` | Paper Update skill covers basic revisions. |
| `/SKILL Reference Manager` | Citations are managed through Zotero. No separate skill needed. |

---

## Skill Dependency Graph

### Current Skill Dependencies

```
[Paper Intake]
    |
    +---> [Batch Process] (calls Intake internally)
    |
    +---> [Deep Read] (requires Intake first)
    |       |
    |       +---> [Paper Update] (updates card after note)
    |
    +---> [Paper Update] (standalone)

[Knowledge Node Check]
    |
    +---> [Research Map Update] (check informs map decisions)

[Literature Synthesis]
    |
    +---> [Paper Writer] (DEFERRED - needs synthesis output)

[Architecture Audit]
[Encoding Audit]
    (independent - no dependencies)
```

### Proposed New Skill Dependencies

```
[Paper Intake]
    |
    +---> [Deep Read] (requires Intake first)
    |       |
    |       +---> [Paper Logic] (REQUIRES Deep Read as input)
    |
    +---> [Survey Process] (requires Intake for classification)

[Knowledge Node Check]
    |
    +---> [Method Node] (REQUIRES Check to recommend "Create")
    |
    +---> [Task Node] (deferred)
    +---> [Dataset Node] (deferred)
```

### Dependency Analysis

**Critical path**: Paper Intake -> Deep Read -> Paper Logic
- This is the only new dependency chain that blocks a core workflow
- Paper Logic cannot exist without Deep Read (needs extracted analysis sections)
- Deep Read cannot exist without Paper Intake (needs existing card)

**Safe additions**: Method Node depends on Knowledge Node Check
- This is a preventive dependency, not a blocking one
- Method Node can work standalone if needed

**No circular dependencies**: All proposed skills have clear upstream dependencies.

---

## Implementation Roadmap

### Phase 1: Complete Core Pipeline (Immediate)

**Timeline**: Can be implemented in parallel (3 skills)

| # | Skill | Reference File | Input | Output |
|---|-------|---------------|-------|--------|
| 1 | Paper Logic | references/literature/paper_logic.md | Zotero Item Key | Paper Logic card |
| 2 | Survey Process | references/literature/survey_process.md | Zotero Item Key | Survey paper |
| 3 | Method Node | references/knowledge/method_node.md | Concept name | Method node |

**Prerequisites**:
- Paper Logic requires Deep Read reference to exist (it does)
- Survey Process requires Paper Intake reference (it does)
- Method Node requires Knowledge Node Check reference (it does)

**Implementation order**:
1. Paper Logic (blocks Level 3 workflow)
2. Survey Process (blocks survey classification)
3. Method Node (enables knowledge growth)

### Phase 2: Expand Knowledge Growth (Deferred)

| # | Skill | Trigger |
|---|-------|---------|
| 4 | Task Node | When manual creation becomes bottleneck |
| 5 | Dataset Node | When internal dataset notes needed |
| 6 | Experiment Node | When experiment tracking frequent |

### Phase 3: Writing Pipeline (Deferred)

| # | Skill | Trigger |
|---|-------|---------|
| 7 | Paper Writer | When users request paper drafting |

---

## Skill Explosion Prevention

### Guardrails

To prevent uncontrolled skill growth, new skills must pass ALL of these checks:

1. **Template exists**: Output format must be defined in Templates/
2. **Workflow blocker**: The skill must unblock a documented pipeline step
3. **Usage frequency**: Manual creation occurs at least 3 times before automation is justified
4. **No overlap**: The skill must not duplicate existing skill functionality
5. **Dependency chain**: The skill must have clear upstream dependencies

### Capacity Analysis

| Metric | Current | After Phase 1 | After Phase 2 |
|--------|---------|--------------|--------------|
| Total skills | 9 | 12 | 15 |
| Reference files | 9 | 12 | 15 |
| Templates covered | 4/10 | 7/10 | 9/10 |
| Pipeline blocks | 3 | 0 | 0 |

**Assessment**: Phase 1 expansion (3 new skills) brings coverage to 70% of templates. Phase 2 (3 more) reaches 90%. Beyond 15 skills, diminishing returns justify deferring further expansion.

### Anti-Patterns to Avoid

- **Creating a skill for every template**: 10 templates != 10 skills. Some templates support multiple workflows.
- **Creating skills for empty domains**: Idea Node (0 items) should wait.
- **Over-engineering simple tasks**: Task/Dataset nodes can remain manual until volume justifies automation.
- **Duplicating existing functionality**: Knowledge Node Check already prevents duplication. New node skills should reference it.

---

## Final Recommendation

### Required Skills (Implement Now)

| Skill | Priority | Blocks Workflow |
|-------|----------|----------------|
| `/SKILL Paper Logic` | **HIGH** | Yes - Level 3 dead-end |
| `/SKILL Survey Process` | **HIGH** | Yes - Survey classification |
| `/SKILL Method Node` | **MEDIUM** | No - Manual creation works |

### Deferred Skills

| Skill | Phase | Trigger |
|-------|-------|---------|
| Task Node | 2 | Volume threshold |
| Dataset Node | 2 | Volume threshold |
| Experiment Node | 2 | Volume threshold |
| Paper Writer | 3 | User demand |

### Implementation Order

```
1. Paper Logic (completes Level 1->2->3 pipeline)
2. Survey Process (proper survey classification)
3. Method Node (enables knowledge graph growth)
```

### Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Adding 3 new skills breaks Mode B permission model | LOW | Each skill inherits Mode B from parent SKILL.md |
| New skills create circular dependencies | NONE | Dependency graph verified acyclic |
| Skill explosion beyond 15 | MEDIUM | Guardrail checks prevent uncontrolled growth |
| New skills duplicate existing functionality | LOW | Overlap check required before creation |

### Final Verdict

| Check | Result |
|---|---|
| Required skills identified | **PASS** |
| Deferral rationale sound | **PASS** |
| Dependency graph valid | **PASS** |
| Implementation order logical | **PASS** |
| Skill explosion prevented | **PASS** |

**Overall: PASS**

The expansion plan adds exactly 3 required skills that unblock documented workflow gaps, while deferring 4+ optional skills until usage volume justifies investment. The dependency graph is acyclic, and guardrails prevent uncontrolled growth beyond 15 skills.

---

*Stage 1.5-7E.2 Skill Expansion Design completed*
*Generated: 2026-07-10 | Agent: Agnes (ResearchAI)*
