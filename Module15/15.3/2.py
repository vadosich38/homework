s = input("Введите текст: ")
num = int(input("Введите номер символа: "))
num -= 1
sym_list = list(s)
collect = 0

print("Символ слева:", sym_list[num-1])
print("Символ справа:", sym_list[num+1])

if sym_list[num] == sym_list[num-1]:
    collect += 1
elif sym_list[num] == sym_list[num+1]:
    collect += 1

if collect == 0:
    print("Таких же символов нет.")
elif collect == 1:
    print("Есть ровно один такой же символ.")
elif collect == 1:
    print("Оба соседа такие же знаки")
