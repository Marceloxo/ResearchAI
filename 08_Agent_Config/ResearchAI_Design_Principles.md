# ResearchAI Design Principles

## Purpose

Long-term design principles that govern the ResearchAI system architecture. These principles are **permanent** — tools change, but the structure should endure.

---

## Principle 1: Raw / Processed / Knowledge Separation

ResearchAI maintains three distinct data layers with strict boundaries:

| Layer | Purpose | Location | Audience |
|---|---|---|---|
| **Raw** | Original parsing output, untouched | `01_Literature/02_MinerU_Output/` | MinerU output |
| **Processed** | Cleaned text for AI reading | `01_Literature/03_Processed_Markdown/` | AI agents |
| **Knowledge** | Structured understanding | `02_KnowledgeVault/` | Humans + AI |

**Rule**: Raw data never enters the KnowledgeVault. Only extracted knowledge does.
**Rule**: Processed markdown is transient — it serves analysis, not archival.

---

## Principle 2: Zotero Owns Bibliographic Truth

Zotero is the **single source of truth** for all bibliographic metadata:

- title, authors, year, DOI, journal, volume, issue, pages
- Citation keys and BibTeX entries
- PDF file organization

**Rule**: ResearchAI never stores bibliographic metadata as the source of truth.
**Rule**: If Zotero and ResearchAI disagree on metadata, Zotero wins.
**Rule**: AI agents must never fabricate citation details — always source from Zotero or verified KnowledgeVault notes.

---

## Principle 3: ResearchAI Owns Interpreted Knowledge

ResearchAI's value is in **interpretation**, not reproduction:

- Reading notes and personal analysis
- Extracted methods, tasks, datasets
- Research ideas and hypotheses
- Experiment results and interpretations
- Writing logic and manuscript structure

**Rule**: KnowledgeVault notes should contain the researcher's (or AI's) understanding, not a copy of the paper text.
**Rule**: Each note should answer "what does this mean for my research?"

---

## Principle 4: Paper ID and Citation Key Are Independent Identifiers

Each paper has **three independent identifiers** serving different purposes:

| Identifier | System | Format | Example | Purpose |
|---|---|---|---|---|
| **Paper ID** | ResearchAI local | `YYYY_FirstAuthor_ShortTitle` | `2023_Monteiro_DeepLearningSeismicSegmentation` | File organization, human readability |
| **Zotero Item Key** | Zotero internal | 6-char alphanumeric | `ABCDE123` | Immutable Zotero reference |
| **Citation Key** | Better BibTeX | `authorYEARkeyword` | `monteiro2023deeplearning` | Academic citation formatting |

**Rule**: Paper ID is for ResearchAI file organization.
**Rule**: Citation Key is for BibTeX/manuscript citations.
**Rule**: They are related but **not required to match**. A paper can have a Paper ID that differs from its Citation Key.
**Rule**: The Literature Index maintains the mapping between all three.

---

## Principle 5: KnowledgeVault Stores Understanding, Not Raw Extraction

The KnowledgeVault is a **thinking space**, not a **storage space**.

- A Literature Card is a quick assessment, not a paper summary.
- A Paper Note is an analysis with personal insight, not a transcription.
- A Method note describes what the method *means*, not just what it *is*.
- An Experiment note records what was *learned*, not just what was *measured*.

**Rule**: If a note could be replaced by a PDF, it doesn't belong in the KnowledgeVault.
**Rule**: Every note should contain at least one original insight or interpretation.

---

## Principle 6: AI Must Never Fabricate Citations

Citation integrity is the highest priority for research credibility.

**Rule**: All citations must come from Zotero or verified KnowledgeVault notes.
**Rule**: If a citation detail is uncertain, mark it as `[uncertain: <detail>]` — never guess.
**Rule**: If a paper is not in Zotero and not in KnowledgeVault, use a placeholder: `[citation needed: <title>]`.
**Rule**: AI agents (Codex, Claude, Gemini) are prone to hallucination — always verify before citing.

---

## Principle 7: Tools Are Replaceable, Knowledge Structure Is Permanent

The tools change; the knowledge structure endures.

| Replaceable Tools | Permanent Structure |
|---|---|
| MinerU → alternative OCR | `01_Literature/` intake system |
| Zotero → alternative reference manager | `02_KnowledgeVault/` knowledge graph |
| Obsidian → alternative note app | `02_KnowledgeVault/` naming conventions |
| Better BibTeX → alternative export | `04_Tools/` tool integration layer |

**Rule**: Design the system so that individual tools can be swapped without restructuring the entire workspace.
**Rule**: The KnowledgeVault structure (Papers → Methods → Tasks → Datasets → Experiments → Ideas → Writing) is the permanent asset.

---

## Principle 8: Knowledge Compression Over Reproduction

ResearchAI values compressed understanding over verbatim preservation.

- One Literature Card summarizes 20 pages of a paper.
- One Method note captures the essence of an entire architecture family.
- One Experiment note distills hours of training into key findings.

**Rule**: If processing a paper produces more text than the original, compress it.
**Rule**: The KnowledgeVault should be scannable — a researcher should grasp the entire field in minutes, not hours.

---

## Principle 9: Bidirectional Traceability

Every piece of knowledge must be traceable to its source and to its downstream use.

```
Source (Zotero/PDF) → Processing (MinerU) → Analysis (KnowledgeVault) → Output (Writing)
    ↑                                                                                   ↓
    └────────────────────── Traceability ────────────────────────────────────────────────┘
```

**Rule**: Every KnowledgeVault note links back to its source paper.
**Rule**: Every manuscript cites from Zotero, not from memory.
**Rule**: Every experiment traces back to an idea, which traces back to a paper gap.

---

## Principle 10: Minimal Initial Structure, Organic Growth

The system starts minimal and grows organically with research.

- No empty knowledge nodes.
- No pre-creating categories that may never be used.
- New directories and conventions are only created when actual content demands them.

**Rule**: If a directory has no content, it should not exist.
**Rule**: If a convention is not needed by any current paper, it should not be documented.
**Rule**: The system should feel lightweight, not bureaucratic.
