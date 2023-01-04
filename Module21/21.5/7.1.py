from typing import Iterable

def sum_(*args):
    return sum(sum_(*arg) if isinstance(arg, Iterable) else arg for arg in args)

assert sum_([[1, 2, [3]], [1], 3])
assert sum_(1, 2, 3, 4, 5)