import speech_recognition as sr
from config.logger import get_logger
logger = get_logger(__name__)

class listener:
    
    def __init__(self):

        self.recognizer = sr.Recognizer()


    def listen(self , mic :sr.Microphone ):

        try :
            self.recognizer.adjust_for_ambient_noise(mic , duration= 0.2)
            audio = self.recognizer.listen(mic)
            text = self.recognizer.recognize_google(audio).lower()
            logger.debug(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            logger.debug("Could not understand audio")
            return None
        

    def listen_raw(self, mic: sr.Microphone) :
        try:
            audio = self.recognizer.listen(mic)
            #logger.debug()
            return self.recognizer.recognize_google(audio).lower()
        
        except sr.UnknownValueError:
            return None    




        
        
        
