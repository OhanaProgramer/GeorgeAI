# core/eod_to_sod_bridge.py

"""
GeorgeAI EOD → SOD Bridge

Generates a Start-of-Day (SOD) log pre-filled with key insights from the previous End-of-Day (EOD).
This connects reflections to intentions, enabling memory continuity and smoother daily planning.
"""

from datetime import datetime, timedelta
from pathlib import Path
from core.markdown_praser import extract_section
from core.sod_generator import generate_sod_stub


def get_yesterday_eod_path() -> Path:
    yesterday = datetime.today() - timedelta(days=1)
    date_str = yesterday.strftime("%Y_%m_%d")
    base_path = Path(__file__).resolve().parent.parent
    return base_path / "reflections" / "EOD" / f"{date_str}_EOD.md"


def generate_sod_from_eod():
    eod_path = get_yesterday_eod_path()
    if not eod_path.exists():
        print(f"❌ No EOD log found for yesterday: {eod_path.name}")
        return None

    try:
        insights = extract_section(eod_path, "## 💡 Key Takeaways")
        carry_forward = extract_section(eod_path, "### 🔁 Carry Forward")
        mood = extract_section(eod_path, "### 🧘 Closing Mood")
    except Exception as e:
        print("⚠️ Error parsing EOD:", e)
        return None

    content_blocks = {
        "intentions": "\n".join(insights + carry_forward).strip(),
        "mood": "\n".join(mood).strip()
    }

    base_path = Path(__file__).resolve().parent.parent
    output_folder = base_path / "reflections" / "SOD"
    return generate_sod_stub(content_blocks, output_folder)


if __name__ == "__main__":
    result = generate_sod_from_eod()
    if result:
        print(f"✅ SOD generated with EOD context: {result.name}")
