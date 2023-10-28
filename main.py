from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_class = Menu()
coffeemaker_class = CoffeeMaker()
money_machine_class = MoneyMachine()
is_on = True


while is_on:
    choice = input(f"What would you like? {menu_class.get_items()}: ")
    if choice == "report":
        coffeemaker_class.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu_class.find_drink(choice)
        resources_enough = coffeemaker_class.is_resource_sufficient(drink)
        if resources_enough:
            cost = drink.cost
            if money_machine_class.make_payment(cost):
                coffeemaker_class.make_coffee(drink)
