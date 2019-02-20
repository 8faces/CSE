import random
import string

Underscore = list(string.punctuation)
word_bank = ['dog', 'catfish', 'Jose', 'frog', 'gummy',
             'cat!', 'pants', 'dragon', 'lizard', 'blank']
word = random.choice(word_bank)
word_bank = list(word)

letter_list = []
playing = True
hastheplayerwon = False
guess = 8


while guess > 0 and playing:
    bush = []
    for letter in word:
        if letter in letter_list:
            bush.append(letter)
        else:
            bush.append("_")
    if "_" not in bush:
        print("DUN DUN DUN")
        playing = False
<<<<<<< HEAD:Hang man.py
=======
        hastheplayerwon = True
        continue

    print(bush)

    tries = input("guess letter")
    letter_list.append(tries)

    guess -= 1
>>>>>>> cb83a6636b7e006f7562ea35ee3164b735ad3555:Brad Yang Hang man.py


if playing and not hastheplayerwon:
    print("you just killed a man")
else:
    print("you win")

        hastheplayerwon = True
        continue

    print(bush)

    tries = input("Come and guess papa Joe's letters")
    letter_list.append(tries)
    guess -= 1