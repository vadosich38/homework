from typing import Iterable
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def multiply(nums1: list, nums2: list, search: int) -> Iterable[tuple]:
    for x in list_1:
        for y in list_2:
            result = x * y
            yield x, y, result
            if result == to_find:
                print('Found!!!')
                return


my_f = multiply(nums1=list_1, nums2=list_2, search=to_find)
for i_res in my_f:
    print(i_res)
