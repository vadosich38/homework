def calc_func(data):
    my_fact = factorial(data)

    return pow(my_fact / pow(data, 3), 10)

def factorial(num, fact={0: 1, 1: 1, 2: 2, 3: 6}):
    if num not in fact:
        fact[num] = factorial(num-1) * num
    return fact[num]


print(calc_func(4))
print(calc_func(21))