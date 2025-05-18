from datetime import date, timedelta
from pathlib import Path
from utils.george_voice import speak
import os
import logging

def run_startup_integrity_check():
    today = date.today()
    yesterday = today - timedelta(days=1)

    issues = []

    # Core file paths
    task_path = Path(f"./tasks/{today:%Y_%m_%d}_task.json")
    sod_path = Path(f"./reflections/SOD/{today:%Y_%m_%d}_SOD.md")
    eod_path = Path(f"./reflections/EOD/{yesterday:%Y_%m_%d}_EOD.md")
    spanish_csv_path = Path("./logs/Spanish/Unified_Spanish_Log.csv")

    # Check for required files
    if not task_path.exists():
        issues.append("⚠️ Today's task file is missing.")
    if not sod_path.exists():
        issues.append("⚠️ Today's Start of Day file is missing.")
    if not eod_path.exists():
        issues.append("⚠️ Yesterday's End of Day file is missing.")

    # Optional enhancement checks
    if not spanish_csv_path.exists():
        issues.append("⚠️ Spanish tracking CSV not found.")

    # OpenAI key check
    if "OPENAI_API_KEY" not in os.environ:
        issues.append("⚠️ OpenAI API key not detected.")

    # TTS check
    try:
        from TTS.api import TTS
        _ = TTS(model_name="tts_models/en/jenny/jenny")
    except Exception:
        issues.append("⚠️ TTS voice engine failed to load.")

    # Output results
    if issues:
        print("\n📋 GeorgeAI Pre-Flight Check")
        for issue in issues:
            print(issue)
        speak("Heads up. Some planning files or systems need attention.")
    else:
        speak("All systems are green and ready.")