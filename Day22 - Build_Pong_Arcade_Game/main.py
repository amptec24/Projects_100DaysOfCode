# Code written by Allen Clarke
from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
from screen_divide import Divider
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('The famous "Pong" game by Allen Clarke')
# Turn off-screen animation
screen.tracer(0)

divider = Divider()
r_bar = Bar((350, 0))
l_bar = Bar((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_bar.go_up, "Up")
screen.onkey(r_bar.go_down, "Down")
screen.onkey(l_bar.go_up, "w")
screen.onkey(l_bar.go_down, "s")

game_is_on = True

while game_is_on:
    # This slow down the speed of the ball moving
    time.sleep(ball.move_speed)
    # Update screen as screen animation is turned off
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce on the y-axis
        ball.bounce_y()

    # Detect collision with right bar.
    if ball.distance(r_bar) < 50 and ball.xcor() > 320 or ball.distance(l_bar) < 50 and ball.xcor() < -320:
        # Needs to bounce on the x-axis
        ball.bounce_x()

    # Detect when the right bar misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_add_point()

    # Detect when the light bar misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_add_point()

screen.exitonclick()
