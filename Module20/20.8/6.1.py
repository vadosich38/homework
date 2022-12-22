nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list()
for num in enumerate(nums):
    if num[0] % 2 == 0:
        my_tuple = (nums[num[1]], nums[num[1]+1])
        new_list.append(my_tuple)
    else:
        continue

print(new_list)