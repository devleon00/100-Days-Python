# Coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    for key in resources:
        print(f"{key}: {resources[key]}")


def make_coffee(coffee):
    coffeein = MENU[coffee]["ingredients"]
    for key in coffeein:
        resources[key] -= coffeein[key]
    resources["money"] += MENU[coffee]["cost"]
    print(f"Here is your {coffee}. Enjoy!.")


def enough_money(money, coffee):
    coffee_price = MENU[coffee]["cost"]
    if money < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
    elif money == coffee_price:
        print("No change")
        make_coffee(coffee)
    elif money > coffee_price:
        print(f"Here is ${round(money - coffee_price, 2)} dollars in change.")
        make_coffee(coffee)


available = True
while available:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "off":
        available = False
    elif coffee == "report":
        report()
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        incomplete_resources = False
        for key in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][key] > resources[key]:
                print(f"Sorry there is not enough {key}.")
                incomplete_resources = True
        if not incomplete_resources:
            print(f"The cost is {MENU[coffee]['cost']} Insert coins... ")
            total = int(input("How many quarters?: ")) * .25
            total += int(input("How many dimes?: ")) * .10
            total += int(input("Hoe many nickles?: ")) * .05
            total += int(input("How many pennies?: ")) * .01
            enough_money(total, coffee)
