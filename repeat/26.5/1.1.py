def prime_gen(curr_num: int = 0, max_num: int = 0):
    while curr_num < max_num:
        curr_num += 1
        if curr_num > 1:
            if curr_num == 2 or curr_num == 3:
                yield curr_num
            else:
                for i in range(2, curr_num):
                    if curr_num % i == 0:
                        break
                else:
                    yield curr_num


my_prime_gen = prime_gen(max_num=50)

for j in my_prime_gen:
    print(j)

# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47