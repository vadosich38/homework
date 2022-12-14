import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict1 = dict()
dict2 = dict()

list1 = [alphabet[random.randint(0, 25)] for _ in range(10)]
list2 = [alphabet[random.randint(0, 25)] for _ in range(10)]
print("Оригинальные списки:\n{}, \n{}".format(list1, list2))

for index, value in enumerate(list1):
    dict1[index] = value

for index, value in enumerate(list2):
    dict2[index] = value

print("Словари:\n{}, \n{}".format(dict1, dict2))