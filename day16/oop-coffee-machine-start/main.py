from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_on = True
while machine_on:

    coffee_type = input("What type of coffee do you have?" +" "+menu.get_items()+"\n")
    if coffee_type == "off":
            print("Turning off the coffee machine.")
            exit()
    elif coffee_type == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(coffee_type)
        if coffee_type == "cappuccino":
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)


        elif coffee_type == "latte":
            drink = menu.find_drink(coffee_type)
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)

        elif coffee_type == "espresso":
            drink = menu.find_drink(coffee_type)
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)


