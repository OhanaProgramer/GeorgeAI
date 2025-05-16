# core/sod_generator.py

"""
GeorgeAI Start-of-Day Generator

Uses prior EOD logs and task completion to scaffold the next day's SOD entry.
Eventually supports intent inference, module activation, and tone suggestions.
"""

from pathlib import Path
from datetime import datetime


def generate_sod_stub(eod_path: Path, output_folder: Path) -> Path:
    """
    Generates a blank or semi-filled SOD markdown file based on yesterday's EOD.
    Currently a stub – will later extract modules, mindset, and suggestions.
    """
    date_str = datetime.today().strftime("%Y_%m_%d")
    sod_path = output_folder / f"{date_str}_SOD.md"

    content = f"""# 🌅 Start of Day – {date_str}

### 🎯 Daily Theme
*{{Theme will be suggested here}}*

---

## 🧘 Morning Mindset
- Mood:
- Energy Level:
- Focus Word:
- Physical State (body scan):

---

## ✅ Top 3 Tasks
1. [ ]
2. [ ]
3. [ ]

---

## 🧩 Focus Modules for Today
- [ ] GeorgeAI
- [ ] Travel
- [ ] Health
- [ ] Art
- [ ] Music
- [ ] Spanish
- [ ] Free/Unstructured Time

---

## 🧠 Intentions & Purpose

---

## 🛠️ Prep Notes

"""

    sod_path.write_text(content)
    return sod_path