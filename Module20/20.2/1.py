import random

list1 = [random.randint(0, 6) for _ in range(10)]
cort1 = tuple(list1)
list2 = [random.randint(-5, 0) for _ in range(10)]
cort2 = tuple(list2)
list3 = list1 + list2
cort3 = tuple(list3)

print("Кортеж 3:", cort3)

print("В третьем кортеже {} нулей".format(cort3.count(0)))
