n_list = []
trash_list = []
cells_count = int(input("Введите количество клеток: "))

for i in range(cells_count):
    print("Введите эффективность клетки номер", i, ":", end = " ")
    eff = int(input())
    n_list.append(eff)

for i in range(len(n_list)):
    if n_list[i] < i:
        trash_list.append(n_list[i])

print("Не подходящие значения:", trash_list)