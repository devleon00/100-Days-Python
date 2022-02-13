
weight = float(input("Enter your weight in kg: ")) 
height = float(input("Enter your height in m: "))

print("Your bmi is: " + str(round(weight / height ** 2)))