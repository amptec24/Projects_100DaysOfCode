from turtle import Turtle
FONT_STYLE = ("Courier", 18, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()
