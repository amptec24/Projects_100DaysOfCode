# Code written by Allen Clarke
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('"Turtle Crossing The Road" game by Allen Clarke')
screen.tracer(0)

# Create object from class
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Control for the turtle
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    # This slow down the speed of the car moving
    time.sleep(0.1)
    # Update screen as screen animation is turned off
    screen.update()
    # Move car across the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect the turtle reach the other side
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()
