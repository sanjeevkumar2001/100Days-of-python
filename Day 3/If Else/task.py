print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("what is your age"))
bill = 0
if height > 120:
    print("you can ride the rollercoaster")
    if age <= 12:
        bill = 5
        print("please pay $5")
    elif age <= 18:
        bill = 7
        print(" you have to pay $7")
    elif age >= 45 and age <= 55 :
        print(f"you have to pay $0")
    else:
        bill = 12
        print("you have to pay $12")
    want_photo = input("do u want to have a photo? type y for yes and n for no")
    if want_photo == "y":
        bill += 3
    print(f"your final bill is {bill}")
else:
    print("sorry,you can't ride")