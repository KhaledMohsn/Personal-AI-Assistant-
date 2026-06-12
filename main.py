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

from config.settings import USER_NAME
class Assistant:

    def __init__(self):

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

                    print(f"Heard : {text}")

                    if WAKE_WORD in text :
                        self.ui.set_active()
                        self.speaker.say(f"Yes {USER_NAME} how can I help you?")

                    with sr.Microphone() as mic :
                        command = self.listener.listen_raw(mic)  

                    if not command:
                        self.ui.set_idle()
                        continue

                    intent = get_intent(self.client, GROQ_MODEL, command)
                    action = intent["action"]
                    query = intent["query"]

                    if action == "exit":
                        self.speaker.say(f"Goodbye {USER_NAME}")
                        self.ui.destroy()

                    elif action == "search":
                        self.web_search.search(query)

                    if action == "create_file":
                        self.actions.create_file()   

                    elif action == "open_app":
                      self.open_app.open_app(query)    

                    else:
                        response = self.ask_groq(query)
                        self.speaker.say(response)        



                    self.ui.set_idle()

if __name__ == "__main__":

    Assistant()
                    