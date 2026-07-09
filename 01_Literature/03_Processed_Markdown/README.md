# 03_Processed_Markdown — Cleaned Markdown for Analysis

## Purpose

Cleaned and standardized markdown files ready for AI agent analysis. This is the bridge between raw MinerU output and KnowledgeVault knowledge extraction.

**This directory does not store paper text for reading.** It stores paper text for *understanding*.

---

## Three-Layer Architecture

| Layer | Location | Purpose | Audience |
|---|---|---|---|
| **Raw MinerU** | `02_MinerU_Output/` | Original parsing output, untouched | MinerU output |
| **Processed Markdown** | `03_Processed_Markdown/` | Cleaned, structured, AI-ready | AI agents for screening/analysis |
| **KnowledgeVault** | `02_KnowledgeVault/` | Extracted knowledge, wikilinks | Humans + AI navigation |

Raw data never enters the KnowledgeVault. Only extracted knowledge does.

---

## What Is Processed Markdown?

Processed Markdown is a **structured extraction** from raw MinerU `full.md`:

- MinerU `full.md` contains: headers, footers, page numbers, layout JSON references, image hashes, model metadata, repeated text blocks
- Processed Markdown contains: abstract, introduction, methods, results, conclusions — stripped of parsing artifacts

Processed Markdown is **not** a copy of the paper. It is a cleaned version optimized for AI reading.

---

## File Naming

- Use Paper ID: `YYYY_FirstAuthor_ShortTitle.md`
- Example: `2023_Monteiro_DeepLearningSeismicSegmentation.md`

---

## Storage Policy

- Processed Markdown is a **transient workspace**, not an archive.
- After knowledge extraction, the processed markdown may be archived or deleted.
- Keep this directory lean — it is a processing layer, not a document library.
- The permanent copy of the paper lives in `02_KnowledgeVault/` as structured notes.

---

## AI Agent Usage

1. Read cleaned markdown from this directory for Level 1 screening and Level 2 deep analysis.
2. Do not modify files here — if cleaning is needed, fix the source in `02_MinerU_Output/`.
3. After knowledge extraction, the processed markdown may be archived or deleted.
4. Always reference the raw output in `02_MinerU_Output/` if you need to verify parsing quality.

---

## Cleaning Standards

See `08_Agent_Config/MinerU_Cleaning_Rules.md` for the full cleaning specification.

Quick rules:
- Keep: title, abstract, sections, formulas, tables, method descriptions, results
- Remove: headers, footers, page numbers, repeated text, layout JSON references, model JSON
- Images: keep index, do not embed all images
- Encoding: fix Chinese characters and special symbols
