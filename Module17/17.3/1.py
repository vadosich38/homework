a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

honest = [x for x in range(a, b) if x % 2 == 0]
print(honest)