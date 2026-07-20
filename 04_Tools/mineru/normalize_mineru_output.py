#!/usr/bin/env python3
"""
MinerU Output Normalizer

Converts MinerU output variants (Desktop A/B/C and CLI) into a stable
Agent-compatible format: full.md + images/ + metadata/ at the folder root.

Usage:
    python normalize_mineru_output.py <mineru_output_folder>

Supported cases:
    Case A: full.md already exists at root -> verify only
    Case B: hybrid_auto/*.md exists -> copy markdown to full.md
    Case C: txt/*.md exists (CLI output) -> copy markdown to full.md, fix image paths
    Case D: other markdown filename exists -> rename/copy to full.md
"""

import os
import sys
import shutil
import re
from pathlib import Path
from datetime import datetime


def log_action(log_path, action, detail):
    """Append a normalization action to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {action}: {detail}\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def find_markdown_files(folder):
    """Find all .md files in the folder (excluding content_list, model, layout, etc.)."""
    md_files = []
    for root, dirs, files in os.walk(folder):
        for fname in files:
            if fname.endswith(".md"):
                full_path = os.path.join(root, fname)
                if any(kw in fname.lower() for kw in [
                    "content_list", "model", "layout", "middle", "span",
                    "mineru_markdown"
                ]):
                    continue
                md_files.append(full_path)
    return md_files


def fix_image_paths(content):
    """Fix image references to always use relative images/ path."""
    def replace_image(match):
        path = match.group(1)
        basename = os.path.basename(path)
        return f"![](images/{basename})"
    content = re.sub(r'!\[\]\(([^)]+)\)', replace_image, content)
    return content


def normalize_folder(folder_path):
    """Normalize a single MinerU output folder."""
    folder = Path(folder_path).resolve()
    log_path = folder / ".normalization.log"
    
    print(f"\n{'='*60}")
    print(f"Normalizing: {folder}")
    print(f"{'='*60}")
    
    # Case A: full.md already exists
    full_md = folder / "full.md"
    if full_md.exists():
        print("  [OK] full.md already exists at root.")
        log_action(str(log_path), "SKIP", "full.md already exists at root")
        return "already_normalized"
    
    # Find markdown files
    md_files = find_markdown_files(str(folder))
    if not md_files:
        print("  [WARN] No markdown files found.")
        log_action(str(log_path), "ERROR", "No markdown files found")
        return "error_no_md"
    
    # Case B: hybrid_auto subfolder
    hybrid_auto = folder / "hybrid_auto"
    if hybrid_auto.exists() and hybrid_auto.is_dir():
        md_in_hybrid = [f for f in md_files if "hybrid_auto" in f]
        if md_in_hybrid:
            src_md = md_in_hybrid[0]
            print(f"  [CASE B] Found markdown in hybrid_auto/: {os.path.basename(src_md)}")
            content = open(src_md, "r", encoding="utf-8").read()
            content = fix_image_paths(content)
            with open(str(full_md), "w", encoding="utf-8") as f:
                f.write(content)
            src_images = os.path.join(os.path.dirname(src_md), "images")
            dst_images = folder / "images"
            if os.path.exists(src_images):
                shutil.copytree(src_images, dst_images, dirs_exist_ok=True)
                print(f"  [OK] Copied images from hybrid_auto/images/")
            log_action(str(log_path), "COPY", f"hybrid_auto -> full.md ({len(content)} chars)")
            return "normalized_b"
    
    # Case C: CLI output (txt/ subfolder)
    txt_dir = folder / "txt"
    if txt_dir.exists() and txt_dir.is_dir():
        md_in_txt = [f for f in md_files if "txt" in f]
        if md_in_txt:
            src_md = md_in_txt[0]
            print(f"  [CASE C] Found CLI output in txt/: {os.path.basename(src_md)}")
            content = open(src_md, "r", encoding="utf-8").read()
            content = fix_image_paths(content)
            with open(str(full_md), "w", encoding="utf-8") as f:
                f.write(content)
            src_images = os.path.join(os.path.dirname(src_md), "images")
            dst_images = folder / "images"
            if os.path.exists(src_images):
                shutil.copytree(src_images, dst_images, dirs_exist_ok=True)
                print(f"  [OK] Copied images from txt/images/")
            log_action(str(log_path), "COPY", f"CLI txt -> full.md ({len(content)} chars)")
            return "normalized_c"
    
    # Case D: Single markdown file at any level
    if len(md_files) == 1:
        src_md = md_files[0]
        rel_path = os.path.relpath(src_md, str(folder))
        print(f"  [CASE D] Single markdown found: {rel_path}")
        content = open(src_md, "r", encoding="utf-8").read()
        content = fix_image_paths(content)
        with open(str(full_md), "w", encoding="utf-8") as f:
            f.write(content)
        src_img_dir = os.path.join(os.path.dirname(src_md), "images")
        dst_img_dir = folder / "images"
        if os.path.exists(src_img_dir):
            shutil.copytree(src_img_dir, dst_img_dir, dirs_exist_ok=True)
            print(f"  [OK] Copied images from {src_img_dir}")
        log_action(str(log_path), "COPY", f"{rel_path} -> full.md ({len(content)} chars)")
        return "normalized_d"
    
    # Multiple markdowns - ambiguous
    print(f"  [WARN] Multiple markdown files found ({len(md_files)}):")
    for mf in md_files:
        print(f"    - {os.path.relpath(mf, str(folder))}")
    log_action(str(log_path), "WARN", f"Ambiguous: {len(md_files)} markdown files found")
    return "ambiguous"


def main():
    if len(sys.argv) < 2:
        print("Usage: python normalize_mineru_output.py <mineru_output_folder>")
        print("       python normalize_mineru_output.py <folder1> <folder2> ...")
        sys.exit(1)
    
    results = {"already_normalized": 0, "normalized_b": 0, "normalized_c": 0, 
               "normalized_d": 0, "error_no_md": 0, "ambiguous": 0}
    
    for folder_path in sys.argv[1:]:
        if not os.path.isdir(folder_path):
            print(f"[ERROR] Not a directory: {folder_path}")
            continue
        result = normalize_folder(folder_path)
        results[result] = results.get(result, 0) + 1
    
    print(f"\n{'='*60}")
    print("Summary:")
    for k, v in results.items():
        if v > 0:
            print(f"  {k}: {v}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
