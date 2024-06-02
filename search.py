from plistlib import UID
import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import wolframalpha
import requests
from bs4 import BeautifulSoup
import os


def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)    
    
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("")
        print("......") 
        return "none"
    return text


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,2)
            speak(result)

        except:
            speak("")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("play","")
        query = query.replace("jarvis","")
        query = query.replace("jarvis play","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")
              

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("")
        print(results)
        speak(results)


    

