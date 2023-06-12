from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

# функция лямбда map перебирает два списка и применяет функцию lambda, которая возвращает кортеж состоящий из элементов
# обоих списков равных по индексу и записывает этот кортеж в список
new_list: List[tuple] = list(map(lambda num, let: (num, let), letters, numbers))
print(new_list)
