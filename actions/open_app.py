import subprocess
from config.logger import get_logger

logger = get_logger(__name__)

APPS = {

    "notepad": "notepad",
    "vscode": "code",
    "calculator": "calc",
    "word": "winword",
    "excel": "excel",
    "spotify": "spotify",
    "discord": "discord"
}

class OpenAppAction:
    def __init__(self, speaker, listener):
        self.speaker = speaker
        self.listener = listener

    def open_app(self, app_name: str):

        logger.info(f"Attempting to open: {app_name}")

        app_name = app_name.lower().strip()

        if app_name not in APPS:
            self.speaker.say(f"I don't know how to open {app_name}")
            return

        try:
            logger.info(f"Opened: {app_name}")
            subprocess.Popen(APPS[app_name], shell=True)
            self.speaker.say(f"Opening {app_name}")
            
        except Exception:
            logger.error(f"Failed to open: {app_name}")
            self.speaker.say(f"I couldn't open {app_name}")