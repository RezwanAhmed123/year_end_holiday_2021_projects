def create_lists():
    list_of_letters_guessed_correctly = []
    list_of_letters_guessed_wrongly = []
    return list_of_letters_guessed_correctly, list_of_letters_guessed_wrongly


def check_guess(list_of_letters_guessed_correctly, list_of_letters_guessed_wrongly, user_input, generated_word):
    if user_input.lower() in generated_word:
        list_of_letters_guessed_correctly.append(user_input)
        return list_of_letters_guessed_correctly
    else:
        list_of_letters_guessed_wrongly.append(user_input)
        return list_of_letters_guessed_wrongly
