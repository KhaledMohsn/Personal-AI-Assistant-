import speech_recognition as sr

class listener:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()


    def listen(self , mic :sr.Microphone ):

        try :
            self.recognizer.adjust_for_ambient_noise(mic , duration= 0.2)
            audio = self.recognizer.listen(mic)
            return self.recognizer.recognize_google(audio).lower()
        
        except sr.UnknownValueError:
            return None
        

    def listen_raw(self, mic: sr.Microphone) :
        try:
            audio = self.recognizer.listen(mic)
            return self.recognizer.recognize_google(audio).lower()
        
        except sr.UnknownValueError:
            return None    




        
        
        
