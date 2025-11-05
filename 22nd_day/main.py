from screen import screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_TOP = 290
SCREEN_BOTTOM = -290
PADDLE_CHECK = 320
PADDLE_HITBOX = 40
END_SCREEN = 400


game_active = True

paddle_r = Paddle((350,0))
paddle_l=Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=paddle_r.move_up,key="Up")
screen.onkeypress(fun=paddle_r.move_down,key="Down")
screen.onkeypress(fun=paddle_l.move_up,key="w")
screen.onkeypress(fun=paddle_l.move_down,key="s")

while game_active:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>SCREEN_TOP or ball.ycor()<SCREEN_BOTTOM:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_r) < PADDLE_HITBOX and ball.xcor() > PADDLE_CHECK or ball.distance(paddle_l) < PADDLE_HITBOX and ball.xcor() < -PADDLE_CHECK:
        ball.bounce_x()

    if ball.xcor() > END_SCREEN:
        ball.return_home()
        score.l_point()

    if ball.xcor()<-END_SCREEN:
        ball.return_home()
        score.r_point()
        

screen.exitonclick()