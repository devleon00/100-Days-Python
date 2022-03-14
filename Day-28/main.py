from cProfile import label
from itertools import count
from tkinter import *
from tkinter import font

from matplotlib.pyplot import fill, text
from prettytable import from_html
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    label_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label_title.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label_title.config(text="Break", fg=PINK)

    else: 
        count_down(5*60)
        label_title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        check = reps // 2
        checks_marks.config(text="✓" * check)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fil="white", font=(FONT_NAME, 35, "bold"))

label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(row=0, column=1)

button_start= Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"),highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

checks_marks = Label(fg=GREEN, bg=YELLOW)
checks_marks.grid(column=1, row=3)

canvas.grid(row=1, column=1)


window.mainloop()