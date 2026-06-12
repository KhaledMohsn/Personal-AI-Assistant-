import speech_recognition as sr
import os

LOCATIONS = {
    "desktop": os.path.normpath(os.path.expanduser("~/Desktop")),
    "documents": os.path.normpath(os.path.expanduser("~/Documents")),
    "downloads": os.path.normpath(os.path.expanduser("~/Downloads")),
}

class CreateAction:

    def __init__(self, speaker, listener, default_dir="created_files"):
        self.speaker = speaker
        self.listener = listener
        self.default_dir = default_dir
        os.makedirs(self.default_dir, exist_ok=True)

    def create_file(self):
        # 1. Get file name
        self.speaker.say("What is the name of the file?")
        with sr.Microphone() as mic:
            name = self.listener.listen_raw(mic)

        if not name:
            self.speaker.say("I didn't catch that")
            return

        # 2. Get location
        self.speaker.say("Where should I save it? Desktop, Documents, or Downloads?")
        with sr.Microphone() as mic:
            location = self.listener.listen_raw(mic)

        folder = LOCATIONS.get(location, self.default_dir) if location else self.default_dir
        if folder == self.default_dir:
            os.makedirs(folder, exist_ok=True)

        # 3. Create the file
        path = os.path.join(folder, f"{name}.txt")
        with open(path, "w") as f:
            f.write("")

        self.speaker.say(f"File {name} has been created in {location or 'the default folder'}!")