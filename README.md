<div align="center">

# Vevo AI Assistant

<p align="center"><b>A smart Windows desktop AI assistant — activated by voice or hotkey.</b></p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Groq-Llama 3.3 70B-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square&logo=windows"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square"/>
</p>

---

## What is Vevo?

Vevo AI Assistant is a Windows desktop AI assistant that lives silently in your system tray and wakes up instantly when you call it — just like Siri, but on your PC. Say **"Vevo"** or press **Ctrl+Space** → a sleek popup appears → type or speak your command → Vevo responds and acts.

---
---

<img width="1918" height="1015" alt="Screenshot 2026-06-09 232325" src="https://github.com/user-attachments/assets/438919cd-c75e-46b7-9f72-e1ef86d3dc23" />

---
## Features

| Feature | Description |
|---|---|
| 🎙 Voice activation | Say "Vevo" to wake it up from anywhere |
| ⌨️ Hotkey | Press `Ctrl+Space` to open the popup |
| 🤖 AI Chat | Powered by Groq — Llama 3.3 70B (free) |
| 🔍 Web Search | DuckDuckGo search + opens browser |
| 📂 App & File Launcher | Open any app or file by name |
| 🌐 Translator | Translate text into 10+ languages |
| 🖥️ System Controls | Volume, screenshot, shutdown, lock, sleep |


</div>
---

## Getting Started

**1. Clone & setup**
```bash
git clone https://github.com/KhaledMohsn/Personal-AI-Assistant-.git
cd Vevo-assistant
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**2. Add your Groq API key** — create `.env`:
```env
GROQ_API_KEY=your_groq_api_key_here
```
Get your free key at → [console.groq.com](https://console.groq.com)

**3. Run**
```bash
python main.py
```

---

## Usage

| Command | Example |
|---|---|
| Wake Vevo | Say **"Vevo"** or press **Ctrl+Space** |
| Web search | "search python tutorials" |
| Open an app | "open discord" |
| Translate | "translate hello to arabic" |
| System control | "volume up" / "screenshot" / "lock" |
| Create file | "create a file called notes" |
| Create folder | "create a folder called projects" |
| Close popup | Press **ESC** |

---

## Tech Stack

Python 3.12 · Groq Llama 3.3 70B · CustomTkinter · SpeechRecognition · DuckDuckGo · deep-translator · pystray · PyInstaller

---

## Configuration

Edit `config/settings.py`:
```python
GROQ_MODEL     = "llama-3.3-70b-versatile"
WAKE_WORD      = "Vevo"
HOTKEY         = "ctrl+space"
LANGUAGE       = "en"
RUN_ON_STARTUP = True
```

## Author
**Khaled Mohsen** 

## License
MIT License

