import speech_recognition as sr
from DataTrain import  DataTrain
import pyttsx3
import time


class VoiceRecognisation:

    def speech(self, string):

        engine = pyttsx3.init()
        query = string
        r = sr.Recognizer()
        with sr.Microphone() as source:
            rate = engine.getProperty('rate')
            engine.setProperty(rate, 1)
            engine.setProperty('voice','HKEY_LOCAL_MACHINE/SOFTWArE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_ZIRA_11.0')
            engine.runAndWait()
            time.sleep(2)
            engine.say(string)
            print(string)
            engine.runAndWait()
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))

            except:
                print("Sorry i could not recognised your voice")
                text = VoiceRecognisation.speech("hello",query)

            text = text.title()
            FilteredQuery=DataTrain.traindata("Data Train",text)
            str_join = " ".join(FilteredQuery)
            print(str_join)
        return str_join
