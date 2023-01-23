class Warior:

    def __init__(self, name):
        self.hp = 100
        self.damage = 20
        self.name = name

    def kik(self, enemy):
        enemy.hp -= self.damage
        print("{} бъет {}а и наносит урон {} очков.\n"
              "У {} остается {} здоровья.\n".format(self.name, enemy.name, self.damage, enemy.name, enemy.hp))


damblrdor = Warior("Damblrdor")
wolan = Warior("Wolan")

while True:
    damblrdor.kik(wolan)
    if wolan.hp <= 0:
        print("Вижил Damblrdor")
        break
    wolan.kik(damblrdor)
    if damblrdor.hp <= 0:
        print("Выжил Wolan De Mort")
        break



