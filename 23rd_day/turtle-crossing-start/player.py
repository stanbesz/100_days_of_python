from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.showturtle()
        pass

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-MOVE_DISTANCE)

    def move_left(self):
        self.goto(self.xcor()-MOVE_DISTANCE,self.ycor())

    def move_right(self):
        self.goto(self.xcor()+MOVE_DISTANCE,self.ycor())

    def check_finished(self):
        res = self.ycor()>FINISH_LINE_Y
        return res
    
    def reset_turtle(self):
        self.goto(STARTING_POSITION)