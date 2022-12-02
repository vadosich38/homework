nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
for i1 in range(len(nice_list)-1):
    for i2 in range(8):
        nice_list.extend(nice_list[i1])
        nice_list.remove(nice_list[i1])

print(nice_list)

#Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]