def only_list_ends(given_list):
    list_ends = [given_list[0], given_list[-1]]
    return list_ends


a = [5, 10, 15, 20, 25]
new_list = only_list_ends(a)
print(new_list)
