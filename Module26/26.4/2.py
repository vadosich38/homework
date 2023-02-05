import random


class CountIterator:
    def init(self):
        self.max_count = 0
        self.__f_num = random.random()
        self.__fact_count = 0
        self.__new_num = 0

    def set_counter(self, count):
        self.__max_count = count

    def __iter__(self):
        self.f_num = random.random()
        self.__fact_count = 0
        self.__new_num = 0
        return self

    def __next__(self):
        if self.__max_count > self.__fact_count:
            self.__fact_count += 1
            self.__new_num += random.random()
            self.__new_num = round(self.__new_num, 2)
            return self.__new_num
        else:
            raise StopIteration


my_iter = CountIterator()


while True:
    ans = int(input("Введите колво чисел: "))
    my_iter.set_counter(count=ans)
    for i_elem in my_iter:
        print(i_elem)
