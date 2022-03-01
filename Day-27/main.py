from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

def button_clicked():
    my_label_result.config(text=round((int(input.get()) * 1.60934), 2))

#Label

my_label_equal = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label_equal.grid(column=0, row=1)

my_label_miles = Label(text="Miles", font=("Arial", 24, "bold"))
my_label_miles.grid(column=3, row=0)

my_label_km = Label(text="km", font=("Arial", 24, "bold"))
my_label_km.grid(column=3, row=1)

my_label_result = Label(text="0", font=("Arial", 24, "bold"))
my_label_result.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=2, row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()

