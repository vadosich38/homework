nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [nice_list[x][y][i] for x in range(len(nice_list)) for y in range(len(nice_list[0][0]))
                                                                                for i in range(len(nice_list[0][0]))]
print(new_list)
