class Unit:
    def __init__(self):
        self.health = 100

    def damage(self, damage_count=0):
        print("Персонаж получает урон: {}".format(damage_count))


class Warrior(Unit):

    def damage(self, damage_count=0):
        print("Боевой персонаж получает урон {}".format(damage_count))
        self.health -= damage_count


class Civil(Unit):

    def damage(self, damage_count=0):
        print("Гражданский персонаж получает урон {}".format(damage_count*2))
        self.health -= damage_count*2


man1 = Warrior()
man1_1 = Warrior()
man2 = Civil()

print(man1.health)
man1.damage(damage_count=20)
print("Объект 1:", man1.health)
print("Объект 1_1:", man1_1.health)

man2.damage(damage_count=20)
