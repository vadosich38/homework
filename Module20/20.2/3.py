import random

def change(nums):
    nums = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums[index] = value
    return tuple(nums), value

my_nums = 1, 2, 3, 4, 5

new_nums1, rand_val1 = change(my_nums)
print(new_nums1, rand_val1)
new_nums2, rand_val2 = change(my_nums)
print(new_nums2, "{} + {} =".format(rand_val1, rand_val2), rand_val1+rand_val2)