import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choice = [rock,paper,scissors]
number = int(input("what do you choose? Type 0 for Rock, 1 for paper 2 for scissors.\n"))
print(game_choice[number])
number_1 = random.randint(0,2)
print(f"Computer chose:{number_1}")
print(game_choice[number_1])
if number == number_1:
    print("Draw")
elif number == 0 and number_1 == 1:
    print("you lose")
elif number == 0 and number_1 == 2:
    print("you win")
elif number == 1 and number_1 == 0:
    print("you win")
elif number == 1 and number_1 == 2:
    print("you lose")
elif number == 2 and number_1 == 0:
    print("you lose")
elif number == 2 and number_1 == 1:
    print("you win")
else:
    print(" you have entered an invalid number")

