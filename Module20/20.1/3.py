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

# изначально есть кортеж из пяти чисел.
# Затем вызывается функция, которая получает на вход кортеж чисел,
#     генерирует случайный индекс и случайное значение,
#     а затем по этим индексу и значению меняет сам кортеж.
# Функция должна возвращать кортеж и случайное значение.
#
# В основном коде функция используется два раза,
# и на экран два раза выводится новый кортеж и случайное значение.
# Причём второй раз выводится сумма первого случайного значения и второго.

