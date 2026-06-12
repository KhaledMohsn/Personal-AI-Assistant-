import os
import sys
import speech_recognition as sr
from dotenv import load_dotenv
from groq import Groq

from config.settings import WAKE_WORD, GROQ_MODEL, SYSTEM_PROMPT
from voice import Speaker, listener
from ui import AssistantUI
from actions import CreateAction , WebSearching, OpenAppAction
load_dotenv()
from actions import get_intent
from config.logger import get_logger
logger = get_logger(__name__)

from config.settings import USER_NAME
class Assistant:

    def __init__(self):
        logger.info("Initializing Assistant")
        self.speaker = Speaker()
        self.listener = listener()
        self.ui = AssistantUI()
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.actions = CreateAction(self.speaker, self.listener)
        self.web_search = WebSearching(self.speaker, self.listener)
        self.open_app = OpenAppAction(self.speaker, self.listener)
        self.ui.start(self.run_assistant)
        

#==========================================================

    def ask_groq(self, text:str ): 
        logger.debug(f"Sending to Groq: {text}")

        response = self.client.chat.completions.create(

            model= GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Mako."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
        
#==============================================================
   

    def run_assistant(self):

        while True:
                
                with sr.Microphone() as mic:

                    text = self.listener.listen(mic)
                    if not text :
                        continue
                    logger.debug(f"Heard: {text}")

                    print(f"Heard : {text}")

                    if WAKE_WORD in text :
                        logger.info("Wake word detected")
                        self.ui.set_active()
                        self.speaker.say(f"Yes {USER_NAME} how can I help you?")
                        

                    with sr.Microphone() as mic :
                        command = self.listener.listen_raw(mic)  

                    if not command:
                        self.ui.set_idle()
                        continue
                    logger.info(f"Command received: {command}")

                    intent = get_intent(self.client, GROQ_MODEL, command)
                    action = intent["action"]
                    query = intent["query"]

                    if action == "exit":
                        logger.info("Triggering exit")
                        self.speaker.say(f"Goodbye {USER_NAME}")
                        self.ui.destroy()

                    elif action == "search":
                        logger.info(f"Triggering search: {query}")
                        self.web_search.search(query)

                    if action == "create_file":
                        logger.info("Triggering create_file action")
                        self.actions.create_file()   

                    elif action == "open_app":
                      logger.info(f"Triggering open_app: {query}")
                      self.open_app.open_app(query)    

                    else:
                        logger.info("asking groq")
                        response = self.ask_groq(query)
                        self.speaker.say(response)        



                    self.ui.set_idle()

if __name__ == "__main__":

    Assistant()
                    