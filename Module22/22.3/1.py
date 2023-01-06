import os
list1 = list()
list2 = list()
summa = 0
diff = 0

file = open(os.path.abspath(os.path.join("..", "..", "..", "..", "..", "Documents", "task", "group_1.txt")),
                                                                                    "r", encoding="utf-8")
for i_line in file:
    info = i_line.split()
    list1.append(int(info[2]))
    summa = sum(list1)
    diff = list1[0]
    for num in range(1, len(list1)):
        diff -= list1[num]

file_2 = open(os.path.abspath(os.path.join("..", "..", "..", "..", "..", "Documents", "task", "group_2.txt")),
                                                                                    "r", encoding="utf-8")
for i_line in file_2:
    info = i_line.split()
    list2.append(int(info[2]))
compose = list2[0]
for num in range(1, len(list2)):
    compose *= list2[num]

print(summa)
print(diff)
print(compose)


