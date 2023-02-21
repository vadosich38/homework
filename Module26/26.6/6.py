# Incorrect solution of the problem of linked lists

class LinkedList:
    def __init__(self):
        self.__index_count = -1
        self.__data_list = list()

    def __str__(self):
        return str(self.__data_list)

    def __iter__(self):
        self.__index_count = -1
        return self

    def __next__(self):
        self.__index_count += 1
        if self.__index_count < len(self.__data_list):
            return self.__data_list[self.__index_count]
        else:
            raise StopIteration

    def get(self, index: int):
        return self.__data_list[index]

    def append(self, num: int):
        self.__data_list.append(num)

    def remove(self, index):
        del self.__data_list[index]


my_list = LinkedList()
my_list.append(num=10)
my_list.append(num=20)
my_list.append(num=30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(index=2))
print('Удаление второго элемента.')
my_list.remove(index=1)
print('Новый список:', my_list)
for i_num in my_list:
    print(i_num)
