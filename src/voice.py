import os

WHISPER_AVAILABLE = False
model = None

try:
    import whisper
    import sounddevice as sd
    from scipy.io.wavfile import write
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False


def record_and_transcribe(seconds=5):
    global model

    if not WHISPER_AVAILABLE:
        return "Voice input not available (Whisper not installed)."

    if model is None:
        try:
            model = whisper.load_model("base")
        except Exception:
            return "Voice model not downloaded. Connect to internet once to enable voice input."

    fs = 44100
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write("temp.wav", fs, recording)

    result = model.transcribe("temp.wav")
    return result["text"]
