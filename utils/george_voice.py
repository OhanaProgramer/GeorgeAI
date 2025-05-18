# george_voice.py

from TTS.api import TTS
import logging
logging.getLogger("TTS").setLevel(logging.ERROR)
import os
import contextlib
import sys

# Voice profile setting — swap model names here to change George's voice
VOICE_MODEL = "tts_models/en/jenny/jenny"

# Load only once
tts = TTS(model_name=VOICE_MODEL)

@contextlib.contextmanager
def suppress_output():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

def speak(text: str, play=True):
    output_file = "george_speaks.wav"
    with suppress_output():
        tts.tts_to_file(text=text, file_path=output_file)
    if play:
        os.system(f"afplay {output_file}")

def speak_if_summary(context):
    prompts = {
        "tasks": "Here is your task list for the day.",
        "success": "Task completed successfully.",
        "greeting": "Good morning Jacques. All systems are green.",
        "eod": "No end of day file found. You might want to reflect or summarize manually.",
        "error": "Something didn't go as planned. Let’s take a look.",
    }
    if context in prompts:
        speak(prompts[context])
    else:
        speak("Something unexpected happened. I’ll take a look.")