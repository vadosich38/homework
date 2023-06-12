from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# функция map перебирает элементы списка и применяет к ним функцию lambda, которая возводит элемент списка в куб
new_floats: List[float] = list(map(lambda x: round((x ** 3), 3), floats))
# функция filter перебирает элементы списка и применяет к ним функцию lambda, которая возвращает элементы длинее 5
new_names: List[str] = list(filter(lambda x: len(x) >= 5, names))
# функция reduce перебирает элементы списка и применяет к ним функцию lambda, которая возвращает произведение
# проитерированных элементов и следующий элемент
new_numbers: List[int] = [reduce(lambda my_summ, num: my_summ * num, numbers)]

print(new_floats)
print(new_names)
print(new_numbers)
