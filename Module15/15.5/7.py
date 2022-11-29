count = int(input("Сколько контейнеров на складе: "))
mass_list = []
def input_chek_new_mass():
    x_mass = int(input("Введите массу нового контейнера: "))
    if x_mass >= 200:
        print("Ошибка! Масса не может быть больше 200! Повторите ввод!")
        input_chek_new_mass()
    return(x_mass)
def input_check(pos):
    print("Введите массу контейнера", pos + 1, ": ", end="")
    mass = int(input())
    if mass <= 200:
        mass_list.append(mass)
    else:
        print("Ошибка! Масса не может превышать 200!")
        input_check(pos)
def fill_list():
    for num in range(count):
        print("Введите массу контейнера", num+1, ": ", end = "")
        mass = int(input())
        if mass < 201:
            mass_list.append(mass)
        else:
            print("Ошибка! Масса не может превышать 200!")
            input_check(num)
def chek_pos():
    position = 0
    for mass in mass_list:
        if mass - x_mass >= 0:
            position += 1

    mass_list.insert(position, x_mass)
    print("Обновленный список:", mass_list)
    print("Позиция нового контейнера:", position+1)

fill_list()
x_mass = input_chek_new_mass()
chek_pos()
