from Ball import *
from Paddle import *
from Sounds import *
from Text import *


def state():
    if ball.x < 0:
        play_sound(ballMissedSound)
        if rightPaddle.lives > 0 >= leftPaddle.lives:
            winnerText.text = "Right Player Wins"
            playBackgroundMusic = False
            stop_all_sounds()
        else:
            rightPaddle.wins += 1
            leftPaddle.lives -= 1
            ball.x = WIN_WIDTH / 2
            ball.y = WIN_HEIGHT / 2
            ball.speedX = BALL_SPEED
            ball.speedY = BALL_SPEED

    if ball.x > WIN_WIDTH:
        play_sound(ballMissedSound)
        if leftPaddle.lives > 0 >= rightPaddle.lives:
            winnerText.text = "Left Player Wins"
            playBackgroundMusic = False
            stop_all_sounds()
        else:
            leftPaddle.wins += 1
            rightPaddle.lives -= 1
            ball.x = WIN_WIDTH / 2
            ball.y = WIN_HEIGHT / 2
            ball.speedX = BALL_SPEED
            ball.speedY = BALL_SPEED


def restart():
    if winnerText.text != "" and is_key_pressed(KeyboardKey.KEY_SPACE):
        leftPaddle.lives = PADDLE_LIVES
        rightPaddle.lives = PADDLE_LIVES
        ball.x = WIN_WIDTH / 2
        ball.y = WIN_HEIGHT / 2
        ball.speedX = BALL_SPEED
        ball.speedY = BALL_SPEED
        winnerText.text = ""


def winner():
    if winnerText.text == "Right Player Wins":
        winnerText.Draw()
        stop_all_sounds()
    if winnerText.text == "Left Player Wins":
        winnerText.Draw()
        stop_all_sounds()
