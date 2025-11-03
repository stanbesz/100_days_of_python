from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

class Scoreboard(Turtle):

    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-20,280)
        self.update_score()
        
    def update_score(self):
        
        self.write(f"Score: {self.score}",align=ALIGNMENT,font =FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto((0,0))
        self.write("GAME OVER!!!",align=ALIGNMENT,font =FONT)