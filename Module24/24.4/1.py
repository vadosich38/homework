import random


class Toyota:

    def __init__(self, color, price, max_speed, fact_speed):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.fact_speed = fact_speed

    def info_print(self):
        print("Цвет машины: {}\n"
              "Цена машины: {}\n"
              "Максимальная скорость машины: {}\n"
              "Фактическая скорость: {}\n".format(self.color, self.price, self.max_speed, self.fact_speed))

    def fact_speed_change(self, new_speed):
        self.fact_speed = new_speed


car1 = Toyota("Red", 100000, 200, 10)
car1.fact_speed = random.randint(0, 200)

car2 = Toyota("Black", 110000, 200, 24)
car2.fact_speed = random.randint(0, 200)

car3 = Toyota("Metalic", 99000, 200, 0)
car3.fact_speed = random.randint(0, 200)

print("Первый вывод:", car1.fact_speed, car2.fact_speed, car3.fact_speed)

print("Второй вывод:")
car1.info_print()
car2.info_print()
car3.info_print()


car1.fact_speed_change(100)
car2.fact_speed_change(10)
car3.fact_speed_change(900)
print("Третий вывод:", car1.fact_speed, car2.fact_speed, car3.fact_speed)
