from turtle import Turtle

STRETCH_WID = 4
STRETCH_LEN = 0.5
SHAPE = "square"
COLOR = "white"


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(STRETCH_WID, STRETCH_LEN)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


