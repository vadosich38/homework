first_list = []
sec_list = []
def deleting(name, count):
    for _ in range(count):
        first_list.remove(name)

print("Список 1")
for i_count in range(3):
    num = int(input("Введите число: "))
    first_list.append(num)

print("Список 2")
for i_count in range(7):
    num = int(input("Введите число: "))
    sec_list.append(num)

first_list.extend(sec_list)

for num in first_list:
    count = first_list.count(num)
    deleting(num, count-1)

print("Очищеный список:", first_list)