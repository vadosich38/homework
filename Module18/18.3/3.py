template = input("Введите шаблон поздравления с {name} и {age}: ")
names_list = input("Введите имена людей: ").split(", ")
ages_list = input("Введите возраст всех людей через пробел: ").split()

for index in range(len(names_list)):
    print(template.format(
                            name = names_list[index],
                            age = ages_list[index]))

people_list = [
            " ".join([names_list[index], str(ages_list[index])])
            for index in range(len(names_list))]
people_str = ", ".join(people_list)
print("\nИменниники:", people_str)
