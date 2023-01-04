def my_printing(start, finish):
    if start == finish:
        return print(finish)
    else:
        print(start)
        start += 1
        my_printing(start, finish)


my_start = 1
my_num = int(input("Введите до какого числа печатать: "))
my_printing(my_start, my_num)
