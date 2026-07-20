#!/usr/bin/env python3
"""
Validate MinerU output folders for Agent compatibility.

Checks:
- full.md exists
- images/ directory exists
- All markdown image references resolve to actual files

Usage:
    python validate_mineru_output.py              # Validate all folders
    python validate_mineru_output.py <folder>     # Validate single folder
    python validate_mineru_output.py --report     # Save report to file

Default path: /home/lco/ResearchAI_Data/Paper/MinerU_md/
"""

import os
import sys
import re
import argparse
from pathlib import Path
from datetime import datetime

# Configuration
DEFAULT_PATH = Path("/home/lco/ResearchAI_Data/Paper/MinerU_md")
REPORT_DIR = Path("/home/lco/ResearchAI/08_Agent_Config/Migration")


def check_image_refs(md_path, folder_path):
    """Check if all image references in markdown resolve to actual files."""
    content = md_path.read_text(encoding="utf-8", errors="replace")
    
    # Find all ![](images/hash.jpg) references
    refs = re.findall(r'!\[.*?\]\(([^)]+)\)', content)
    
    broken = []
    total = 0
    for ref in refs:
        # Only check image references that start with 'images/'
        if not ref.startswith('images/'):
            continue
        total += 1
        
        # Extract just the filename from images/hash.jpg -> hash.jpg
        basename = os.path.basename(ref)
        # Image files are stored at folder/images/hash.jpg
        # But the reference is relative to full.md, so we look in folder/images/
        img_path = folder_path / "images" / basename
        
        if not img_path.exists():
            broken.append(ref)
    
    return total, len(broken), broken


def validate_folder(folder_path):
    """Validate a single MinerU output folder."""
    result = {
        "path": str(folder_path),
        "pass": True,
        "issues": [],
    }
    
    full_md = folder_path / "full.md"
    images_dir = folder_path / "images"
    
    # Check full.md
    if not full_md.exists():
        result["pass"] = False
        result["issues"].append("missing full.md")
        return result
    
    # Check images/
    if not images_dir.is_dir():
        result["pass"] = False
        result["issues"].append("missing images/ directory")
        return result
    
    # Check image references
    total_refs, broken_refs, broken_list = check_image_refs(full_md, folder_path)
    if broken_refs > 0:
        result["pass"] = False
        result["issues"].append(f"{broken_refs}/{total_refs} broken image refs: {broken_list[:3]}")
    
    return result


def validate_all(path=None):
    """Validate all MinerU output folders."""
    base = Path(path) if path else DEFAULT_PATH
    
    if not base.exists():
        print(f"ERROR: Path not found: {base}")
        sys.exit(1)
    
    results = []
    for d in base.iterdir():
        if d.is_dir():
            results.append(validate_folder(d))
    
    total = len(results)
    passed = sum(1 for r in results if r["pass"])
    failed = total - passed
    
    print(f"\n{'='*60}")
    print(f"MinerU Validation Report")
    print(f"{'='*60}")
    print(f"Total papers: {total}")
    print(f"Compatible: {passed}")
    print(f"Failed: {failed}")
    print(f"{'='*60}")
    
    if failed > 0:
        print("\nFailed folders:")
        for r in results:
            if not r["pass"]:
                name = os.path.basename(r["path"])
                print(f"  FAIL: {name}")
                for issue in r["issues"]:
                    print(f"    - {issue}")
    
    return results, total, passed, failed


def save_report(results, total, passed, failed):
    """Save validation report to file."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / "MinerU_validation_report.md"
    
    with open(str(report_path), "w", encoding="utf-8") as f:
        f.write("# MinerU Output Validation Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"| Metric | Count |\n|---|---|\n")
        f.write(f"| Total papers | {total} |\n")
        f.write(f"| Compatible | {passed} |\n")
        f.write(f"| Failed | {failed} |\n\n")
        
        if failed > 0:
            f.write("## Failed Folders\n\n")
            for r in results:
                if not r["pass"]:
                    name = os.path.basename(r["path"])
                    f.write(f"### FAIL: {name}\n\n")
                    for issue in r["issues"]:
                        f.write(f"- {issue}\n")
                    f.write("\n")
        
        f.write("## Compatible Folders\n\n")
        for r in results:
            if r["pass"]:
                name = os.path.basename(r["path"])
                f.write(f"- {name}\n")
    
    print(f"\nReport saved to: {report_path}")


def main():
    parser = argparse.ArgumentParser(description="Validate MinerU output folders")
    parser.add_argument("path", nargs="?", default=None,
                        help="Path to validate (default: MinerU_md)")
    parser.add_argument("--report", action="store_true",
                        help="Save report to file")
    args = parser.parse_args()
    
    results, total, passed, failed = validate_all(args.path)
    
    if args.report:
        save_report(results, total, passed, failed)


if __name__ == "__main__":
    main()
