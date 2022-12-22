my_tuple = (-4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
my_elem = int(input("Введите элемент: "))

def func(tuple_1, elem):
    if elem not in tuple_1:
        return ()
    elif tuple_1.count(elem) == 1:
        return tuple_1[tuple_1.index(elem):]
    else:
        return tuple_1[tuple_1.index(elem):tuple_1.index(elem, tuple_1.index(elem) + 1) + 1]

print(func(my_tuple,my_elem))
