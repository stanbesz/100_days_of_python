from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()
        self.score = 0

    def update_score(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level: {self.score}",align="center",font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)

    pass
