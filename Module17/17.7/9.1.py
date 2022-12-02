nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#len1 = len(nice_list)
len2 = len(nice_list[0])
len3 = len(nice_list[0][0])

for i1 in range(len(nice_list)):
    for i2 in range(len(nice_list[0])):
        for _ in range(len3):
            nice_list.append(nice_list[i1][i2][0])
            nice_list[i1][i2].remove(nice_list[i1][i2][0])
#    nice_list.remove(nice_list[0])


print(nice_list)

#Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]