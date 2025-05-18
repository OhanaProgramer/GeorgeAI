

from datetime import datetime
from pathlib import Path
from core.markdown_praser import extract_section
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_eod_file_path():
    today_str = datetime.today().strftime("%Y_%m_%d")
    base_path = Path(__file__).resolve().parent.parent
    return base_path / "reflections" / "EOD" / f"{today_str}_EOD.md"

def display_eod():
    eod_path = get_eod_file_path()
    if not eod_path.exists():
        console.print(f"❌ No EOD file found: {eod_path.name}")
        return

    console.print(Panel.fit(f"🌙 End of Day – {eod_path.stem.replace('_', '-')}", style="bold blue"))

    try:
        tasks = extract_section(eod_path, "### ✅ Tasks Today")
        takeaways = extract_section(eod_path, "### 💡 Key Takeaways")
        carry = extract_section(eod_path, "### 🔁 Carry Forward")
        mood = extract_section(eod_path, "### 🧘 Closing Mood")
    except Exception as e:
        console.print(f"⚠️ Error reading EOD sections: {e}")
        return

    if tasks:
        console.print("\n[bold green]Tasks Completed:[/bold green]")
        console.print("\n".join(tasks))
    if takeaways:
        console.print("\n[bold yellow]Key Takeaways:[/bold yellow]")
        console.print("\n".join(takeaways))
    if carry:
        console.print("\n[bold magenta]Carry Forward:[/bold magenta]")
        console.print("\n".join(carry))
    if mood:
        console.print("\n[bold cyan]Closing Mood:[/bold cyan]")
        console.print("\n".join(mood))

if __name__ == "__main__":
    display_eod()