count = int(input("Введите коичество сотрудников в офисе: "))
list_id = []
flag = False
for _ in range(count):
    id = int(input("Введите айди пропуска сотрудника: "))
    list_id.append(id)

search_id = int(input("Введите айди искомого пропуска: "))

for i in list_id:
    if i == search_id:
        flag = True

if flag:
    print("Сотрудник на рабочем месте")
else:
    print("Сотрудник не работает")