def my_zip(*args):
    length = min(len(element) for element in args)
    tpl_list = [tuple(struct[i] for struct in map(list, args))
    for i in range(length)]
    return tpl_list


a = {1, 100, 3}
b = {10: 12, 30: 34, "z": 11}

print(my_zip(a, b))