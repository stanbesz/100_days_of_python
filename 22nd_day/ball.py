from turtle import Turtle

SCREEN_TOP = 290
SCREEN_BOTTOM = -290


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.speed("slowest")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.goto(0,0)

    def move(self):
        new_y = self.ycor()+self.y_move
        new_x = self.xcor()+self.x_move
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed *= 0.9
    
    def bounce_y(self):
        self.y_move*=-1

    def return_home(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()