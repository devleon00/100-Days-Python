import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")

# print(f"{random.choice(names)} is going to buy the meal today!")