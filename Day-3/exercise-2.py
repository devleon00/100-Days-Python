height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2), 2) 
if bmi < 18.5:
    print(f"{bmi} Underweight")
elif 24.9 > bmi:
    print(f"{bmi} Normal weight")
elif 29.9 > bmi:
    print(f"{bmi} Overweight")
elif 34.9 > bmi:
    print(f"{bmi} Obesity class I")
elif 39.9 > bmi:
    print(f"{bmi} Obeseity class II")
else:
    print("Obesity class III")

