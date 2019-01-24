import random
word_bank = ['dog', 'catfish', 'Jose', 'frog', 'gummy',
             'cat!', 'pants', 'dragon', 'lizard', 'blank']
word = random.choice(word_bank)
word = "pants"
word_bank = list(word)


guess = 8

while guess > 0:
    guess = input("you have 8 guesses :")


guess -= 1
