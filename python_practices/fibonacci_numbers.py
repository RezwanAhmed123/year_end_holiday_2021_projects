def sequence_filler(size_of_list):
    first = 1
    before = 0
    fibonacci_list = [1]
    for number in range(size_of_list):
        next_number = first + before
        fibonacci_list.append(next_number)
        before = first
        first = next_number
    return fibonacci_list


number_in_sequence = int(input("How many numbers do you want in this fibonacci sequence? "))
print(sequence_filler(number_in_sequence))
