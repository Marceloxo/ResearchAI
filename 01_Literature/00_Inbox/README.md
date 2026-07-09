# 00_Inbox — New Paper Intake

## Purpose

Temporary holding area for newly acquired papers before they enter the processing pipeline.

## Input

- New PDF files downloaded or received
- Papers from external sources (email, colleagues, downloads)
- Papers waiting to be classified

## Output

Papers are moved out of Inbox to `01_PDFs/` after initial classification.

## AI Agent Usage

1. When a new PDF arrives, place it here first.
2. Record basic info: title, authors, year.
3. Assign a Paper ID per `Paper_ID_Rules.md`.
4. Move to `01_PDFs/` after classification.
5. Do not leave papers in Inbox for more than one processing cycle.

## Retention Policy

- Papers should be processed within 1 batch cycle.
- If a paper is rejected (not relevant), delete it from Inbox.
- If a paper is accepted, move it through the full pipeline.
