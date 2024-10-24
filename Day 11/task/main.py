from art import logo

print(logo)
import random

num = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_score = 0
for i in range(0, 2):
    user_random_cards = random.choice(cards)
    num.append(user_random_cards)

user_score = num[0] + num[1]
if user_score == 21:
    print("You win!")
    exit()
print(f"Your cards: {num}, current score:{user_score}")

num1 = []
computer_random_card = random.choice(cards)
num1.append(computer_random_card)
print(f"Computer's first card is {computer_random_card}")

temp = 0


def user_calculation(score):
    user_random_cards1 = random.choice(cards)
    num.append(user_random_cards1)
    score += user_random_cards1
    return score


def computer_calculation(score1):
    computer_random_card1 = random.choice(cards)
    num1.append(computer_random_card1)
    score1 += computer_random_card1
    return score1


should_continue = True
while should_continue:
    choice = input("do you want to get another card type 'y' for yes or 'n' to pass").lower()
    if choice == "y":
        user_score = user_calculation(score=user_score)
        print(f"Your cards: {num}, current score: {user_score}")
        if user_score > 21:
            for i in range(0, len(num)):
                if num[i] == 11:
                    num[i] = 1
                    user_score -= 10
                    continue
                else:
                    print("you lose")
                    exit()
    else:
        while computer_random_card <= 21:
            computer_random_card = computer_calculation(score1=computer_random_card)
            print(f"Computer's final hand: {num1}, final score: {computer_random_card}")
            if computer_random_card <= 21:
                if user_score == 21 and computer_random_card < 21:
                    print("you win")
                    exit()
                elif computer_random_card > user_score:
                    print("you lose")
                    exit()
                elif user_score == computer_random_card:
                    print("Draw")
                    exit()
                else:
                    continue
            else:
                print("You win")
                should_continue = False
