# Rock paper scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock. 1 for Paper or 2 dor Scissors\n" ))
ai_chose = random.randint(0, 2)

print(options[user_choice])

print(f"""Computer chose: 
    {options[ai_chose]}
""")

if (user_choice == 0 and ai_chose == 2) or (user_choice == 1 and ai_chose == 0) or (user_choice == 2 and ai_chose == 1):
    print("You win")
elif ai_chose == user_choice:
    print("Draw")
else:
    print("You lose")



#Write your code below this line 👇

