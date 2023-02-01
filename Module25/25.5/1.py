goods_dict = {"car": 0, "apartment": 0, "house": 0}


class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculating(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculating(self):
        self.__tax_sum = self.worth / 1000
        return self.__tax_sum


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculating(self):
        self.__tax_sum = self.worth / 200
        return self.__tax_sum


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculating(self):
        self.__tax_sum = self.worth / 500
        return self.__tax_sum


money = int(input("Сколько у вас есть денег: "))

while True:
    good = input("Введите каким имуществом вы владеете и его стоимость. "
                 "Например: car/apartment/house 190000. "
                 "Введите x, если вы ввели все свое имущество: ")
    if good == "x":
        break
    try:
        category, price = good.strip().split()

        if category == "car":
            goods_dict[category] += int(price)
        elif category == "apartment":
            goods_dict[category] += int(price)
        elif category == "house":
            goods_dict[category] += int(price)
    except Exception as a:
        print("Возникла ошибка, ввод не корректный. Текст ошибки:", a)

cars = Car(int(goods_dict["car"]))
apartments = Apartment(int(goods_dict["apartment"]))
houses = CountryHouse(int(goods_dict["house"]))

cars_tax = cars.calculating()
apartments_tax = apartments.calculating()
houses_tax = houses.calculating()
sum_taxes = cars_tax + apartments_tax + houses_tax

print("\nВаши налоги:"
      "\nЗа автомобили: {}"
      "\nЗа квартиры: {}"
      "\nЗа дома: {}"
      "\nСуммарно: {}".format(cars_tax, apartments_tax, houses_tax, sum_taxes))

if sum_taxes > money:
    print("Вам не хватает {} чтобы оплатить налоги!".format(money-sum_taxes))
else:
    print("Вы оплатили все налоги и у вас осталось {} денег".format(money - sum_taxes))
