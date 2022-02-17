from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue = True
menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()
while should_continue:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice == "off":
        should_continue = False
    elif user_choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        if drink and coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
