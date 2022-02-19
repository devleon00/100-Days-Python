from turtle import Turtle, Screen, colormode
import random

library_color = []
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


tim = Turtle()
tima= ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
       "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
tim.shape("turtle")
tim.pensize(5)
tim.speed(0)

for n in range(0, 36):
    tim.circle(100)
    tim.right(10)
    tim.pencolor(random_color())

screen = Screen()
screen.exitonclick()
