# core/markdown_parser.py

"""
GeorgeAI Markdown Parser

This module provides helper functions for parsing and analyzing markdown logs.
Intended for use with SOD, EOD, reflections, and module-based journals.
"""

from pathlib import Path
from typing import List

def extract_section(file_path: Path, header: str) -> List[str]:
    """
    Extracts lines under a specified markdown header until the next header.
    Returns a list of lines found under the given section.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {file_path}")

    lines = file_path.read_text().splitlines()
    in_section = False
    section_lines = []

    for line in lines:
        if line.strip().startswith(header):
            in_section = True
            continue
        if in_section and line.strip().startswith("## "):
            break
        if in_section:
            section_lines.append(line.strip())

    return section_lines
