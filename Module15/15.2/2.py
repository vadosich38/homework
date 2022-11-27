n = int(input("Введите количество чисел в спсике: "))
num_list = []
summ = 0
counter = 0

for _ in range (n):
    num = int(input("Введите число в спсиок: "))
    num_list.append(num)

k = int(input("Введите делитель: "))

for i in num_list:
    if i % k == 0:
        print("Индекс числа", i, ":", counter)
        summ += counter
    counter += 1

print("Сумма индексов:", summ)