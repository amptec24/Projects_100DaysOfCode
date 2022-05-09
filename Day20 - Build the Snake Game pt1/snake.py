from turtle import Turtle
GAME_STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head_of_snake = self.segments[0]

    def create_snake(self):
        for position in GAME_STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head_of_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    def left(self):
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)

    def down(self):
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)

    def right(self):
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)
