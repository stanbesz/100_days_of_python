from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    start_position = [(0,0),(-20,0),(-40,0)]
    snake_segments:list = []
    head = 0

    def __init__(self):
        for pos in self.start_position:
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.up()
            segment.setposition(pos)
            self.snake_segments.append(segment)
        self.head = self.snake_segments[0]

    def move(self):
        for seg_num in range(len(self.snake_segments)-1,0,-1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)