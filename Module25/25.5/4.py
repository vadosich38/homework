class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def ger_surname(self):
        return self.__surname


class Employee(Person):
    def salary_count(self):
        pass

    def data(self):
        return "{} {}".format(self.get_name(), self.ger_surname())


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.position = "Менеджер"

    def salary_count(self):
        return 13000


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours
        self.position = "Рабочий"

    def salary_count(self):
        salary = self.__hours * 100
        return salary


class Agent(Employee):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales
        self.position = "Агент"

    def salary_count(self):
        salary = 5000 + (self.__sales * 0.05)
        return salary


mike_manager = Manager(name="Mike", surname="Tur", age=45)
sam_worker = Worker(name="Sam", surname="Gog", age=25, hours=250)
gorg_agent = Agent(name="Gorg", surname="Tio", age=30, sales=1000000)

print("Зарплаты сотрудников компании:\n"
      "{} на должности {} заработал {}\n"
      "{} на должности {} заработал {}\n"
      "{} на должности {} заработал {}\n".format(mike_manager.data(), mike_manager.position,
                                                 mike_manager.salary_count(), sam_worker.data(), sam_worker.position,
                                                 sam_worker.salary_count(), gorg_agent.data(), gorg_agent.position,
                                                 gorg_agent.salary_count()))

