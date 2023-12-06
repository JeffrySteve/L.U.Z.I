import pyttsx3
import speech_recognition as sr
import eel
import os
import subprocess
import time
import wikipedia
import webbrowser
import cv2
from requests import get
from engine.features import *


#text->Voice
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 180)
    print(voices)
    engine.say(text)
    engine.runAndWait()
    
 
#Voice->text 
@eel.expose  
def TakeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('listening.....')
        eel.DisplayMessage('listening.....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source,10 ,6)
        
    try:
        print("recognizing")
        eel.DisplayMessage('recognizing.....')

        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        
        #To open Notepad
        if "open notepad" in query.lower():
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
        #To Open Command Prompt
        elif "open command prompt" in query.lower():
            os.system("start cmd") 
            eel.DisplayMessage("Opening Command Prompt...", 5)
        
        #To Open Camera
        elif "open camera" in query.lower():
            cap=cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()  
        
        #To Find IP Address    
        elif "find my current ip address" in query.lower():
             ip = get('https://api.ipify.org').text
             speak(f"your IP address is {ip}")
        
        #To search anyhting in Wikipedia     
        elif "wikipedia" in query.lower():
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            eel.DisplayMessage(results)
            speak("accoeding to wikipedia")
            speak(results)
         
        #To open youtube    
        elif "open youtube" in query.lower():
            webbrowser.open("www.youtube.com")
        
        #To Search something on google    
        elif "open google" in query.lower():
            speak("Sir, what should i search on google")
            search = TakeCommand().lower()
            webbrowser.open(f"{search}")    
        
         
         
         
               
        else:
            pass
        
        eel.ShowHood()
        
    except Exception as e:  
        speak("say that again")
        return ""   
    return query.lower()

#Fucntion call

    
#Open Browser    
   