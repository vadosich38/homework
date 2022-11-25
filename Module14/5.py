n = int(input("Введите число больше единицы: "))
dell = 2

while True:
    if n % dell < 0.01:
        print("Наименьший делитель:", dell)
        break
    else:
        dell += 1