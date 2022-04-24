# Make turtle make randon walk increase the line thickness and choose random colors
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.pensize(10)
tim.speed(0)
# how to Generate Randon RGB colours
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb_colour = (r, g, b)
    return random_rgb_colour


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]

for x in range(300):
    #tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(35)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()