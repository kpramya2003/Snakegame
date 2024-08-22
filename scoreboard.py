from turtle import Turtle
ALIGN='center'
FONT=('Arial',15,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,275)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align=ALIGN, font=FONT)
    def update_score(self):
        self.clear()
        self.write(f"score : {self.score}",align=ALIGN,font=FONT)