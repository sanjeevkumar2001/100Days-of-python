from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

"""def calculation(first_number, second_number):
    if operator == "+":
        return add(first_number, second_number)
    elif operator == "-":
        return sub(first_number, second_number)
    elif operator == "*":
        return mul(first_number, second_number)
    else:
        return div(first_number, second_number)"""


def dictionary_calculation(first_number, second_number):
    return dict[operator](first_number, second_number)


should_continue = True

guess = int(input("enter the first number:\n"))
operator = input("choose a operator between '+','-','*','/'.")
second_guess = int(input("enter the second number"))
"""output = calculation(first_number=guess, second_number=second_guess)
print(output)"""
output1 = dictionary_calculation(first_number=guess, second_number=second_guess)
print(output1)

while should_continue:

    continuation = input(" do u want to continue type 'yes' or 'no'.")
    if continuation == "yes":
        operator = input("choose a operator between '+','-','*','/'.")
        second_guess1 = int(input("enter the second number:"))
        """output = calculation(first_number=output, second_number=second_guess1)
        print(output)"""
        output1 = dictionary_calculation(first_number=output1, second_number=second_guess1)
        print(output1)
    else:

        should_continue = False
