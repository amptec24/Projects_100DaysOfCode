from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
tim = Turtle()
tim.shape("turtle")

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()