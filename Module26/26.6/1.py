from typing import Iterable
my_num = int(input("Введите число: "))


def my_gen(num: int) -> Iterable[int]:
    fact = 1
    while fact < num:
        res = fact ** 2
        fact += 1
        yield res


class Square:
    def __init__(self, num: int):
        self.__my_num = num
        self.__fact_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__fact_num += 1
        if self.__fact_num < self.__my_num:
            return self.__fact_num ** 2
        else:
            raise StopIteration


res1 = my_gen(my_num)
res2 = (num ** 2 for num in range(1, my_num))
res3 = Square(my_num)

print("Результат первой реализации:")
for i_num in res1:
    print(i_num)
print("Результат второй реализации:")
for i_num in res2:
    print(i_num)
print("Результат третей реализации:")
for i_num in res3:
    print(i_num)
