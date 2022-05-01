from turtle import Turtle
SCORE_STYLE = ("Courier", 60, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player = 0
        self.r_player = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_player, align=ALIGNMENT, font=SCORE_STYLE)
        self.goto(100, 200)
        self.write(self.r_player, align=ALIGNMENT, font=SCORE_STYLE)

    def l_add_point(self):
        self.l_player += 1
        self.update_scoreboard()

    def r_add_point(self):
        self.r_player += 1
        self.update_scoreboard()
