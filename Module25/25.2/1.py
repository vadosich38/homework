class Dot:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Точка расположена по такиим координатам х={} y={}\n".format(self.__x, self.__y)

    def set_x(self, new_x):
        try:
            if isinstance(new_x, int):
                print("Координата x точки меняется с {} на {}".format(self.__x, new_x))
                self.__x = new_x
            else:
                raise "Ошибка! Заданые данные не являются числом"
        except TypeError:
            print("Значение должно быть цифровым. Не принятое значение: {}".format(new_x))

    def set_y(self, new_y):
        try:
            if isinstance(new_y, int):
                print("Координата y точки меняется с {} на {}".format(self.__y, new_y))
                self.__y = new_y

            else:
                raise "Ошибка! Заданые данные не являются числом"
        except TypeError:
            print("Значение должно быть цифровым. Не принятое значение: {}".format(new_y))

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


dot1 = Dot(1, 2)
dot2 = Dot()

print(dot1)
print(dot2)

print(dot1.get_x())
print(dot1.get_y())
print(dot2.get_x())
print(dot2.get_y())

print(dot1)
print(dot2)

dot1.set_x(100)
dot1.set_x("a")
dot1.set_y(120)
dot2.set_x(50)
dot2.set_y("a")
dot2.set_y(75)

print(dot1)
print(dot2)


