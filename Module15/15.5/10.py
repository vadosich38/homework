count = int(input("Сколько чисел в списке: "))
num_list = []
def input_list():
    for _ in range(count):
        num = int(input("Введите число: "))
        num_list.append(num)
def sort():
    lenth = len(num_list)
    mult = 0
    max = -10e16
    for _ in range(lenth):
        for num in range(0 + mult, lenth):
            if num_list[num] > max:
                max = num_list[num]
                pos = num

        num_list[0 + mult], num_list[pos]  = num_list[pos], num_list[0 + mult]
        mult += 1
        max = -10e16
    print(num_list)

input_list()
sort()
