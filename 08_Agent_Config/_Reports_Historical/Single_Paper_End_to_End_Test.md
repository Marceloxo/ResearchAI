# Single Paper End-to-End Test

## Purpose

Validate the complete Zotero -> ResearchAI pipeline with a single paper. This is the integration test before scaling to 3-5 papers.

## Test Paper

**Paper ID**: `2023_Monteiro_DeepLearningSeismicSegmentation`

- **Title**: Literature review on deep learning for the segmentation of seismic images
- **Authors**: Monteiro et al.
- **Year**: 2023
- **Type**: Survey / Review
- **Current Status**: Already processed in KnowledgeVault (18 knowledge nodes)

## Test Checklist

### Phase 1: Zotero Setup

- [ ] **1.1** Install Zotero
- [ ] **1.2** Install Better BibTeX plugin
- [ ] **1.3** Configure collections: Inbox, Reading, Deep Read, Reference
- [ ] **1.4** Configure tags: #to-read, #reading, #done, #key-paper, #survey, #seismic-ai, #segmentation
- [ ] **1.5** Configure Better BibTeX citation key format: `authorYEARkeyword` (NOT Paper ID format)
- [ ] **1.6** Configure BibTeX export target: `C:\ResearchAI\01_Literature\04_Literature_Index\bibliography.bib`
- [ ] **1.7** Configure attachment storage: external drive (NOT ResearchAI workspace)

### Phase 2: Import and Verify

- [ ] **2.1** Import `2023_Monteiro_DeepLearningSeismicSegmentation.pdf` to Zotero
- [ ] **2.2** Verify Zotero auto-detected metadata (title, authors, year, journal, DOI)
- [ ] **2.3** Assign to `ResearchAI/Inbox` collection
- [ ] **2.4** Assign tags: `#to-read`, `#seismic-ai`, `#survey`
- [ ] **2.5** Note the Zotero item key (6-char code)
- [ ] **2.6** Note the Better BibTeX citation key

### Phase 3: BibTeX Export

- [ ] **3.1** Trigger BibTeX export
- [ ] **3.2** Verify `bibliography.bib` exists in `01_Literature/04_Literature_Index/`
- [ ] **3.3** Verify BibTeX entry has correct title, authors, year, DOI
- [ ] **3.4** Verify citation key format is `authorYEARkeyword` (e.g., `monteiro2023deeplearning`)

### Phase 4: Literature Index Update

- [ ] **4.1** Add row to `Literature_Index.md`:
  - `paper_id`: `2023_Monteiro_DeepLearningSeismicSegmentation`
  - `zotero_key`: (from step 2.5)
  - `citation_key`: (from step 2.6)
  - `doi`: (from step 2.2)
  - `citation_status`: `not_cited`
- [ ] **4.2** Verify bidirectional lookup: Literature Index -> Zotero item key works
- [ ] **4.3** Verify bidirectional lookup: Zotero citation key -> BibTeX entry works

### Phase 5: MinerU Processing

- [ ] **5.1** Run MinerU Desktop on the test PDF
- [ ] **5.2** Verify output folder in `01_Literature/02_MinerU_Output/`
- [ ] **5.3** Rename UUID folder to Paper ID

### Phase 6: Processed Markdown

- [ ] **6.1** Apply cleaning rules from `MinerU_Cleaning_Rules.md`
- [ ] **6.2** Generate processed markdown using `Processed_Markdown_Template.md`
- [ ] **6.3** Save to `01_Literature/03_Processed_Markdown/` with Paper ID filename
- [ ] **6.4** Quality assessment: Good / Fair / Poor

### Phase 7: KnowledgeVault Verification

- [ ] **7.1** Verify Literature Card exists and includes `zotero_key` and `citation_key`
- [ ] **7.2** Verify Paper Note exists and includes `zotero_key` and `citation_key`
- [ ] **7.3** Verify Method notes (CNN, U-Net, Transformer, Attention) link to this paper
- [ ] **7.4** Verify Task notes (Fault Segmentation, Seismic Image Segmentation) link to this paper
- [ ] **7.5** Verify Dataset notes (F3 Netherlands, Parihaka, etc.) link to this paper

### Phase 8: Obsidian Graph Verification

- [ ] **8.1** Open KnowledgeVault in Obsidian
- [ ] **8.2** Verify Paper Note has outgoing links to Methods, Tasks, Datasets
- [ ] **8.3** Verify Method notes have incoming links from Paper Note
- [ ] **8.4** Verify no orphan nodes (notes with zero connections)
- [ ] **8.5** Verify graph shows a connected cluster for this paper's knowledge

### Phase 9: Citation Integrity

- [ ] **9.1** Verify all citations in Paper Note come from Zotero (not fabricated)
- [ ] **9.2** Verify DOI in Paper Note matches Zotero DOI exactly
- [ ] **9.3** Verify authors in Paper Note match Zotero creators exactly
- [ ] **9.4** Verify no duplicate metadata between Zotero and KnowledgeVault

## Success Criteria

| Criterion | Pass Condition |
|---|---|
| Zotero metadata | Title, authors, year, DOI match exactly |
| Citation key format | `authorYEARkeyword`, NOT Paper ID format |
| BibTeX export | File exists, entry is correct |
| Literature Index | All three identifiers present and linked |
| Bidirectional lookup | Literature Index <-> Zotero works both ways |
| KnowledgeVault links | Paper Note links to Methods, Tasks, Datasets |
| Obsidian graph | Connected cluster, no orphans |
| Citation integrity | All citations traceable to Zotero |
| No duplication | Metadata stored once in Zotero, not duplicated |

## Failure Recovery

If any criterion fails:

1. **Metadata mismatch**: Re-import to Zotero, verify auto-detection.
2. **Citation key wrong format**: Adjust Better BibTeX settings to `authorYEARkeyword`.
3. **DOI missing**: Manually add DOI to Zotero, re-export.
4. **Lookup broken**: Check Literature Index for correct `zotero_key` value.
5. **Graph disconnected**: Check wikilinks in Paper Note and related notes.

## Post-Test Actions

After successful test:

1. Update `Zotero_Deployment_Record.md` with lessons learned.
2. Update `Zotero_Integration_Design.md` if any design changes are needed.
3. Proceed to processing 3-5 more papers through the full pipeline.
4. Mark this test plan as completed.

After failed test:

1. Document what failed and why.
2. Fix the issue.
3. Retry the test.
4. Do NOT proceed to full pipeline until test passes.
