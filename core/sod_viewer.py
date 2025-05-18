# core/sod_viewer.py

"""
GeorgeAI SOD Viewer

Displays today's Start-of-Day markdown log in terminal.
"""

from datetime import datetime
from pathlib import Path
from core.markdown_praser import extract_section
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_sod_file_path():
    today_str = datetime.today().strftime("%Y_%m_%d")
    base_path = Path(__file__).resolve().parent.parent
    return base_path / "reflections" / "SOD" / f"{today_str}_SOD.md"

def display_sod():
    sod_path = get_sod_file_path()
    if not sod_path.exists():
        console.print(f"❌ No SOD file found: {sod_path.name}")
        return

    console.print(Panel.fit(f"📝 Start of Day – {sod_path.stem.replace('_', '-')}", style="bold green"))

    try:
        theme = extract_section(sod_path, "### 🎯 Daily Theme")
        mindset = extract_section(sod_path, "## 🧘 Morning Mindset")
        top_tasks = extract_section(sod_path, "## ✅ Top 3 Tasks")
        intentions = extract_section(sod_path, "## 🧠 Intentions & Purpose")
    except Exception as e:
        console.print(f"⚠️ Error reading SOD sections: {e}")
        return

    if theme: console.print("[bold yellow]Theme:[/bold yellow] " + " ".join(theme))
    if mindset:
        console.print("\n[bold cyan]Mindset:[/bold cyan]")
        console.print("\n".join(mindset))
    if top_tasks:
        console.print("\n[bold magenta]Top Tasks:[/bold magenta]")
        console.print("\n".join(top_tasks))
    if intentions:
        console.print("\n[bold green]Intentions:[/bold green]")
        console.print("\n".join(intentions))

if __name__ == "__main__":
    display_sod()
