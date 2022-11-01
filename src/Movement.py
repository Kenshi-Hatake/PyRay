from Constants import * 
from Ball import *
from Paddle import *
from Sounds import *


def moving_ball():
    # BALL MOVING
    ball.x += ball.speedX * get_frame_time()
    ball.y += ball.speedY * get_frame_time()

    # BALL COLLISION TOP/BOTTOM OF WINNDOW
    if ball.y > WIN_HEIGHT:
        play_sound(ballTouchedWallSound)
        ball.y = WIN_HEIGHT
        ball.speedY *= -1
    if ball.y < 0:
        play_sound(ballTouchedWallSound)
        ball.y = 0
        ball.speedY *= -1


def moving_paddles():
    # MOVING THE LEFT PADDLE
    if is_key_down(KeyboardKey.KEY_W):
        leftPaddle.y -= leftPaddle.speed * get_frame_time()
    if is_key_down(KeyboardKey.KEY_S):
        leftPaddle.y += leftPaddle.speed * get_frame_time()

    # MOVING THE RIGHT PADDLE
    if is_key_down(KeyboardKey.KEY_UP):
        rightPaddle.y -= rightPaddle.speed * get_frame_time()
    if is_key_down(KeyboardKey.KEY_DOWN):
        rightPaddle.y += rightPaddle.speed * get_frame_time()
