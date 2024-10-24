import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

random_word = random.randint(0, len(word_list)-1)
chosen_word = word_list[random_word]
print(chosen_word)
guess = input("guess a letter\n")
for i in chosen_word:
    if guess in i:
        print("Right")
    else:
        print("Wrong")
