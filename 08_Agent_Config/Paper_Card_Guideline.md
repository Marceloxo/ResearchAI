# Paper Card vs Paper Note — Role Clarification

## Purpose

Prevent duplicated analysis and ensure each note type serves a distinct purpose in the knowledge pipeline.

## Literature Card (Screening Note)

**Location:** `02_KnowledgeVault/01_Papers/`

**Purpose:** Rapid classification to decide whether a paper deserves deep analysis.

**Characteristics:**
- Short (typically 1-2 pages of markdown)
- Focused on decision support: Deep Read / Keep Reference / Ignore
- Contains structured metadata + brief assessment
- Does NOT reproduce paper content

**Required Sections:**
1. Basic Information (title, authors, year, venue, task, method, dataset)
2. Research Problem (1-2 sentences)
3. Main Contribution (1 sentence)
4. Method Overview (1-3 sentences)
5. Dataset and Evaluation (brief)
6. Why This Paper Matters (1-2 sentences, personal relevance)
7. Limitations (brief)
8. **Reproducibility Status** (graded: Confirmed Available / Missing / Not Found Yet / Not Checked)
9. My Decision (Deep Read / Keep Reference / Ignore) with reason
10. Related Knowledge (wikilinks)

**Token Budget:** ~300 tokens of analysis per paper.

**When to Create:**
- For EVERY paper entering the system (non-optional, Level 1).
- Even for papers that will be "Ignored."

**When NOT to Create:**
- Never create a Literature Card for a paper already in the KnowledgeVault.

## Paper Note (Deep Analysis Note)

**Location:** `02_KnowledgeVault/01_Papers/`

**Purpose:** Detailed understanding of a paper that passed Level 1 screening.

**Characteristics:**
- Long (typically 5-15 pages of markdown)
- Focused on comprehension, not decision-making
- Contains structured analysis of method, experiment, results, limitations
- Includes personal insight and transferable ideas

**Required Sections:**
1. Paper Type (research_article / survey / review / benchmark)
2. One Sentence Summary
3. Research Background
4. Problem Definition (input/output)
5. Motivation
6. Main Contributions
7. Method (overall framework + key modules + math formulation)
8. Dataset
9. Experimental Setup
10. Results
11. Ablation Study
12. Limitation
13. **My Analysis** (transferable ideas + potential improvements)
14. **Reproducibility Analysis** (official implementation, missing components, feasibility)
15. Related Notes (wikilinks)

**Token Budget:** ~1,500 tokens of analysis per paper.

**When to Create:**
- Only for papers marked "Deep Read" in their Literature Card.
- Each paper gets ONE Paper Note (not multiple versions).

**When NOT to Create:**
- Never create a Paper Note for a paper marked "Ignore" or "Keep Reference."
- Never create a Paper Note that duplicates the Literature Card — the Paper Note assumes the Card already exists.

## Paper Logic (Argument Mining Note)

**Location:** `02_KnowledgeVault/09_Paper_Logic/`

**Purpose:** Deep structural deconstruction of core papers for writing assistance and research gap discovery.

**Characteristics:**
- Very long (typically 10-20 pages)
- Focused on argument structure, not paper content summary
- Maps claims to evidence, analyzes writing strategy, extracts transferable ideas
- Used for manuscript planning

**When to Create:**
- Only for papers that meet ALL Level 3 trigger conditions (see Paper_Processing_Decision_Framework.md).
- Maximum ~10-20% of all processed papers.

## Anti-Duplication Rules

1. **One Literature Card per paper.** Never create a second card for the same paper.
2. **Paper Note builds on Literature Card.** The Card decides "deep read." The Note explains "why."
3. **Paper Logic is meta-analysis.** It analyzes HOW the paper argues, not WHAT the paper says.
4. **If a paper is marked "Keep Reference" in the Literature Card, stop.** Do not create a Paper Note.
5. **Survey papers use Survey_Template.md, not Paper_Template.md.** Do not apply research-article analysis to a survey.

## Decision Flow

```
New paper arrives
    │
    ▼
Create Literature Card (Level 1)
    │
    ├── Decision: Ignore
    │   └── STOP. No further notes.
    │
    ├── Decision: Keep Reference
    │   └── STOP. No Paper Note. Card is the only record.
    │
    └── Decision: Deep Read
        │
        ▼
        Create Paper Note (Level 2)
        │
        ├── Is this a survey/review paper?
        │   └── YES → Use Survey_Template.md
        │
        └── Is this a research article meeting ALL Level 3 triggers?
            ├── YES → Create Paper Logic (Level 3)
            └── NO → STOP. Paper Note is the deepest analysis.
```

## Summary Table

| Note Type | Depth | When | Token Cost | Output |
|---|---|---|---|---|
| Literature Card | Shallow | Every paper | ~300 | Decision: Read / Keep / Ignore |
| Paper Note | Deep | Papers marked "Deep Read" | ~1,500 | Understanding + transferable ideas |
| Survey Note | Deep | Survey/review papers only | ~1,500 | Taxonomy + coverage + future directions |
| Paper Logic | Deepest | Core papers only (trigger conditions met) | ~4,000 | Argument mining + writing strategy |
