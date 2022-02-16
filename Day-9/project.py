import os
import art

dictionary_users = {}
continue_user = True

print(art.logo)
print("Welcome to the secret auction program.\n")

while continue_user:
    name = input("What's is your name? \n")  
    bid = input("What's is your bid? \n")  
    dictionary_users[name] = bid
    other_user = input("Are there any other bidders? Type 'yes' or 'no' \n")  
    if other_user == "no":
        continue_user = False
    os.system('cls')

max_value = 0
name = ""
for key in dictionary_users:
    if int(dictionary_users[key]) > max_value:
        max_value = int(dictionary_users[key])
        name = key

print(f"The winner is {name} with a bid of {max_value}")