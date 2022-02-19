from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.hideturtle()
        self.pencolor("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))