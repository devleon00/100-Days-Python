from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.level_text = Turtle()
        self.level_text.penup()
        self.level_text.pencolor("black")
        self.level_text.goto(-250, 250)
        self.level_text.hideturtle()
        self.update_level()

    def update_level(self):
        self.level_text.clear()
        self.level_text.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        game = Turtle()
        game.penup()
        game.pencolor("black")
        game.hideturtle()
        game.write("GAME OVER", align="center", font=FONT)
        game.home()
