from pyray import draw_circle
from Constants import * 

class Ball:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.radius = 0.0
        self.speedX, self.speedY = 0.0, 0.0

    def Draw(self) -> None:
        draw_circle(int(self.x), int(self.y), self.radius, BALL_COLOR)

ball = Ball()
ball.x = WIN_WIDTH / 2
ball.y = WIN_HEIGHT / 2
ball.radius = BALL_RADIUS
ball.speedX = BALL_SPEED
ball.speedY = BALL_SPEED

def draw_ball():
    ball.Draw()