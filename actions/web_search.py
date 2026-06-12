import webbrowser
import speech_recognition as sr
import urllib.parse
from config.logger import get_logger

logger = get_logger(__name__)

class  WebSearching:
    def __init__(self,speaker, listener):
        self.speaker = speaker
        self.listener = listener


    def search(self, command:str):
        logger.info(f"Web search: {command}")

        if not command:
            self.speaker.say("What do you want to search for?")

            with sr.Microphone() as mic :
               
               command = self.listener.listen_raw(mic)

            if not command:
                self.speaker.say("I didn't catch that")  
                print("I didn't catch that!")
                return  
            
        url = f"https://www.google.com/search?q={urllib.parse.quote(command)}"
        webbrowser.open(url)
        self.speaker.say(f"Searching for {command}")



