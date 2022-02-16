# Calculator 
import os
import art

#Add 
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide 
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    os.system('cls')
    print(art.logo)
    print("Welcome to calculator\n")
    num1 = float(input("What's the fist number?: "))
    should_continue = True
    for key in operations:
        print(key)
    while should_continue:
        user_pick = input("Pick an operation from the line above: ")
        next_number = float(input("What's the next number?: "))
        answer = operations[user_pick](num1, next_number)
        print(f"{num1} {user_pick} {next_number} = {answer}")

        if input(f"Type 'y' to continue calcultaing with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()