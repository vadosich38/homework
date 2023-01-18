sale = 0


class Family:
    fam_name = "Deff"
    money = 100000
    have_a_house = False

    def info_print(self):
        print("Фамилия семьи: {}\n"
              "Сбережения семьи: {}\n"
              "Наличие дома у семьи: {}\n".format(self.fam_name, self.money, self.have_a_house))

    def incoming(self, incom_summ):
        self.money += incom_summ
        print("Семья заработала {}\n"
              "Сбережения семьи: {}\n".format(incom_summ, self.money))

    def hous_purchase(self, price, discount=0):
        price -= price * discount / 100
        if price <= self.money:
            self.money -= price
            self.have_a_house = True
            print("Семья купила дом за {}!\n"
                  "Сбережения семьи: {}\n".format(price, self.money))
        else:
            print("Для покупки дома недостаточно накоплений!\n"
                  "Сбережения семьи: {}\n"
                  "Цена дома: {}\n"
                  "Не хватает {}\n".format(self.money, price, price - self.money))


family_horsky = Family()
family_horsky.fam_name = "Horsky"
family_horsky.info_print()

family_horsky.incoming(100)
family_horsky.info_print()

while not family_horsky.have_a_house:
    family_horsky.hous_purchase(10**6, sale)
    if not family_horsky.have_a_house:
        family_horsky.incoming(250000)
        sale += 2
else:
    family_horsky.info_print()
