from playsound import playsound
import eel
import datetime
import subprocess
from engine.command import*

#Playing assistant sound function
@eel.expose
def PlayAssistantSound():
    music_dir = "www\\assests\\audio\\start_sound.mp3"
    playsound(music_dir)
       
#Opening greet 
@eel.expose 
def wish():
    hour = datetime.datetime.now().hour   
    
    if hour>=0 and hour<=12:
        speak("Good  Morning")
    elif  hour>=12 and hour<=18:
        speak("Good  Afternoon")  
    else:
        speak("Good Evening")
    speak("Hi sir, I am Loossy. How can I help you today")    
    

      
          
        