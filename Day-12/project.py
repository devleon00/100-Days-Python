#Number Guessing Game :

import art
import random

print(art.logo)
print("Welcome to the Numver Guessing Game!")
print("Im thinking of a number between 1 and 100")
correct_number = random.randint(1, 100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
print(correct_number)

if level == "hard":
    number_of_attempts = 5
elif level == "easy":
    number_of_attempts = 10
else:
    print("Incorrect input")

should_continue = True
while should_continue:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > correct_number:
        print("Too high.")
    elif guess < correct_number:
        print("Too low.")
    if guess == correct_number:
        print(f"You got it! The answer was {correct_number}.")
        should_continue = False
    else: 
        number_of_attempts -= 1
        if number_of_attempts == 0:
            should_continue = False
            print("You've run out of guesses, you lose.")
        else: 
            print("Guess Again")