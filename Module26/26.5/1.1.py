def simple_printer(max):
    num = 0
    while num < max:
        num += 1
        if num != 2 and num % 2 == 0 or num == 1:
            continue

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


my_gen = simple_printer(max=500)

for num in my_gen:
    print(num, end=" ")
