# george_voice_test.py

from TTS.api import TTS

# Load a pre-trained female English model (LJ Speech)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

# Text to speak
text = "Hello Jacque. I'm your local voice, ready to help."

# Save to file
tts.tts_to_file(text=text, file_path="george_speaks.wav")

print("✅ Audio saved to george_speaks.wav")
