class CountIterator:
    __counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__counter += 1
        return self.__counter - 1


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
