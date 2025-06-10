# Simple Hangman game
import random
import sys

WORDS = [
    'python',
    'algorithm',
    'function',
    'variable',
    'development',
    'hangman',
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===
    """,
]


def choose_word():
    return random.choice(WORDS)


def display_board(misses, correct_guesses, word):
    print(HANGMAN_PICS[len(misses)])
    blanks = ['_' if letter not in correct_guesses else letter for letter in word]
    print('Word: ' + ' '.join(blanks))
    print('Misses: ' + ' '.join(misses))


def play():
    word = choose_word()
    misses = []
    correct_guesses = []
    MAX_MISSES = len(HANGMAN_PICS) - 1

    while True:
        display_board(misses, correct_guesses, word)

        if len(misses) >= MAX_MISSES:
            print('You lost! The word was "{}".'.format(word))
            break
        if all(letter in correct_guesses for letter in word):
            print('Congratulations! You guessed the word.')
            break

        guess = input('Guess a letter: ').lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue
        if guess in misses or guess in correct_guesses:
            print('You already guessed that letter.')
            continue

        if guess in word:
            correct_guesses.append(guess)
        else:
            misses.append(guess)


def main():
    print('Welcome to Hangman!')
    play()
    print('Thanks for playing!')


if __name__ == '__main__':
    main()
