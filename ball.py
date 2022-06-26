from turtle import Turtle
from random import randint

SHAPE = "circle"
COLOR = "white"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(0, 0)
        self.initial_heading = randint(-80, 80)
        self.setheading(self.initial_heading)
        self.move_speed = 1.2

    def move(self):
        self.forward(self.move_speed)

    def bounce_y(self):
        self.setheading(-self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self):
        self.move_speed += 0.01

