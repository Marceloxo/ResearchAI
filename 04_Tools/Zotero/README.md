# 04_Tools/Zotero — Zotero Integration Scripts

## Purpose

This directory holds tools and scripts for Zotero integration with ResearchAI.

## Contents

- `Zotero_Setup_Guide.md` — step-by-step installation and configuration guide
- `metadata_mapping.md` — Zotero field ↔ ResearchAI field mapping reference
- `bib_sync.sh` (future) — BibTeX export synchronization script
- `collection_manager.py` (future) — automated collection/tag management
- `paper_id_mapper.py` (future) — Paper ID ↔ Zotero item key converter

## What NOT to Store

- **Zotero database files** (`.sqlite`, `.db`) — these belong in the Zotero data directory
- **PDF files** — stored in `01_Literature/01_PDFs/` and Zotero's own PDF storage
- **BibTeX exports** — stored in `01_Literature/04_Literature_Index/bibliography.bib`

## Zotero Responsibilities

- Better BibTeX configuration
- BibTeX synchronization
- Metadata processing and validation
- Collection/tag automation scripts

## Current Status

**Not yet implemented.** Zotero is not installed. This directory is a placeholder for future scripts and configuration.
