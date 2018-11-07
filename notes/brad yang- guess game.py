import random

guess = input("Guess any number from 0 to 10 first try ")

random_number = random.randint(0, 10)

if int(guess) == int(random_number):
        print("you win")
    else:
guess1 = input("second try again")

if int(guess1) == int(random_number):
        print("you win")
    else:
guess2 = input("third try again")

if int(guess2) == int(random_number):
        print("you win")
    else:
guess3 = input("forth try again")

if int(guess3) == int(random_number):
        print("you win")
    else:
guess4 = input("fifth last try")

if int(guess4) == int(random_number):
        print("you win")
    else:
        print("you lose try again")