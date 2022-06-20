"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python "https://nostarch.com/inventwithpython
Tags:short, game, puzzle"""

import random

NUM_DIGITS = 3 # (!)Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Try setting this to 1 or 100.


def main():
    print(""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico       One digit is correct but in the wrong position.
    Fermi       One digit is corrent and in the right position.
    Bagels      No digit is correct.

For example, if the secret number was  248 and your guess was 843, the
clues would be Fermi Pico."".format(NUM_DIGITS))

while True: # Main game loop.
    # This stores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print('I have a thought up a number.')
    print('You have {} guesses to get it.'.format(MAX_GUESSE))

    numGuesses = 1



