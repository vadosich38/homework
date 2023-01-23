import random
flag = True


def handout(player, count):
    for _ in range(count):
        card_num = random.randint(1, 52)
        new_card = Card(card_num, player)
        player.cards_list.append(new_card)


class Player:

    def __init__(self, name):
        self.name = name
        self.cards_list = list()
        self.summ = 0

    def data_print(self):
        print("\nУ игрока {} на руках суммарно: {}\n\nТакие карты:".format(self.name, self.summ))
        for index in range(len(self.cards_list)):
            print(self.cards_list[index].name)


class Card:
    cards = {1: ("2 чирва", 2), 2: ("2 бубна", 2), 3: ("2 пика", 2), 4: ("2 крест", 2),
             5: ("3 чирва", 3), 6: ("3 бубна", 3), 7: ("3 пика", 3), 8: ("3 крест", 3),
             9: ("4 чирва", 4), 10: ("4 бубна", 4), 11: ("4 пика", 4), 12: ("4 крест", 4),
             13: ("5 чирва", 5), 14: ("5 бубна", 5), 15: ("5 пика", 5), 16: ("5 крест", 5),
             17: ("6 чирва", 6), 18: ("6 бубна", 6), 19: ("6 пика", 6), 20: ("6 крест", 6),
             21: ("7 чирва", 7), 22: ("7 бубна", 7), 23: ("7 пика", 7), 24: ("7 крест", 7),
             25: ("8 чирва", 8), 26: ("8 бубна", 8), 27: ("8 пика", 8), 28: ("8 крест", 8),
             29: ("9 чирва", 9), 30: ("9 бубна", 9), 31: ("9 пика", 9), 32: ("9 крест", 9),
             33: ("10 чирва", 10), 34: ("10 бубна", 10), 35: ("10 пика", 10), 36: ("10 крест", 10),
             37: ("валет чирва", 10), 38: ("валет бубна", 10), 39: ("валет пика", 10), 40: ("валет крест", 10),
             41: ("дама чирва", 10), 42: ("дама бубна", 10), 43: ("дама пика", 10), 44: ("дама крест", 10),
             45: ("король чирва", 10), 46: ("король бубна", 10), 47: ("король пика", 10), 48: ("король крест", 10),
             49: ("туз чирва", 1, 11), 50: ("туз бубна", 1, 11), 51: ("туз пика", 1, 11), 52: ("туз крест", 1, 11)}

    def __init__(self, num, player):
        self.name = self.cards[num][0]
        if "туз" in self.cards[num][0]:
            if player.summ + 11 <= 21:
                player.summ += self.cards[num][2]
            else:
                player.summ += self.cards[num][1]
        else:
            player.summ += self.cards[num][1]
        self.num = self.cards[num][1]


kostya = Player("Костя")
crupie = Player("Крупье")

print("\nСдаем первые две карты!")
handout(kostya, 2)
handout(crupie, 2)
kostya.data_print()

while True:
    if kostya.summ == 21:
        print("\n!!!! Игрок {} собрал 21 очко и побеждает !!!!".format(kostya.name))
        flag = False
        break
    elif kostya.summ > 21:
        print("\n!!!! Игрок {} набрал более 21 очка и сгорает !!!!".format(kostya.name))
        crupie.data_print()
        flag = False
        break

    choise = int(input("\n1 - взять еще, 2 - остановиться: "))
    if choise == 1:
        handout(kostya, 1)
        kostya.data_print()
    elif choise == 2:
        break

if flag:
    print("Вскрываемся!")
    crupie.data_print()
    kostya.data_print()

    if crupie.summ > kostya.summ:
        print("\n!!!! Костя проиграл !!!!")
    elif crupie.summ == kostya.summ:
        print("\n !!!! НИЧЬЯ !!!!")
    else:
        print("\n!!!! Костя выиграл !!!!")




