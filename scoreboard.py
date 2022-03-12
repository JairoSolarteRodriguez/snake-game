from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'italic')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('#fff')
        self.updateScore()
        self.hideturtle()

    def updateScore(self, gameover=False):
        message = 'Game Over' if gameover else f'Score: {self.score}'
        self.write(message, font=FONT, align=ALIGN)

    def increaseScore(self):
        self.clear()
        if self.score > 2:
            self.score += 2
        elif self.score > 20:
            self.score += 3
        else:
            self.score += 1
        self.updateScore()

    def gameOver(self):
        gameover = True
        self.clear()
        self.score += 1
        self.updateScore(gameover)