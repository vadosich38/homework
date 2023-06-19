import random


def my_func(count: int):
    prev_num = random.random()
    for num in range(count):
        print("Первое число:", round(prev_num, 2))
        rand_num = random.random()
        print("Сгенерированный рандом:", round(rand_num, 2))
        new_num = prev_num + rand_num
        print("Сумма:", round(new_num, 2))
        prev_num = new_num

        yield round(new_num, 2)


print("Вывод 1")
for i in my_func(5):
    print(i, "\n")

print("Вывод 2")
for i in my_func(5):
    print(i, "\n")

print("Вывод 3")
for i in my_func(5):
    print(i, "\n")
