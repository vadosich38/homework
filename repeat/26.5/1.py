def unlim_gen(num: int = 0):
    while True:
        yield num
        num += 1


my_gen = unlim_gen()
for i in my_gen:
    print(i)
