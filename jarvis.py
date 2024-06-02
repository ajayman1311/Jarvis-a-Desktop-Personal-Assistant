#Project jarvis
import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import pyautogui
import requests
from bs4 import BeautifulSoup


from gui import play_gif
play_gif
#Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour<12:
        speak("good morning sir. what a glorios morning.")
    elif hour>=12 and hour<18:
        speak("good afternoon sir.") 
    elif hour>=18 and hour<21:
        speak("good evening sir.")     
    else:
        speak("I think you should rest sir, I hope you enjoyed your day today.")  

# def googlesearch(self, query):
#             query = query.replace("jarvis","")
#             query = query.replace("google","")
#             URL = "https://www.youtube.com/results?search_query=" + query
#             headers = {
#             'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
#             }
#             info = requests.get(URL, headers = headers)
#             soupify = BeautifulSoup(info.content, features='html.parser')
#             results = soupify.find(class_= 'Z0LcW t2b5Cf CfV8xf').getText
#             ui.terminalPrint(results)   # type: ignore
#             speak(results)        

#now convert audio to text
# 
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

#for main function                               
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "open youtube" in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")
            
        elif 'open github' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.github.com")
            speak("opening github")  
            
        elif 'open facebook' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook") 
            
        elif 'open spotify' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://open.spotify.com")
            speak("opening facebook")
            
        elif 'open google cloud skills boost' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.cloudskillsboost.google/")
            speak("opening facebook")    
                     
        elif 'open instagram' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")   
             
        elif 'open google' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open sheets' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://docs.google.com/spreadsheets/d/1IPwCu8R1k-V2n_Mq7tLzI-1FLfV7EaVIXM-4TsYT5k8/edit#gid=0")
            speak(" Sheets opening")
        elif 'open docs' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://docs.google.com/document/d/142ONaNO7PBFWYliMKSi1n1K9ysPWt5dixQBx5duq8Wk/edit")
            speak("Docs opening sir")  
        elif 'open slides' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://docs.google.com/presentation/d/1lK8ZLCoD1MMl2INxCrtARlbFhNjXCj5Sx3R-n0c0Cdc/edit#slide=id.p")
            speak("opening yahoo")      
            
        elif 'open gmail' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query or 'open shopping website' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   
        
        elif "today's temperature" in query:
             query = query.replace("jarvis","")
             search = "temperature in gorakhpur"
             url = f"https://www.google.com/search?q={search}"
             r  = requests.get(url)
             data = BeautifulSoup(r.text,"html.parser")
             temp = data.find("div", class_ = "BNeawe").text
             speak(f"current{search} is {temp}")
        elif "today's weather" in query:
            query = query.replace("jarvis","")
            search = "weather in gorakhpur"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        
        elif 'open whatsapp' in query:
            query = query.replace("jarvis","")
            webbrowser.open("https://web.whatsapp.com/")
            speak("opening sir")
                
        elif "translate" in query:
            from translator import translategl
            query = query.replace("jarvis","")
            query = query.replace("translate","")
            translategl(query)   
     
        
        elif "open" in query:   #EASY METHOD
           query = query.replace ("open","")
           query = query.replace("jarvis","")
           pyautogui.press("super")
           pyautogui.typewrite(query)
           pyautogui.sleep(2)
           pyautogui.press("enter")  
        # elif "open" in query:
        #    from openclose import openappweb
        #    openappweb(query)
        
        elif "time batana" in query:
               query = query.replace("jarvis","")
               strTime = datetime.datetime.now().strftime("%H:%M")    
               speak(f"Sir, the time is {strTime}")       
            
        elif "close" in query:
           from openclose import closeappweb
           closeappweb(query)    
            
        elif "google" in query:
           from search import searchGoogle
           searchGoogle(query)
        elif "youtube" in query:
           from search import searchYoutube
           searchYoutube(query)   
        elif "wikipedia" in query:
           from search import searchWikipedia
           searchWikipedia(query)  
           
        elif "send message" in query:
            query = query.replace("jarvis","")
            from Whatsapp import sendMessage
            sendMessage() 

              
            
        # elif "search" in query:
        #     query = query.replace("jarvis","")
        #     self.googlesearch(query)
            
        elif 'pause' in query:
            query = query.replace("jarvis","")
            pyautogui.press("k")
            speak("video paused")
            
        elif 'play' in query:
            query = query.replace("jarvis","")
            pyautogui.press("k")
            speak("video played")
            
        elif 'mute' in query:
            query = query.replace("jarvis","")
            pyautogui.press("m")
            speak("mute")   
        
        elif 'unmute' in query:
            query = query.replace("jarvis","")
            pyautogui.press("m")
            speak("unmuted")     
            
        elif 'volume up' in query:
            query = query.replace("jarvis","")
            from keyboard import volumeup
            speak("volume up")    
            
        elif 'volume down' in query:
            query = query.replace("jarvis","")
            from keyboard import volumedown
            speak("volumedown")    
            
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            speak("You told me to"+rememberMessage)
            remember = open("remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("remember.txt","r")
            speak("You told me" + remember.read())
            
        elif "i am tired" in query:
            speak("Playing your favourite songs, sir")
            a = (1,2,3,4,5) 
            b = random.choice(a)
            if b==1:
                webbrowser.open("https://www.youtube.com/watch?v=qcC1i4ENMMs")    
            elif b==2:
                webbrowser.open("https://www.youtube.com/watch?v=s-bZD3O3P80")
            elif b==3:
                webbrowser.open("https://www.youtube.com/watch?v=EFqkHIMbhQg")
            elif b==4:
                webbrowser.open("https://www.youtube.com/watch?v=BNfAf4To73c")
            elif b==5:
                webbrowser.open("https://www.youtube.com/watch?v=orYf6VDtj_k")    
                
            
        elif 'music from pc' in query or "music" in query:
            query = query.replace("jarvis","")
            speak("ok i am playing music")
            music_dir = 'E:/music/New music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
        elif 'video from pc' in query or "video" in query:
            query = query.replace("jarvis","")
            speak("ok i am playing videos")
            video_dir = 'E:/movies'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))  
        elif 'good bye' in query:
            query = query.replace("jarvis","")
            speak("good bye")
            exit()
        elif "shutdown" in query:
            query = query.replace("jarvis","")
            speak("shutting down")
            os.system('shutdown -s') 
        elif "how are you" in query or "how r u" in query:
            query = query.replace("jarvis","")
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('Sir, Always be happy..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            query = query.replace("jarvis","")
            ans_m = " For your information Ajay Kumar Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            query = query.replace("jarvis","")
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello Jarvis" in query:
            query = query.replace("jarvis","")
            hel = "Hello Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            query = query.replace("jarvis","")
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            query = query.replace("jarvis","")
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 
        elif query == 'none':
            continue 
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
        # else:
        #     temp = query.replace(' ','+')
        #     g_url="https://www.google.com/search?q="    
        #     res_g = 'Searching.....'
        #     print(res_g)
        #     speak(res_g)
        #     webbrowser.open(g_url+temp)
                                            