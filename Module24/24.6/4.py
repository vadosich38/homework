import random
hours = 0


class Parent:

    def __init__(self, p_name, p_age, c_list):
        self.name = p_name
        self.age = p_age
        self.child_list = c_list

    def per_data(self):
        print("Меня зовут {} и мне уже {} лет. А это мои дети: {}".format(self.name, self.age, self.child_list))

    def relaxing(self, child):
        child.relaxed = True
        print("{} успокоил(а) {}".format(self.name, child.name))

    def fooding(self, child):
        child.hunger = False
        print("{} накормил(а) {}".format(self.name, child.name))


class Children:

    def __init__(self, name, age, relaxed=True, hunger=False):
        self.name = name
        self.age = age
        self.relaxed = relaxed
        self.hunger = hunger


childrens = [Children("Екатерина", 2), Children("Олег", 44)]
mother = Parent("Ольга", 55, childrens)
father = Parent("Дмитрий", 47, childrens)

for i_child in childrens:
    if mother.age - i_child.age < 12:
        print("Матери {} {} лет. А ребенку {} {} лет. "
              "Разница менее 12 лет! "
              "Переназначте возраст ребенка!".format(mother.name, mother.age, i_child.name, i_child.age))
        i_child.age = int(input("Введите возраст ребенка: "))
        if father.age - i_child.age < 12:
            print("Отцу {} {} лет. А ребенку {} {} лет. "
                  "Разница менее 12 лет! "
                  "Переназначте возраст ребенка!".format(father.name, father.age, i_child.name, i_child.age))
            i_child.age = int(input("Введите возраст ребенка: "))

while True:
    crysys_time = random.randint(0, 24)
    if hours == 24:
        print("\nСутки закончились и начался новый день! Нажмите Enter чтобы посмотреть следующий день\n" + "-"*100)
        hours = 0
        input()
    if hours == crysys_time:
        print("\nНа часах {} часов, дети расстроенные и устроили истерику! Их нужно успокоить.".format(hours))
        for i_child in childrens:
            father.relaxing(i_child)
    if hours == 6 or hours == 12 or hours == 18:
        print("\nНа часах {} часов, пора кушать! Дети голодные!".format(hours))
        for i_child in childrens:
            mother.fooding(i_child)
    hours += 1




