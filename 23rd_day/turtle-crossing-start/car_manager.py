from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 25
MOVE_INCREMENT = 10
OUT_OF_SCREEN = 320
SCREEN_SIZE = 280

class CarManager:

    speed_increase = MOVE_INCREMENT
    car_list:list = []
    car_amount = 30

    def __init__(self):
        self.create_cars()
        pass

    def create_cars(self):
        for ind in range(0,self.car_amount):
            self.add_car()

    def move_cars(self):
        for ind in range(0,len(self.car_list)-1):
            self.car_list[ind].goto(self.car_list[ind].xcor()-self.speed_increase,self.car_list[ind].ycor())
            if self.car_list[ind].xcor() < -OUT_OF_SCREEN and len(self.car_list)<=self.car_amount:
                self.car_list[ind].clear()
                self.car_list.pop(ind)
                self.add_car_start()

    def add_car(self):
            car = Turtle()
            car.up()
            car.shape("square")
            car.shapesize(1,2)
            car.color(random.choice(COLORS))
            car.setposition(random.randint(-SCREEN_SIZE,SCREEN_SIZE),random.randint(-SCREEN_SIZE+STARTING_MOVE_DISTANCE,SCREEN_SIZE))
            self.car_list.append(car)

    def add_car_start(self):
            car = Turtle()
            car.up()
            car.shape("square")
            car.shapesize(1,2)
            car.color(random.choice(COLORS))
            car.setposition(OUT_OF_SCREEN,random.randint(-SCREEN_SIZE+STARTING_MOVE_DISTANCE,SCREEN_SIZE))
            self.car_list.append(car)

    def update_speed(self):
        self.speed_increase=self.speed_increase+int(MOVE_INCREMENT/2)

    pass
