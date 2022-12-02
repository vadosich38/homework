import random
num_list = [random.randint(-400, 400) for _ in range(20)]
a = random.randint(1, 5)
b = random.randint(5, 20)

print("Стартовый список:", num_list)
print(a, b)
print("Новый список:", num_list[:a] + num_list[b:])