from turtle import Turtle
SIGNATURE = ("Courier", 10, "normal")
SIGNATURE_ALIGNMENT = "right"


class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(16):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.goto(380, - 280)
        self.write("Code by Allen Clarke", align=SIGNATURE_ALIGNMENT, font=SIGNATURE)


