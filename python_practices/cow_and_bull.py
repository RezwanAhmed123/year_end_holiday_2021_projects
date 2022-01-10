import random


def computer_number():
    g_value = random.randint(1000, 9999)
    return g_value


def determine_cow_or_bull(computer, human):
    computer_value = [int(b) for b in str(computer)]
    human_number = [int(a) for a in str(human)]
    warning_statement = ''
    bulls = 0
    cows = 0
    for item in range(0, 4):
        if computer_value[item] == human_number[item]:
            cows += 1
        elif human_number[item] in computer_value:
            if human_number.count(human_number[item]) <= computer_value.count(human_number[item]):
                bulls += 1
            else:
                if warning_statement == f'Too many {human_number[item]}':
                    pass
                else:
                    warning_statement = f'Too many {human_number[item]}'
                    print(f'{human_number.count(human_number[item]) - computer_value.count(human_number[item])}'
                          f' more {human_number[item]}s than required')
    return cows, bulls


generated_number = str(computer_number())
print('''
Hello and welcome to a game of cow and bull!
Try to guess a number between 1000 to 9999 (any 4 digit number).
If you guess a correct digit at the correct position, the computer tells you that you guessed (correct_guesses) cows.
If you guess a correct digit at the wrong position, the computer tells you that you guessed, (wrong_guesses) bulls.
Guess the secret number to win!
To stop the game and reveal the answer, simply type in 'reveal answer' .
''')
user_guess = ''
while user_guess != generated_number:
    if user_guess.lower() != 'reveal answer':
        try:
            user_guess = str(input("Please input a number between 1000 and 9999: "))
            (x, y) = determine_cow_or_bull(generated_number, user_guess)
            print(f"{x} cows, {y} bulls.")
        except ValueError:
            print("Please input an integer!")
        except IndexError:
            print("Please input a 4-digit number!")
    else:
        print(f'The generated number was {generated_number}. You lose!')
        break

if user_guess == generated_number:
    print("You win!")
