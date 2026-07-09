# 02_MinerU_Output — Raw MinerU Parsing Results

## Purpose

Stores the raw output from MinerU Desktop GUI processing. This layer preserves the original parsing results before any cleaning.

## Input

- MinerU Desktop exports (UUID-named folders)
- Each folder contains: `full.md`, `origin.pdf`, `images/`, `layout.json`, `*_content_list.json`, `*_model.json`

## Output

- Cleaned markdown moved to `03_Processed_Markdown/`
- Raw MinerU folders are archived here permanently

## Directory Structure

```
02_MinerU_Output/
  2023_Monteiro_DeepLearningSeismicSegmentation/
    ├── full.md
    ├── origin.pdf
    ├── images/
    ├── layout.json
    └── *_content_list.json
```

## AI Agent Usage

1. After MinerU Desktop processes a PDF, copy the output folder here.
2. Rename the UUID folder to use the Paper ID naming convention.
3. Read `full.md` for Level 1 screening.
4. Do not modify files in this directory — they are the raw parsing artifact.
5. If MinerU output is incomplete or corrupted, note this in the Literature Index.

## Important

- This is the **raw** layer. Never put processed/cleaned content here.
- Keep this directory organized by Paper ID, not UUID.
- The raw MinerU UUID folders should be renamed after ingestion.
