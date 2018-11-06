import random

guess = input("Guess any number from 0 to 10 ")

random_number = random.randint(0, 10)

if int(guess) == int(random_number):
    print("you win")
else:
    print("you lose bwahahahahhahah try again")