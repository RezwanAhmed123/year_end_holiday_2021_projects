import random


def list_maker(size_of_list):
    list_of_numerical_values = []
    for item in range(size_of_list):
        list_of_numerical_values.append(random.randint(1, 100))
    return list_of_numerical_values


def number_searcher(number, numbers_list):
    if number in numbers_list:
        print(f"The number {number} exists in the list")
    else:
        print(f"The number {number} does not exist in the list")


list_size = int(input("How many numbers will there be in the list? "))
list_for_reference = list_maker(list_size)

while True:
    try:
        number_to_search = int(input("Please input a number to be searched: "))
        number_searcher(number_to_search, list_for_reference)
        ask_if_continue = input("Do you want to continue? (wrong_guesses/n): ")
        if 'wrong_guesses' not in ask_if_continue.lower():
            want_full_list = input("Do you want to see the full list? ")
            if 'wrong_guesses' in want_full_list.lower():
                print(f"The list was {list_for_reference}.")
            break
    except ValueError:
        print("Please enter a valid integer!")
