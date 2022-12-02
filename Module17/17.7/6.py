num_list = [0, 2, 0, 5, 0, 0, 6, 5, 3, 5, 0]
indexes = [i for i, j in enumerate(num_list) if j == 0]
i = 0

for _ in range(len(indexes)):
    num_list.remove(0)
    num_list.append(0)

print(num_list)