from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

EDGE = 290

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.right,key="Right")
screen.onkey(snake.left,key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #distance from points
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > EDGE or snake.head.xcor() < -EDGE or snake.head.ycor()>EDGE or snake.head.ycor()<-EDGE:
        game_is_on = False
        score.game_over()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()


screen.exitonclick()