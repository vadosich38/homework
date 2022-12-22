nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
new_list = list()
def paar_maker(list, start):
    return list[start], list[start+1]

for _ in range(len(nums) // 2):
    new_list.append(paar_maker(nums, index))
    index += 2

print(new_list)