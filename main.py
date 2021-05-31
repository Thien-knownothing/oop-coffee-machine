from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
on = True
menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
while on:
    drink = input("Please select your drink: espresso, latte, cappuccino: ")
    if drink == "off":
        print("Maintenen on, Shutdown machine")
        on = False
    elif drink == "report":
        maker.report()
        money.report()
    elif drink in menu.get_items():
        ordered = menu.find_drink(drink)
        if maker.is_resource_sufficient(ordered):
            if money.make_payment(ordered.cost):
                maker.make_coffee(ordered)
    else:
        print("please input sufficient order")

