# ADR-001: Zotero-Centered PDF Architecture

## Date

2026-07-09

## Status

Accepted

## Context

ResearchAI needs a single, authoritative source for paper PDFs. Previous designs used two separate PDF locations, creating confusion about which system owns PDFs.

## Decision

**Zotero is the sole owner of all paper PDFs.**

Zotero's data directory is at:

```
D:\ResearchAI_Data\
```

This directory contains:
- `zotero.sqlite` — database (bibliographic metadata)
- `storage/` — PDF files (single source of truth for all paper PDFs)
- `styles/` — citation styles
- `translators/` — import translators
- `locate/` — full-text indexing

MinerU reads PDFs directly from `D:\ResearchAI_Data\storage\`.

## Consequences

### Positive

- **Single source of truth**: One copy of each PDF. No duplication.
- **Simpler pipeline**: MinerU reads from Zotero storage directly.
- **Cleaner architecture**: Zotero manages PDFs + metadata. ResearchAI manages knowledge extraction.
- **Reduced confusion**: New agents know exactly where to find PDFs.

### Negative

- **MinerU reads Zotero internals**: Accessing `storage/` is reading Zotero's internal directory. However, this is read-only and safe.
- **Requires Zotero first**: Papers must be in Zotero before MinerU can process them. This is a feature — it enforces the Zotero-first workflow.

### Neutral

- **MinerU output still goes to**: `D:\ResearchAI_Data\Paper\MinerU_md\`
- **ResearchAI workspace unchanged**: `C:\ResearchAI\` still contains all knowledge, code, and documentation.

## Architecture

```
Zotero (D:\ResearchAI_Data\)
    ├── storage/          ← PDF source (MinerU reads here)
    ├── zotero.sqlite     ← Metadata (authoritative)
    ├── styles/           ← Citation styles
    ├── translators/      ← Import translators
    └── locate/           ← Full-text indexing

MinerU Desktop
    ├── Input: D:\ResearchAI_Data\storage\{hash}.pdf
    └── Output: D:\ResearchAI_Data\Paper\MinerU_md\{paper_id}\

ResearchAI Processing
    ├── 01_Literature/02_MinerU_Output/ ← references to MinerU output
    ├── 01_Literature/03_Processed_Markdown/ ← cleaned markdown
    └── 02_KnowledgeVault/ ← structured knowledge (no PDFs)
```

## PDF Lifecycle

```
Paper added to Zotero → Stored in D:\ResearchAI_Data\storage\
    ↓
MinerU reads PDF from storage/
    ↓
MinerU outputs markdown to D:\ResearchAI_Data\Paper\MinerU_md\
    ↓
ResearchAI processes markdown → KnowledgeVault
```

## Migration Strategy

### Current State

- Zotero data directory: `D:\ResearchAI_Data\` (actual)
- `D:\ResearchAI_Data\Paper\Origin_pdf\` — deprecated, not a system directory
- `D:\ResearchAI_Data\Zotero_Attachments\` — not used (replaced by Zotero's own storage)

### No Immediate Action Required

- No PDF files are moved
- No Zotero configuration is changed
- Existing papers are not affected
- The change is purely architectural — documented in this ADR

## Alternatives Considered

### Option A: Separate PDF Directory (Previous Design)

- **Pros**: Independence from Zotero
- **Cons**: Two copies of PDFs; confusion about authority; harder to maintain consistency

### Option B: Zotero-Centered (Chosen)

- **Pros**: Single source of truth; no duplication; cleaner architecture
- **Cons**: Requires Zotero to be running for PDF access

### Option C: Central PDF Library Outside Both

- **Pros**: Maximum flexibility
- **Cons**: More complex; requires third coordination system

Option B was chosen because simplicity and single-source-of-truth outweigh the minor inconvenience of Zotero dependency.

## References

- `04_Tools/Zotero/Zotero_Storage_Strategy.md` — updated to reflect this decision
- `04_Tools/Data_Storage_Architecture.md` — updated to reflect this decision
- `D:\ResearchAI_Data\README.md` — updated to reflect this decision
- `AGENT_BOOTSTRAP.md` — updated to reflect this decision
