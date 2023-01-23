import random


class Warior:

    def __init__(self, name):
        self.hp = 100
        self.name = name

    def kik(self, enemy):
        damage = random.randint(1, 25)
        enemy.hp -= damage
        print("{} бъет {}а и наносит урон {} очков.\n"
              "У {} остается {} здоровья.\n".format(self.name, enemy.name, damage, enemy.name, enemy.hp))


def fight(warior1, warior2):
    while True:
        start = random.randint(0, 1)
        if start == 1:
            warior1.kik(warior2)
            if warior2.hp <= 0:
                print("Выжил Damblrdor!")
                break
        else:
            warior2.kik(warior1)
            if warior1.hp <= 0:
                print("Выжил Wolan De Mort")
                break


damblrdor = Warior("Damblrdor")
wolan = Warior("Wolan")

fight(damblrdor, wolan)





