from turtle import Turtle, Screen, shape
import pandas

screen = Screen()
screen.title("U.S States Game")
img = "sblank_states_img.gif"
screen.addshape(img)
shape(img)

data = pandas.read_csv("./50_states.csv")
data_states = data["state"].tolist()
is_on = True
score = 0

while is_on:
    state = screen.textinput(f"{score}/50 Guess state", "What's another state's nam?").title()

    if state in data_states:
        score += 1
        new_x = data["x"][data["state"] == state].item()
        new_y = data["y"][data["state"] == state].item()
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto((new_x, new_y))
        tim.write(state, align="center")
    
    if score == 50:
        is_on = False
        

screen.exitonclick()
