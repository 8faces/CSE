import random
guesses = 5
playing = True
while guesses > 0 and playing:
word_bank = ['dog', 'catfish', 'Jose', 'frog', 'gummy',
             'cat!', 'pants', 'dragon', 'lizard', 'blank']
word = random.choice(word_bank)
word_bank = list(word)
