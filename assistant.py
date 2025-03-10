import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import webbrowser
import os
import platform
from config import GEMINI_API_KEY  # Secure API key storage

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(query):
    """Send query to Google Gemini AI."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(query)
    return response.text

# Initialize TTS Engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice commands."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand.")
        return None
    except sr.RequestError:
        print("API request error.")
        return None

def open_application(app_name):
    """Open applications based on OS."""
    system = platform.system()

    # Define app launch commands
    apps = {
        "Darwin": {  # macOS
            "chrome": "open -a 'Google Chrome'",
            "vs code": "open -a 'Visual Studio Code'",
            "whatsapp": "open -a 'WhatsApp'",
            "settings": "open -a 'System Settings'",
            "calculator": "open -a 'Calculator'",
            "spotify": "open -a 'Spotify'",
            "youtube": "open -a 'Safari' https://www.youtube.com"
        },
        "Windows": {
            "chrome": "start chrome",
            "vs code": "code",
            "whatsapp": "start whatsapp",
            "settings": "start ms-settings:",
            "calculator": "calc",
            "spotify": "start spotify",
            "youtube": "start chrome https://www.youtube.com"
        },
        "Linux": {
            "chrome": "google-chrome",
            "vs code": "code",
            "whatsapp": "whatsapp-desktop",
            "settings": "gnome-control-center",
            "calculator": "gnome-calculator",
            "spotify": "spotify",
            "youtube": "xdg-open https://www.youtube.com"
        }
    }

    # Normalize app name
    app_name = app_name.lower().strip()

    # Execute the appropriate command
    if system in apps and app_name in apps[system]:
        speak(f"Opening {app_name}...")
        os.system(apps[system][app_name])
    else:
        speak(f"Sorry, I couldn't find a way to open {app_name} on {system}.")

def handle_query(query):
    """Handle user queries."""
    if not query:
        return
    
    if "open" in query:
        app_name = query.replace("open ", "").strip()
        open_application(app_name)

    elif "search" in query:
        search_query = query.replace("search", "").strip()
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "exit" in query or "stop" in query:
        speak("Goodbye!")
        exit()

    else:
        answer = ask_gemini(query)
        speak(answer)

def run_assistant():
    """Main assistant loop."""
    while True:
        query = listen()
        handle_query(query)

if __name__ == "__main__":
    run_assistant()
