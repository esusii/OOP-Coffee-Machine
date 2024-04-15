from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True

while machine_on:
    m = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()

    for i in range (0,1):
        print(m.get_items())
    choice = input("Which coffee would you like?:")
    if choice == "report":
        cm.report()
        mm.report()
    else:
        order = m.find_drink(choice)
        enough_resources = cm.is_resource_sufficient(order)
        if order:
            cost = order.cost
            print(f"The cost of a {choice} is ${cost}.")
            if cm.is_resource_sufficient(order):
                mm.make_payment(cost)
                cm.make_coffee(order)









