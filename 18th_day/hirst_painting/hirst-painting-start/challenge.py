from cologram_data import rgb_colors
from turtle import Turtle,Screen
import turtle as t
from random import randint,choice

t.colormode(255)

start_pos_x = -250
start_pos_y = -250

timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
timmy.up()
timmy.setx(start_pos_x)
timmy.sety(start_pos_y)

column_num = 0
for i in range(10):
    for col in range(10):
        timmy.color(choice(rgb_colors))
        timmy.down()
        timmy.dot(20)
        timmy.up()
        timmy.forward(50)
    column_num+=1
    timmy.setx(start_pos_x)
    timmy.sety(start_pos_y+50*column_num)
    
print(rgb_colors)


