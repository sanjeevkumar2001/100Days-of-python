from art import logo

print(logo)
from random import randint

print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
random_number = randint(1, 100)
print(random_number)
choice = input("choose difficulty 'easy' or 'hard':").lower()
should_continue = True
attempts = 10
attempts1 = 5

guess = 0
guess1 = 0


def easy():
    print(f"you have {attempts} attempts remaining to guess the number.")
    global guess
    guess = int(input("Make a guess:"))


def hard():
    print(f"you have {attempts1} attempts remaining to guess the number.")
    global guess1
    guess1 = int(input("Make a guess:"))


while should_continue:
    if choice == "easy":
        easy()
        while attempts >= 1:
            if guess > random_number:
                print("Too High")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses, Sorry you lost")
                    exit()
                easy()
            elif guess < random_number:
                print("Too low")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses, Sorry you lost")
                    exit()
                easy()
            elif guess == random_number:
                print("Congratulations You are king kohli")
                exit()
            else:
                continue
        print("You've run out of guesses,Sorry you lost")
        should_continue = False
    else:
        hard()
        while attempts1 >= 1:
            if guess1 > random_number:
                print("Too High")
                attempts1 -= 1
                if attempts1 == 0:
                    print("You've run out of guesses, Sorry you lost")
                    exit()
                hard()
            elif guess1 < random_number:
                print("Too low")
                attempts1 -= 1
                if attempts1 == 0:
                    print("You've run out of guesses, Sorry you lost")
                    exit()
                hard()
            elif guess1 == random_number:
                print("Congratulations You are king kohli")
                exit()
            else:
                continue
        print("You've run out of guesses,Sorry you lost")
        should_continue = False
