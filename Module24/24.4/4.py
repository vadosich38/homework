#пример создания счетчика в классе
class Peoples:
    peoples_counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Peoples.peoples_counter += 1

    def info(self):
        print("Имя человека: {}, ему {} лет".format(self.name, self.age))


man1 = Peoples("Vlad", 25)
man2 = Peoples("Olya", 20)

print("Всего людей: ", Peoples.peoples_counter)
man1.info()
man2.info()
