from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.current_y = 0
        self.current_x = position
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")
        self.goto(position, self.current_y)

    def up(self):
        self.current_y += 20
        self.goto(self.current_x, self.current_y)

    def down(self):
        self.current_y -= 20
        self.goto(self.current_x, self.current_y - 20)