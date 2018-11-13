import random

guesses = 5
random_number = random.randint(0, 10)
playing = True
while guesses > 0 and playing:
    guess = input("Guess a number from 0-10")
    if int(guess) == int(random_number):
        print("You Win!")
        playing = False
    else:
        print("Try again")
        guesses -= 1
    if int(guess) < int(random_number):
        print("to low")
    if int(guess) > int(random_number):
        print("to high")