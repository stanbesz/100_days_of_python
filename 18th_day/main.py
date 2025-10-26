from turtle import Turtle,Screen
import turtle as t
from random import randint,choice
colors = []

for i in range(10):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

timmy = Turtle()
screen = Screen()
screen.screensize(2000,1000)
timmy.shape("arrow")
timmy.color("DarkOrchid")

flag_stop = False

def handler():
    global flag_stop
    if not flag_stop:
        flag_stop = True
    elif flag_stop:
        flag_stop = False
    timmy.end_poly()


start_pos = timmy.pos()
timmy.width(2)
screen.onkey(handler,"space")
screen.listen()

def draw_shapes():
	sides = 3
	for i in range(0,len(colors)):
		timmy.color(colors[i])
		for side in range(sides):
			timmy.forward(100)
			timmy.right(360/sides)
		sides+=1

timmy.speed("fastest")

def random_walk():
	rotations = [0,90,180,270]
	while not flag_stop:
		color_tuple = random_color()
		timmy.forward(30)
		timmy.setheading(choice(rotations))
		timmy.color(color_tuple)

def spirograph():
	circle_amount = 360 / 100
	for i in range(0,101):
		timmy.circle(100)
		timmy.setheading(circle_amount*i)
		color_tuple = random_color()
		timmy.color(color_tuple)

spirograph()

screen.exitonclick()