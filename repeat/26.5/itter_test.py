i = (x for x in range(7)) #генераторное выражение, ленивые вычисления
j = [i for i in range(7)] #генератор списка, лист комприхенщенс


#функция генератор, ленивые вычисления
def my_iter(num: int = 0, maxi: int = 7):
    while num < maxi:
        yield num
        num += 1


#класс итератор, ленивые вычисления
class MyIter:
    def __init__(self):
        self.__start = -1
        self.__max = 6

    def __iter__(self):
        self.__start = -1
        return self

    def __next__(self):
        while self.__start < self.__max:
            self.__start += 1
            return self.__start
        else:
            raise StopIteration


var1 = i
var2 = j
var3 = my_iter()
var4 = MyIter()

print("Вариант1")
for i in var1:
    print(i)

print("Вариант2")
for i in var2:
    print(i)

print("Вариант3")
for i in var3:
    print(i)

print("Вариант4")
for i in var4:
    print(i)
