from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()
#  Game instructions: "w" = Forwards, "s" = Backwards, "a" = Counter-Clockwise (left) , "d" = Clockwise (right)
#  and "c" = Clear drawing


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


def clear():
    tim.reset()


screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
