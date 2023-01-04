nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

def corrector(my_list, new_list=[]):
    for elem in my_list:
        if isinstance(elem, list):
            corrector(elem)
        else:
            new_list.append(elem)
    return new_list

print(corrector(nice_list))