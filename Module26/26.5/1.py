def nonestop():
    num = 0
    while True:
        num += 1
        yield num


my_gen = nonestop()
for num in my_gen:
    print(num)
    