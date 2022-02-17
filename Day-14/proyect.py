# Higher or lower Game

import art
from game_data import data
import random
import os

count = 0
should_continue = True
elections = random.choices(data, k=2)
while should_continue:
    os.system("cls")
    print(art.logo)
    if count > 0:
        print(f"You're right! Current score: {count}")
    elections[0] = elections[1]
    elections[1] = random.choice(data)
    if elections[0] == elections[1]:
        elections[1] = random.choice(data)
    correct_choice = ""
    if elections[0]['follower_count'] > elections[1]['follower_count']:
        correct_choice = "A"
    elif elections[0]['follower_count'] < elections[1]['follower_count']:
        correct_choice = "B"

    print(f"Compare A: {elections[0]['name']}, a {elections[0]['description']}, from {elections[0][ 'country']}.")
    print(art.vs)
    print(f"Compare B: {elections[1]['name']}, a {elections[1]['description']}, from {elections[1][ 'country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == correct_choice:
        count += 1
    else:   
        should_continue = False

print(f"Wrong! You're total score was {count}")
