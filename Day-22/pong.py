# Pong game

import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Ww 20 h 100 X POS 350 Y 0

screen = Screen()
screen.setup(800, 600, 0, 0)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.up, "w")
screen.onkeypress(right_paddle.down, "s")

screen.onkeypress(left_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect rebound
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Multipy by -1 to change 'y' direction
        ball.rebound_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        # Multipy by -1 to change 'x' direction
        ball.rebound_x()

    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()


