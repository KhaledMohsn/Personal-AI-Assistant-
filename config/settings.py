import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"
ASSISTANT_NAME = "Vevo"
WAKE_WORD = "vevo"
HOTKEY = "ctrl+space"
APP_NAME = "Vevo AI Assistant"
APP_VERSION = "1.0.0"
RUN_ON_STARTUP = True
MINIMIZE_TO_TRAY = True
VOICE_ENABLED = True
SYSTEM_PROMPT = "You are a helpful assistant named Vevo."
USER_NAME = "khaled"

