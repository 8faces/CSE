import random
import string
word_bank = ['dog', 'catfish', 'Jose', 'frog', 'gummy',
             'cat!', 'pants', 'dragon', 'lizard', 'blank']
word = random.choice(word_bank)
word_bank = list(word)
guess = 8
while guess > 0:
    input("you have 8 guesses")

for i in range(len(word_bank)):
