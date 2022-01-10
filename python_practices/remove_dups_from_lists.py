def dup_remover(first_list, second_list):
    new_list = {number2 for number1 in first_list for number2 in second_list if number1 == number2}
    return new_list


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(dup_remover(a, b))

