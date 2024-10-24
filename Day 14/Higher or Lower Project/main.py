from game_data import data
from random import randint
from art import logo

print(logo)
from art import vs

random_integer = randint(0, 49)
print(random_integer)


def first_follower(random_change):
    description = data[random_change]["description"]
    name = data[random_change]["name"]
    country = data[random_change]["country"]
    print(f"Compare A: {name}, a {description}, from {country}")


def follow_count(random_change):
    return data[random_change]["follower_count"]


random_integer1 = randint(0, 49)
print(random_integer1)


def second_followers(random_change1):
    description1 = data[random_change1]["description"]
    name1 = data[random_change1]["name"]
    country1 = data[random_change1]["country"]
    print(f"Against B: {name1}, a {description1}, from {country1}")


def follower_count1(random_change1):
    return data[random_change1]["follower_count"]


first_follower(random_change=random_integer)
print(vs)
second_followers(random_change1=random_integer1)
followers = follow_count(random_change=random_integer)
followers1 = follower_count1(random_change1=random_integer1)


should_continue = True
score = 0

while should_continue:
    guess = input("Who has more followers 'A' or 'B':").lower()
    if followers > followers1:
        if guess == "a":
            score += 1
            print(f"You're right, current score is {score}")
            first_follower(random_change=random_integer)
            followers = follow_count(random_change=random_integer)
            print(followers)
            print(vs)
            random_integer1 = randint(0, 49)
            second_followers(random_change1=random_integer1)
            followers1 = follower_count1(random_change1=random_integer1)
            print(followers1)
        else:
            print(f"sorry you lost!, with a score of  {score}")
            should_continue = False

    elif followers < followers1:
        if guess == "b":
            score += 1
            print(f"You're right, current score is {score}")
            random_integer = random_integer1
            first_follower(random_change=random_integer)
            followers = follow_count(random_change=random_integer)
            print(followers)
            print(vs)
            random_integer1 = randint(0, 49)
            second_followers(random_change1=random_integer1)
            followers1 = follower_count1(random_change1=random_integer1)
            print(followers1)

        else:
            print(f"sorry you lost!, with a score,{score}")
            should_continue = False
    else:
        print("Draw")
        random_integer = randint(0, 49)
        first_follower(random_change=random_integer)
        followers = follow_count(random_change=random_integer)
        print(followers)
        print(vs)
        random_integer1 = randint(0,49)
        second_followers(random_change1=random_integer1)
        followers1 = follower_count1(random_change1=random_integer1)
        print(followers1)

"""random_integer3 = 0


def got_right():
    print(logo)
    random_integer1
    first_follower(random_change=random_integer)"""
