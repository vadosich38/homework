def calc_func(data, fact={0: 1, 1: 1, 2: 2, 3: 6}):
    if data not in fact:
        i = max(fact)
        for j in range(i + 1, data + 1):
            fact[j] = fact[j - 1] * j

    return pow(fact[data] / pow(data, 3), 10)


print(calc_func(4))
print(calc_func(21))