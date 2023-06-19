import random


class CountIterator:
    def __init__(self, count):
        self.max_count = 0
        self.__fact_count = 1
        self.__new_num = 0
        self.__max_count = count

    def __iter__(self):
        self.__new_num = 0
        self.__fact_count = 0
        return self

    def __next__(self):
        while self.__fact_count < self.__max_count:
            self.__fact_count += 1
            # print("Старое число", round(self.__new_num, 2))
            self.__new_num = round(self.__new_num + random.random(), 2)
            # print("Новое число", round(self.__new_num, 2))
            return self.__new_num
        else:
            raise StopIteration


my_iter = CountIterator(5)
for i_elem in my_iter:
    print(i_elem)
print()
for i_elem in my_iter:
    print(i_elem)
