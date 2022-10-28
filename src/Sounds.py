import os
from pyray import load_sound, init_audio_device, stop_sound, unload_sound
from pygame import mixer 

mixer.init()
init_audio_device()

ballTouchedSound = load_sound(os.path.join("assets", "touched.wav"))
ballMissedSound = load_sound(os.path.join("assets", "missed.wav"))
ballTouchedWallSound = load_sound(os.path.join("assets", "wallTouched.wav"))

playBackgroundMusic = True 
if playBackgroundMusic:
    mixer.music.load(os.path.join("assets", "background.mp3"))
    mixer.music.play(-1, 0, 0)

def stop_all_sounds():

    stop_sound(ballTouchedSound)
    stop_sound(ballMissedSound)
    stop_sound(ballTouchedWallSound)

    
def unload_all_sound():

    unload_sound(ballTouchedSound)
    unload_sound(ballMissedSound)
    unload_sound(ballTouchedWallSound)