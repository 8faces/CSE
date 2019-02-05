import random
import string
Underscore = list(string.punctuation)
word_bank = ['dog', 'catfish', 'Jose', 'frog', 'gummy',
             'cat!', 'pants', 'dragon', 'lizard', 'blank']
word = random.choice(word_bank)
word_bank = list(word)

letter_list = []

guess = 8


while guess > 0:
    bush = []
    for letter in word:
        if letter in letter_list:
            bush.append(letter)
        else:
            bush.append("_")
    print(bush)

    tries = input("Come and guess papa Joe's letters")
    letter_list.append(tries)
    guess -= 1
