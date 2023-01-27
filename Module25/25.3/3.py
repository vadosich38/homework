my_list = list()


class DivisionError(Exception):
    pass


with open("numbers.txt", "r", encoding="utf-8") as file:
    for i_string in file:
        my_list.append(i_string.split())
        try:
            if int(my_list[0][0]) < int(my_list[0][1]):
                raise DivisionError("Первое число - {} меньше второго - {}".format(my_list[0][0], my_list[0][1]))
            res = round(int(my_list[0][0]) / int(my_list[0][1]), 2)
            print("{} / {} = {}".format(my_list[0][0], my_list[0][1], res))
        except DivisionError:
            print("Данную пару чисел нельзя разделить: {} {}, "
                  "первое число меньше второго".format(my_list[0][0], my_list[0][1]))
        except ZeroDivisionError:
            print("На ноль делить нельзя: {} и {}".format(my_list[0][0], my_list[0][1]))
        finally:
            my_list.clear()
