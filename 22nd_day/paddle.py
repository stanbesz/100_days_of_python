from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,pos: tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(pos)

    def move_up(self):
        self.goto(self.get_pos_x(),self.get_pos_y()+20)

    def move_down(self):
        self.goto(self.get_pos_x(),self.get_pos_y()-20)

    def get_pos_x(self):
        return self.xcor()
    
    def get_pos_y(self):
        return self.ycor()