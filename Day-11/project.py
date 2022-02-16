# Blackjack

import random
import os
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    os.system("cls")
    print(art.logo)
    user_cards = random.choices(cards, k=2)
    cpu_cards = random.choices(cards, k=2)
    while sum(cpu_cards) < 17:
        cpu_cards.append(random.choice(cards))
    should_cointinue = True
    while should_cointinue:
        print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"    Computer's first card is {cpu_cards[0]}")
        if sum(user_cards) < 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                random_choice = random.choice(cards)
                if random_choice == 11 and sum(user_cards) + 11 > 21:
                    user_cards.append(1)
                else:
                    user_cards.append(random_choice)
            else:
                should_cointinue = False
        else:
            should_cointinue = False

    final_user = sum(user_cards)
    final_computer = sum(cpu_cards)
    print(f"Your final hand: {user_cards}, final score: {final_user}")
    print(f"Computer's final hand: {cpu_cards}, final score: {final_computer}")
    if final_user > 21:
        print("    You went over. You lose 😭")

    elif final_computer > 21:
        print("    Opponent went over. You win 😁")
        
    elif final_user == 21 and len(user_cards) == 2 and final_computer != 21:
        print("    You win with Blackjack 😁")

    elif final_computer == 21 and len(cpu_cards) == 2 and final_user != 21:
        print("    Computer win with Blackjack 😁")

    elif final_user > final_computer:
        print("    You win 😃")
    
    elif final_user < final_computer:
        print("    You lose 😤")

    else:
        print("    Draw 🙃")
        
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
        blackjack()
    else:
        return

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()