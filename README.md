

# **Genius - AI Voice Assistant 🚀**

Genius is a J.A.R.V.I.S-inspired AI-powered voice assistant designed to execute voice commands, control applications, answer queries using Google Gemini AI, and provide a seamless interactive experience through a futuristic web interface.

## **🛠 Features**
- 🎙 **Wake Word Detection**: Activate with "Hey Genius" (using Vosk).
- 💡 **AI-Powered Responses**: Uses **Google Gemini AI** for smart interactions.
- 🖥 **App & Web Control**: Open applications like VS Code, Chrome, WhatsApp, and system settings.
- 🌐 **Web App Integration**: Real-time voice interaction with a futuristic UI.
- 🔊 **Text-to-Speech (TTS)**: Converts responses to speech.
- 🎤 **Speech Recognition**: Listens to user commands and executes actions.
- 🌎 **Web Search**: Open YouTube, Google, and other websites.
- 🔌 **Cross-Platform**: Works on macOS, Windows, and Linux.

---

## **📦 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/hrishabh1103/Minor2_Genius_2.0.git
cd genius-voice-assistant
```

### **2️⃣ Install Dependencies**
Ensure you have Python 3.11+ installed.

```bash
pip install flask flask-cors flask-socketio pyttsx3 vosk pyaudio google-generativeai
```

### **3️⃣ Download Vosk Model**
```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 vosk_model
```

---

## **🚀 Running the Assistant**
### **Start the Backend (Python Server)**
```bash
wakeword.py
```

### **Start the Web App**
- If using **Bolt.new**, deploy your frontend there.
- If running locally, open `index.html` in a browser.

---

## **🎙 How to Use**
1. **Say "Hey Genius"** → The assistant will wake up.
2. **Give a command**, like:
   - **"Open YouTube"** → Opens YouTube in a browser.
   - **"What's the weather today?"** → Gets weather updates.
   - **"Set a reminder"** → Saves reminders.
   - **"Tell me a joke"** → Fetches a joke using Gemini AI.
   - **"Exit"** → Closes the assistant.

3. **For manual input**, type commands in the web interface.

---

## **📌 Configuration**
- Add your **Gemini API key** in `config.py`:
```python
GEMINI_API_KEY = "your-api-key-here"
```

---

## **🛠 Future Improvements**
- 🤖 **Custom Wake Words** using Porcupine AI.
- 🔥 **Home Automation Integration** (IoT).
- 🌐 **Cloud Deployment** for remote access.
- 📱 **Mobile-Friendly UI** for smart assistants.

---

## **🤝 Contributing**
Want to improve Genius? Fork this repo and submit a pull request! 🚀

---

## **📜 License**
MIT License © 2025 Hrishabh Gupta
