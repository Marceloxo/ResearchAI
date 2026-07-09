# Paper ID Rules

## Purpose

Standardized naming convention for all papers entering the ResearchAI literature system.

## Format

```
YYYY_FirstAuthor_ShortTitle
```

### Components

| Component | Rule | Example |
|---|---|---|
| `YYYY` | Publication year (4 digits) | `2023` |
| `FirstAuthor` | First author's last name (capitalized) | `Monteiro` |
| `ShortTitle` | 3-5 keywords from the title (CamelCase) | `DeepLearningSeismicSegmentation` |

### Full Example

```
2023_Monteiro_DeepLearningSeismicSegmentation
```

## Rules

1. **Year must be present.** Use the publication year of the paper.
2. **Author uses last name only.** No initials, no first name.
3. **Title uses 3-5 keywords.** Capture the core subject matter.
4. **No spaces.** Use CamelCase for multi-word titles.
5. **No special characters.** Only letters, numbers, and underscores.

## Forbidden Formats

- **UUID-based names** — `a1b2c3d4-...` (MinerU default, not human-readable)
- **Random strings** — `paper_12345` (no semantic meaning)
- **Full titles** — `2023_Monteiro_LiteratureReviewOnDeepLearningForTheSegmentationOfSeismicImages` (too long)

## Fallback for Uncertain Papers

If the paper year or first author cannot be determined:

```
TEMP_YYYYMMDD_Number
```

Example: `TEMP_20260708_001`

## Usage in Filenames

Apply the Paper ID to all paper-related files:

- PDF: `2023_Monteiro_DeepLearningSeismicSegmentation.pdf`
- MinerU output folder: `2023_Monteiro_DeepLearningSeismicSegmentation/`
- Processed markdown: `2023_Monteiro_DeepLearningSeismicSegmentation.md`
- KnowledgeVault paper note: `2023_Monteiro_DeepLearningSeismicSegmentation.md`
- KnowledgeVault paper card: `2023_Monteiro_DeepLearningSeismicSegmentation_Card.md`

## Migration of Existing Files

Existing MinerU output folders with UUID names should be renamed to Paper ID format when migrated to the new system.

## Identifier Separation

Each paper has **three independent identifiers**:

| Identifier | System | Format | Example | Purpose |
|---|---|---|---|---|
| **Paper ID** | ResearchAI local | `YYYY_FirstAuthor_ShortTitle` | `2023_Monteiro_DeepLearningSeismicSegmentation` | File organization, human readability |
| **Zotero Item Key** | Zotero internal | 6-char alphanumeric | `ABCDE123` | Immutable Zotero reference |
| **Citation Key** | Better BibTeX | `authorYEARkeyword` (lowercase) | `monteiro2023deeplearning` | Academic citation formatting |

### Key Distinctions

1. **Paper ID != Citation Key**. They serve different purposes and follow different naming conventions. Paper ID uses CamelCase and underscores for file organization. Citation Key uses lowercase for BibTeX compatibility.
2. **They are related but not required to match**. The Literature Index maintains the mapping between all three identifiers.
3. **Changing the Paper ID does not affect Zotero**. Paper ID is ResearchAI-local.
4. **Changing the Citation Key does not affect Paper ID**. Citation Key is managed by Better BibTeX.

See `08_Agent_Config/ResearchAI_Design_Principles.md` (Principle 4) for full details.
