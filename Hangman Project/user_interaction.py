import string
from nltk.corpus import words


def user_instruction():
    print('''
    Welcome to a game of hangman!
    Please type in a letter one by one into the input terminal.
    For every letter you get right, the screen shows the letter that was guessed.
    For every letter you get wrong, the letter will be added to the list of wrong guesses and you lose a try.
    Once you have not guessed the word in ten tries, you lose!
    Thank you for playing!
    ''')


def user_help():
    print('''
    Input a letter into the system terminal.
    If you want to guess the word, write down the entire word into the terminal without spaces.
    To quit the game, type q.
    ''')


def user_input():
    user_guess = input("Please input a letter (a-z): ")
    if user_guess.lower() in string.ascii_letters:
        return user_guess.lower()
    elif user_guess.lower() == "help":
        user_help()
    elif user_guess.lower() in words.words():
        return user_guess.lower()
    else:
        print("Invalid answer!")
