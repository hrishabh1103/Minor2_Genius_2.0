import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Helps with background noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Stops after 5 seconds of silence
            query = recognizer.recognize_google(audio)
            print("You said:", query)  # Debugging output
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Speech Recognition API request failed.")
            return None

def handle_query(query):
    if "hello" in query:
        speak("Hello! How can I assist you?")
    else:
        speak("I didn't understand that.")

def run_assistant():
    while True:
        query = listen()
        if query:
            handle_query(query)

if __name__ == "__main__":
    run_assistant()
