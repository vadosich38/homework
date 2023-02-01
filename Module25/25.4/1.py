class Unit:
    def __init__(self):
        self.__health = 100

    def damage(self, damage_count=0):
        print("Персонаж получает урон: {}".format(damage_count))

    def get_health(self):
        return self.__health

    def set_health(self, count):
        self.__health -= count


class Warrior(Unit):

    def damage(self, damage_count=0):
        print("Боевой персонаж получает урон {}".format(damage_count))
        self.set_health(damage_count)


class Civil(Unit):

    def damage(self, damage_count=0):
        print("Гражданский персонаж получает урон {}".format(damage_count*2))
        self.set_health(damage_count*2)


man1 = Warrior()
man1_1 = Warrior()
man2 = Civil()

print("Здоровье первого персонажа:", man1.get_health())
man1.damage(damage_count=20)
print("Здоровье первого персонажа:", man1.get_health())
print("Здоровье персонажа 1_1:", man1_1.get_health())
print()
man2.damage(damage_count=20)
print("Здоровье второго персонажа:", man2.get_health())

