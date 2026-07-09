# 00_Meta — Vault Meta-Information

## Purpose

Central indexing and navigation layer for the knowledge vault. This directory contains Maps of Content (MOCs), vault-wide indices, and structural documentation that help both humans and AI agents navigate the knowledge base.

## Contents

- **MOC files**: Hub pages that aggregate links for a given topic, method, or task (e.g., `MOC - Seismic Fault Segmentation`).
- **Vault index**: A master list of all notes organized by category.
- **Tag registry**: A reference of all tags used in the vault with definitions.
- **Vault statistics**: Optional tracking of note counts, link density, and coverage gaps.

## Relationship to Other Directories

- Indexes content from every other subdirectory in the vault.
- Provides the entry point for AI agents to understand vault scope before performing tasks.
- Referenced by `Vault_README.md` for vault-level conventions.

## AI Agent Usage

1. Start here when first exploring the vault — read MOC files to understand what knowledge exists.
2. After adding new notes, check whether a MOC should be updated.
3. Before proposing new research directions, consult relevant MOCs to avoid duplication.
4. Update the master index when creating new note categories.
