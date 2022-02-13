print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

string1 = "true"
string2 = "love"

count1 = 0
count2 = 0

name_combined = name1 + name2

for letter in string1:
    count1 += name_combined.count(letter.lower()) 

for letter in string2:
    count2 += name_combined.count(letter.lower()) 

total = int(str(count1) + str(count2))

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")

if 50 >= total >= 40:
    print(f"Your score is {total}, you are alright together")

else: 
    print(f"Your score is {total}")