from typing import Callable


def singleton(cls: Callable) -> Callable:
    instanc_list = list()

    def decorated_class():
        if instanc_list:
            print("Инстанс уже создан, id:{}".format(id(instanc_list[0])))
            return instanc_list[0]
        else:
            instanc = cls()
            instanc_list.append(instanc)
            return instanc

    return decorated_class


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)

#Результат:
#1986890616688
#1986890616688
#True