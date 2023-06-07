class Person:
    def __init__(self, age, sur_name, second_name, city, country):
        self.__age = age
        self.__sur_name = sur_name
        self.__second_name = second_name
        self.__city = city
        self.__country = country

    def __str__(self):
        return "Данные человека:\nВозраст: {}\tИмя: {}\tФамилия: {}\tГород: {}\tСтрана: {}".format(self.__age,
                                                                                                   self.__sur_name,
                                                                                                   self.__second_name,
                                                                                                   self.__city,
                                                                                                   self.__country)

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age) -> None:
        self.__age = age

    @property
    def sur_name(self) -> str:
        return self.__sur_name

    @sur_name.setter
    def sur_name(self, sur_name) -> None:
        self.__sur_name = sur_name

    @property
    def second_name(self) -> str:
        return self.__second_name

    @second_name.setter
    def second_name(self, second_name) -> None:
        self.__second_name = second_name

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city) -> None:
        self.__city = city

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country) -> None:
        self.__country = country


pers1 = Person(age=26, sur_name="Vlad", second_name="Sa", city="Naumburg", country="Germany")
pers2 = Person(age=20, sur_name="Olya", second_name="Pe", city="Naumburg", country="Germany")
pers3 = Person(age=67, sur_name="Andrea", second_name="Zi", city="Jena", country="Germany")
pers4 = Person(age=70, sur_name="Durkai", second_name="Di", city="Naumburg", country="Germany")
pers5 = Person(age=53, sur_name="Tatyana", second_name="Ap", city="Zaporizhzhya", country="Ukraine")
pers6 = Person(age=71, sur_name="Joe", second_name="Ba", city="Washington", country="USA")

persons_list = [pers1, pers2, pers3, pers4, pers5, pers6]

print("Сортируем список персон от младшего к старшему")
sorted_list = (sorted(persons_list, key=lambda sort_pers: sort_pers.age))
for per in sorted_list:
    print(per)

print("\nСортируем список персон от старшего до младшего")
sorted_list = (sorted(persons_list, key=lambda sort_pers: -sort_pers.age))
for per in sorted_list:
    print(per)
