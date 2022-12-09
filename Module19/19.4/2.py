import random
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
#первая задача
print("\nПреобразовал список в множество")
nums_1_set = set(nums_1)
nums_2_set = set(nums_2)
print("Первое множество:", nums_1_set)
print("Второе множество:", nums_2_set)

#вторая задача
print("\nУдалил минимальное значение")
nums_1_set.remove(min(nums_1_set))
nums_2_set.remove(min(nums_2_set))
print("Первое множество:", nums_1_set)
print("Второе множество:", nums_2_set)

print("\nДобавил случайное число от 100 до 200")
nums_1_set.add(random.randint(100, 200))
nums_2_set.add(random.randint(100, 200))
print("Первое множество:", nums_1_set)
print("Второе множество:", nums_2_set)

#третяя задача
print("Все элементы множеств:", nums_1_set.union(nums_2_set))
print("Пересечение множеств:", nums_1_set.intersection(nums_2_set))
print("Элементы, входящие в nums_2, но не входящие в nums_1:", nums_2_set.difference(nums_1_set))
