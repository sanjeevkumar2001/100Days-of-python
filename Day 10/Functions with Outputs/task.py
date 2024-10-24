str = ""


def format_name(f_name, l_name):
    str = f_name + l_name
    return str.title()


print(format_name(input("enter your first_name"), input("enter your second name")))
