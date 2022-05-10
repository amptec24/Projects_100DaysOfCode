# Draw a spirograph
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_colour = (r, g, b)
    return rgb_colour


for _ in range(73):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)

# # ******************************************************
# # App Brewery Solution
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)
# # *******************************************************

screen = t.Screen()
screen.exitonclick()
