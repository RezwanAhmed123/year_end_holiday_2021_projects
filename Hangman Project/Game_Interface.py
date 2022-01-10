import user_interaction
import random_word_chooser
import Game_Mechanics

user_interaction.user_instruction()
computer_word = random_word_chooser.generated_word()
(correct_guesses, wrong_guesses) = Game_Mechanics.create_lists()
guess_status = list("_" * len(computer_word))
all_guesses = []
tries_counter = 1

while 0 < tries_counter < 11:
    if guess_status != computer_word:
        user_guess = user_interaction.user_input()
        if user_guess.lower() == "quit":
            tries_counter = 11
            break
        else:
            user_guess = list(user_guess)
            for letter in user_guess:
                if letter in all_guesses:
                    print("Already guessed!")
                else:
                    Game_Mechanics.check_guess(correct_guesses, wrong_guesses, letter, computer_word)
                    all_guesses.append(letter)
        for items in range(len(computer_word)):
            secret_letter = computer_word[items]
            if secret_letter in correct_guesses:
                guess_status[items] = secret_letter
        print(guess_status)
        if len(wrong_guesses) != 0:
            print(f"Your current wrong guesses are {wrong_guesses}")
        tries_counter = 1 + len(wrong_guesses)
        print(f"Tries left = {11 - tries_counter}")
    elif computer_word == guess_status:
        print("You win!")
        break
print(f"The game is over! The correct word was {computer_word}")
