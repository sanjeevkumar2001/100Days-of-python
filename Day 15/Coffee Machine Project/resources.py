from main import MENU
from main import resources

milk = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
water = resources["water"] - MENU["latte"]["ingredients"]["water"]
coffee = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
milk1 = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
water1 = resources["milk"] - MENU["cappuccino"]["ingredients"]["water"]
coffee1 = resources["milk"] - MENU["cappuccino"]["ingredients"]["coffee"]
milk2 = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
water2 = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
water3 = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]


def is_milk_sufficient():
    return milk



def is_water_sufficient():
    return water


def is_coffee_sufficient():
    return coffee


output = is_milk_sufficient()
print(output)
output1 = is_water_sufficient()
print(output1)
output2 = is_coffee_sufficient()
print(output2)
