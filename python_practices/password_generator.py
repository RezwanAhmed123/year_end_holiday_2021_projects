import random
import string

alphabet_str = string.ascii_letters
alphabet_list = list(alphabet_str)
symbols = ("!", "@", "#", "%", "^", "&", "*", "(", ")")
list_of_weak_passwords = ["123456", "picture1", "qwerty", "omgpop", "qwertyuiop"]


def raw_password(number):
    password_for_you = []
    for cycle in range(3):
        password_for_you.append(str(random.randint(0, 9)))
        password_for_you.append(str(random.choice(alphabet_list)).upper())
        password_for_you.append(str(random.choice(alphabet_list)).lower())
    if number > 1:
        for item in range(2):
            password_for_you.append(str(random.choice(symbols)))
    return password_for_you


def password_maker(strength):
    if strength == 2:
        password_for_you = raw_password(strength)

        random.shuffle(password_for_you)
        password_output = "".join(str(item) for item in password_for_you)
        return password_output

    elif strength == 1:
        password_for_you = raw_password(strength)
        password_output = "".join(str(item) for item in password_for_you)
        return password_output

    else:
        password_output = random.choice(list_of_weak_passwords)
        return password_output


continue_trying = 'wrong_guesses'
while continue_trying == 'wrong_guesses':
    try:
        password_strength = int(input("How strong do you want your password to be? (weak[0]/medium[1]/strong[2]): "))
        print(password_maker(password_strength))
        continue_trying = input("do you need another password? (wrong_guesses/n): ").lower()
    except ValueError:
        print("Must enter a number between 0 to 2!")
