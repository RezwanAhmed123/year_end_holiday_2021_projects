import random
secret_number = random.randint(0, 99999)
user_input = f'The secret number was {secret_number}.'
with open('file_to_be_saved_as.txt', 'w') as open_file:
    open_file.write(user_input)
print("All done, please check the file!")
