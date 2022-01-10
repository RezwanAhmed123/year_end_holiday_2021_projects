from nltk.corpus import words
import random


def generated_word():
    word_list = words.words()
    random_word = random.choice(word_list).lower()
    word_in_game = list(random_word)
    return word_in_game
