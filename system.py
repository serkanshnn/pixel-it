import platform
import os
import winsound

def sound(sound):
    if (platform.system() == "Linux"):
        merged = "aplay "+sound+"&"
        return os.system(merged)
    elif (platform.system() == "Darwin"):
        merged = "afplay "+sound+"&"
        return os.system(merged)
    elif (platform.system() ==  "Windows"):    
        return winsound.PlaySound(sound,winsound.SND_ASYNC)