import re


class Man:
    __counter = 0

    def __init__(self, name, age):
        self.__name = ""
        self.__age = -1
        self.set_name(name)
        self.set_age(age)

    def get_counter(self):
        return self.__counter

    def __str__(self):
        return "Человеку по имени {} {} лет".format(self.__name, self.__age)

    def set_name(self, new_name):
        if bool(re.search(r"\d", new_name)):
            print("Имя должно содержать только буквы! Непринятый вариант имени: {}".format(new_name))
        else:
            print("Меняем имя человека на {}\n".format(new_name))
            self.__name = new_name

    def set_age(self, new_age):
        if new_age not in range(1, 100):
            print("Возраст должен быть более 0 и менее 100! "
                  "Вы пробовали назначить {} как возраст человека".format(new_age))
        else:
            print("Меняем возраст {} на {}\n".format(self.__name, new_age))
            self.__age = new_age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


vlad = Man("Vlad", 25)

print(vlad)
print(vlad.get_age())
print(vlad.get_name())
print("-"*90)

vlad.set_age(26)
vlad.set_name("Vladyslav")
print(vlad)
print("-"*90)

vlad.set_age(126)
vlad.set_name("Vladyslav1")
print(vlad)
print("-"*90)

print("Так делать не стоит: ")
vlad._Man__age = 10
vlad._Man__name = "Памилка"
print(vlad)
print("-"*90)
