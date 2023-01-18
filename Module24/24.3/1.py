import random


class Toyota:
    color = "Red"
    price = 150000
    max_speed = 200
    fact_speed = 0

    def info_print(self):
        print("Цвет машины: {}\n"
              "Цена машины: {}\n"
              "Максимальная скорость машины: {}\n"
              "Фактическая скорость: {}\n".format(self.color, self.price, self.max_speed, self.fact_speed))

    def fact_speed_change(self, new_speed):
        self.fact_speed = new_speed


car1 = Toyota()
car1.fact_speed = random.randint(0, 200)

car2 = Toyota()
car2.fact_speed = random.randint(0, 200)

car3 = Toyota()
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
