# Hangman
import random

guess_max = 7
guesses = 0
guessed_letter = []
word = 'cat'
split_word = list(word)
word_len = len(split_word)
game_word = []
i = 0

# Create game word with underscores in place of letters
while i <= word_len-1:
    game_word.append('_')
    i += 1


while guesses < guess_max:
    guess = raw_input("What's your guess? ")
    try:
        guessed_letter.index(guess)
        print "You already guessed that letter"
        continue
    except ValueError:
        pass

    # Check if the letter has already be tried
    try:
        found = split_word.index(guess)
    except ValueError:
        found = 99

    # Check if letter is found
    if found < 99:
        game_word[found] = guess
        print "found it"
    else:
        guesses += 1
        print "Not found"

    guessed_letter.append(guess)

print game_word

print guessed_letter