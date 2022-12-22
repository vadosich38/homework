my_tuple = (100, 21, 222, 23, 34, 55, 66, 27, 118, 29)

def sort(tuple1):
    for i_symbol in tuple1:
        if not isinstance(i_symbol, int):
            print("В кортеже обнаружено не целое число!")
            return tuple1
    my_list = list(tuple1)
    for i_index in range(len(my_list) - 1):
        my_list[my_list.index(min(my_list[i_index:]))], my_list[i_index] = \
            my_list[i_index], my_list[my_list.index(min(my_list[i_index:]))]
    new_tuple = tuple(my_list)
    return new_tuple

print(sort(my_tuple))