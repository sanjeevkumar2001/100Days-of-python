from main import MENU
from main import resources


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            exit()
        else:
            resources[item] = resources[item] - order_ingredients[item]


def insert_coins(total_cost):
    quarters = round(float(int(input("how many quarters:")) * 0.5), 2)
    dimes = round(float(int(input("how many dimes:")) * 0.10), 2)
    nickels = round(float(int(input("how many nickels:")) * 0.05), 2)
    pennies = round(float(int(input("how many pennies")) * 0.01), 2)
    total = quarters + dimes + nickels + pennies

    if total < total_cost:
        print(f"Sorry, there is not enough money")
        exit()
    else:
        change = round(total - total_cost,2)
        print(f"Here is your {change} dollars in change")
        return total_cost


def print_statement(choice):
    print(f"Here is your {choice}.Enjoy!")


money = 0
should_continue = True
while should_continue:
    choice = input("what would you like? (espresso/latte/cappuccino)").lower()
    if choice == "off":
        exit()

    elif choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")

        print(f"money: ${money}")

    else:
        drink = MENU[choice]["ingredients"]
        is_resources_sufficient(order_ingredients=drink)
        cost = MENU[choice]["cost"]
        money += insert_coins(total_cost=cost)
        print_statement(choice)
