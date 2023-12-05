from playsound import playsound
import eel

# Playing assistant sound function

@eel.expose
def PlayAssistantSound():
    music_dir = "www\\assests\\audio\\start_sound.mp3"
    playsound(music_dir)