# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# Each line must be a different color
from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# My Solution for the Challenge
list_of_side = [3, 4, 5, 6, 7, 8, 9, 10]
list_leght = len(list_of_side)
continue_drawing = True
amount_of_side = 0

while continue_drawing:
    num_sides = list_of_side[amount_of_side]
    angle = 360 / num_sides
    tim.color(random.choice(colours))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
    amount_of_side += 1
    if amount_of_side == list_leght:
        continue_drawing = False

# # App Brewery Solution
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()