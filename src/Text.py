from pyray import draw_text, YELLOW 
from Constants import * 


class Text:

    def __init__(self) -> None:
        self.text = ""
        self.width, self.height = 0, 0
        self.fontSize = 0
    
    def Draw(self) -> None:
        draw_text(self.text, int(self.width), int(self.height), int(self.fontSize), YELLOW)


winnerText = Text()
winnerText.text = ""
winnerText.width = 150
winnerText.height = WIN_HEIGHT / 2 - 30
winnerText.fontSize = 60