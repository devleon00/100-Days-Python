# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 90)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors[10-30])

from turtle import Turtle, Screen, colormode
import random

# 10 * 10 | 20 size | 50 separation |

tim = Turtle()
tim.speed(0)
tim.shape("arrow")
color_list = [(245, 243, 239), (246, 243, 244), (202, 164, 109), (240, 245, 242),
              (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41),
              (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72)]

screen = Screen()
screen.colormode(255)
screen.setup(width=1000, height=1000, startx=200, starty=200)

tim.penup()
for i in range(10):
    tim.goto(0, i * 50)
    for j in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)


screen.exitonclick()
