# Code written by Allen Clarke

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My 80's Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
# Up key is Case Sensitive.
# Function inside other function for screen is written without () ig function(function, text)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
