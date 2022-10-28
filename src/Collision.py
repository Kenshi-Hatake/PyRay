from Ball import *
from Paddle import *
from Sounds import *


def collisions():
    if check_collision_circle_rec(Vector2(ball.x, ball.y), ball.radius, leftPaddle.GetRect()):
        play_sound(ballTouchedSound)
        if ball.speedX < 0:
            ball.speedX *= PADDLE_BALL_BOOST
            ball.speedY = (ball.y - leftPaddle.y) / (leftPaddle.height / 2) * ball.speedX

    if check_collision_circle_rec(Vector2(ball.x, ball.y), ball.radius, rightPaddle.GetRect()):
        play_sound(ballTouchedSound)
        if ball.speedX > 0:
            ball.speedX *= PADDLE_BALL_BOOST
            ball.speedY = (ball.y - rightPaddle.y) / (rightPaddle.height / 2) * (-ball.speedX)