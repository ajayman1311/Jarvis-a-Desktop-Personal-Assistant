from fnmatch import translate
from time import sleep
from googletrans import Translator
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeComm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognising.")
        input_lang = "en" 
        text = r.recognize_google(audio,language=input_lang)
        print(text)
    except Exception:                #For Error handling
        speak("")
        print("......") 
        return "none"
    return text

def translategl(query):
    output_lang = "hi"
    # print(googletrans.LANGUAGES)
    translator = Translator()
    # speak("Choose the language in which you want to translate")  
    text_to_translate = translator.translate(query,src = "auto",dest=output_lang)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        print(text_to_translate.text)
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")
