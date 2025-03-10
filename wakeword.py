import queue
import sounddevice as sd
import vosk
import json
import assistant  # Import assistant.py

# Load Vosk Model
model = vosk.Model("vosk_model")
q = queue.Queue()

# Callback function for audio streaming
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Start listening for wake word
def detect_wake_word():
    print("Listening for wake word...")
    
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                
                if "hey genius" in text:  # Replace with your wake word
                    print("Wake word detected! Activating assistant...")
                    assistant.run_assistant()  # Call assistant function

if __name__ == "__main__":
    detect_wake_word()
