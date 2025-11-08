import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

TURTLE_HITBOX = 25
GAME_SPEED = 0.1

turtle = Player()
score = Scoreboard()

def check_collision(cars,turtle):
        min_dist =  10000
        for car in cars.car_list:
            if min_dist>car.distance(turtle):
                min_dist = car.distance(turtle)

        if min_dist<TURTLE_HITBOX:
             return True
        else:
             return False
        
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=turtle.move_up,key="w")
screen.onkeypress(fun=turtle.move_down,key="s")
screen.onkeypress(fun=turtle.move_left,key="a")
screen.onkeypress(fun=turtle.move_right,key="d")

cars = CarManager()
screen.update()
game_is_on = True

while game_is_on:

    time.sleep(GAME_SPEED)
    cars.move_cars()
    screen.update()

    if check_collision(cars,turtle):
        score.game_over()
        game_is_on = False

    if turtle.check_finished():
        turtle.reset_turtle()
        cars.update_speed()
        score.increase_score()


screen.exitonclick()