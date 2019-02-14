import random
import string
playing = True
Underscore = list(string.punctuation)
word_bank = ['dog', 'catfish', 'Jose', 'frog', 'gummy',
             'cat!', 'pants', 'dragon', 'lizard', 'blank']
word = random.choice(word_bank)
word_bank = list(word)

letter_list = []
hastheplayerwon = False
guess = 8


while guess > 0:
    bush = []
    for letter in word:
        if letter in letter_list:
            bush.append(letter)
        else:
            bush.append("_")
    if "_" not in bush:
        print("DUN DUN DUN")
        playing = False
        hastheplayerwon = True
        continue

    print(bush)

    tries = input("Come and guess papa Joe's letters")
    letter_list.append(tries)
    guess -= 1


if playing and not hastheplayerwon:
    print("you just killed a man")

else:
    print("you win")
