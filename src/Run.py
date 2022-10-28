from Collision import *
from Draw import *
from Movement import *
from Window import *


def run():
    init_window_all()

    while not window_should_close():
        moving_ball()
        moving_paddles()
        collisions()
        state()
        restart()

        Draw()

    unload_all_sound()

    close_audio_device()
    close_window()
