import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Life:
    __max_carma = 500
    __carma = 0

    def one_day(self):
        variable = random.randint(1, 50)
        if self.__carma >= self.__max_carma:
            print("Человек достиг максимального уровня кармы: {} из {} максимум".format(self.__carma, self.__max_carma))
            return True
        elif variable % 10 == 0:
            try:
                if variable == 10:
                    raise KillError("Совершено убийство!")
                elif variable == 20:
                    raise DrunkError("Персонаж напился!")
                elif variable == 30:
                    raise CarCrashError("Персонаж разбил машину!")
                elif variable == 40:
                    raise GluttonyError("Персонаж объелся!")
                elif variable == 50:
                    raise DepressionError("У персонажа наступила депрессия!")
            except Exception as a:
                print("Возникла ошибка:", a)
                with open("karma.log", "a", encoding="utf-8") as log_file:
                    log_file.write("Ошибка: {}\n".format(a))
        else:
            carma_score = random.randint(1, 7)
            self.__carma += carma_score
            self.data(carma_score)

    def data(self, new_value):
        print("Прошел день, заработано кармы - {}. Всего кармы: {}".format(new_value, self.__carma))


one_life = Life()
while True:
    data = one_life.one_day()
    if data:
        break
    else:
        continue



