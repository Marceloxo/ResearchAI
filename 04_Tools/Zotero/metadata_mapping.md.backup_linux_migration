# Metadata Mapping

## Purpose

Define the correspondence between Zotero fields and ResearchAI fields. This mapping ensures consistency when data flows between the two systems.

---

## Field Mapping Table

### Core Metadata

| Zotero Field | ResearchAI Field | Source of Truth | Sync Direction |
|---|---|---|---|
| `title` | `title` (YAML) | Zotero | Zotero → ResearchAI |
| `creators[0].lastName` | `authors` (YAML) | Zotero | Zotero → ResearchAI |
| `date` (year) | `year` (YAML) | Zotero | Zotero → ResearchAI |
| `publicationTitle` | `venue` (YAML) | Zotero | Zotero → ResearchAI |
| `DOI` | `doi` (YAML) | Zotero | Zotero → ResearchAI |
| `itemKey` | `zotero_key` (Literature Index) | Zotero | Zotero → ResearchAI |
| `citationKey` (BBT) | `citation_key` (Literature Index) | Better BibTeX | Zotero → ResearchAI |
| `tags[].name` | `tags` (YAML) | Both | Bidirectional |

### ResearchAI-Generated Fields

| ResearchAI Field | Source | Notes |
|---|---|---|
| `paper_id` | ResearchAI local | `YYYY_FirstAuthor_ShortTitle` |
| `paper_type` | ResearchAI local | `research_article` / `survey` / `review` / `benchmark` |
| `reading_status` | ResearchAI local | `to-read` / `reading` / `done` / `archived` |
| `importance` | ResearchAI local | `high` / `medium` / `low` |
| `knowledge_status` | ResearchAI local | Tracking vault extraction progress |
| `methods_extracted` | ResearchAI local | List of method notes created |
| `datasets_extracted` | ResearchAI local | List of dataset notes created |

### Cross-Reference Fields

| Field | Purpose |
|---|---|
| `zotero_key` | Links ResearchAI paper to Zotero item |
| `citation_key` | Links ResearchAI paper to BibTeX entry |
| `doi` | Universal identifier, shared between systems |

---

## Literature Index Schema

When Zotero is connected, the Literature Index table gains these columns:

| Column | Source | Example |
|---|---|---|
| `paper_id` | ResearchAI | `2023_Monteiro_DeepLearningSeismicSegmentation` |
| `title` | Zotero | "Literature review on deep learning..." |
| `year` | Zotero | `2023` |
| `type` | ResearchAI | `survey` |
| `zotero_key` | Zotero | `ABCDE123` |
| `citation_key` | Better BibTeX | `monteiro2023deeplearning` |
| `doi` | Zotero | `10.xxxx/xxxxx` |
| `status` | ResearchAI | `deep_read` |
| `knowledge_status` | ResearchAI | `paper_note` |

---

## Sync Protocol

### When Zotero Changes → ResearchAI Updates

1. Better BibTeX exports updated `bibliography.bib`
2. `Literature_Index.md` is updated with new `zotero_key` and `citation_key`
3. Paper metadata in KnowledgeVault notes is verified against Zotero

### When ResearchAI Changes → Zotero Updates

1. Reading status (`inbox` → `screened` → `deep_read`) synced to Zotero tags
2. New tags added to Zotero (e.g., `#key-paper`) reflected in Literature Index
3. Paper type classification does NOT sync to Zotero (Zotero has no equivalent)

### Conflict Resolution

- **Metadata conflicts** (title, authors, year): Zotero wins
- **Status conflicts** (reading progress): ResearchAI wins
- **Classification conflicts** (paper type): ResearchAI wins
- **Tag conflicts**: Manual review required
