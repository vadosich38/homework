a = int(input("Введите число а: "))
b = int(input("Введите число b: "))

coubs = [a**3 for a in range(a,b+1)]
squers = [a**2 for a in range(a,b+1)]

print("Кубы чисел:", coubs)
print("Квадраты чисел", squers)
