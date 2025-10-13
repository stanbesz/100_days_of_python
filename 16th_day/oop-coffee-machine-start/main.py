from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_coffee = Menu()
money_logic = MoneyMachine()
coffee_logic = CoffeeMaker()


def main():
    is_active = True

    while is_active:

        prompt = input("What would you like? (espresso/latte/cappuccino/): ").lower()

        if prompt == "off":
            print("Coffee Maker ended!")
            is_active = False
            return
        elif prompt == "report":
            coffee_logic.report()
        else:
            coffee_item = menu_coffee.find_drink(prompt)
            if not coffee_item:
                print("Wrong Item chosen!")
            else:
                if coffee_logic.is_resource_sufficient(coffee_item):
                    if not money_logic.make_payment(coffee_item.cost):
                        print("Sorry not enough money!")
                    else:
                        coffee_logic.make_coffee(coffee_item)

                else:
                    print("​Sorry there is not enough resources.")

main()