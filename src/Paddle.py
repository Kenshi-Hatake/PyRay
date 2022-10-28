from Constants import *


class Paddle:

    def __init__(self) -> None:
        self.x, self.y = 0, 0
        self.speed = PADDLE_SPEED
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = 0
        self.wins = 0
        self.lives = PADDLE_LIVES
        self.livePosX, self.livePosY = 0, 0

    def GetRect(self) -> Rectangle:
        return Rectangle(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    def Draw(self) -> None:
        draw_rectangle_rec(self.GetRect(), self.color)
        draw_text(f"Lives: {str(self.lives)}", self.livePosX, self.livePosY, 30, WHITE)
        if self.y < 50:
            self.y = 50
        if self.y > get_screen_height() - 50:
            self.y = get_screen_height() - 50


leftPaddle = Paddle()
leftPaddle.x = 50
leftPaddle.y = WIN_HEIGHT / 2
leftPaddle.color = LEFT_PADDLE_COLOR
leftPaddle.livePosX, leftPaddle.livePosY = 10, 10

rightPaddle = Paddle()
rightPaddle.x = WIN_WIDTH - 50
rightPaddle.y = WIN_HEIGHT / 2
rightPaddle.color = RIGHT_PADDLE_COLOR
rightPaddle.livePosX, rightPaddle.livePosY = WIN_WIDTH - 120, 10


def draw_paddles():
    leftPaddle.Draw()
    rightPaddle.Draw()
