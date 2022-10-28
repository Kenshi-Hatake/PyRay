from pyray import *

from Ball import *
from Paddle import *
from State import *
from Constants import * 

def Draw():
    begin_drawing()

    clear_background(BLACK)
    
    if TOGGLE_FPS:
        draw_fps(int(WIN_WIDTH / 2 - 50), 10)

    draw_paddles()
    draw_ball()

    winner()

    end_drawing()