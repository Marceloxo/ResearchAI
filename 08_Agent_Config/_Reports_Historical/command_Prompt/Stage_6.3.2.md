
# Stage 6.4.1 — MinerU Path Architecture Correction and Verification

The previous Stage 6.4 blocker report is invalid because it used an outdated PDF path assumption.

Before any further action, update the pipeline architecture understanding.

## Authoritative Pipeline

PDF source:

```

/home/lco/ResearchAI_Data/Zotero/storage/

```

Each Zotero storage directory contains the original PDF attachment.

Example:

McBrearty 2023:
```

/home/lco/ResearchAI_Data/Zotero/storage/2ZVY52Y6/
McBrearty和Beroza - 2023 - Earthquake Phase Association with Graph Neural Networks.pdf

```

Wang 2023:
```

/home/lco/ResearchAI_Data/Zotero/storage/J2ML7W6A/
Wang 等 - 2023 - Seismic Facies Segmentation via a Segformer-Based Specific Encoder–Decoder–Hypercolumns Scheme.pdf

```

These PDFs have been manually verified to exist.

---

## Deprecated Path

The following path is obsolete:

```

/home/lco/ResearchAI_Data/Paper/Origin_pdf

```

Do NOT use it.

It is not part of the current pipeline.

---

## Current MinerU Architecture

Input:

```

Zotero/storage/<ZoteroKey>/*.pdf

```

Output:

```

/home/lco/ResearchAI_Data/Paper/MinerU_md/<paper>/full.md

```

MinerU_md is the only Markdown output location.

---

## Task

Do NOT create Deep Read Notes yet.

Perform only:

1. Verify MinerU output status for:
   - Wang 2023 Segformer seismic facies segmentation
   - McBrearty 2023 GNN phase association

2. Verify whether corresponding full.md exists under:

```

/home/lco/ResearchAI_Data/Paper/MinerU_md/

```

3. If missing, prepare MinerU processing plan using existing pipeline.

4. Update Stage 6.4 status.

Constraints:
- Do not modify templates.
- Do not create skills.
- Do not modify historical reports.
- Do not use Origin_pdf.

Create:

```

08_Agent_Config/Migration/Stage_6.4.1_MinerU_Path_Verification_Report.md

```

The report must explicitly state:

"Zotero/storage is the authoritative PDF source. MinerU_md is the authoritative Markdown output."


