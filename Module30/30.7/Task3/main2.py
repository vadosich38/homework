from collections import Counter


def can_be_poly(text: str) -> bool:
    """
    Проверка, можно ли из поданой строки перестановкой сделать палиндром. В палиндромах с нечетным количеством букв
    останется только одна буква без пары. В палиндромах с четным количеством букв, все буквы имеют пару.
    :param text: входная строка
    :return: истина или ложь (выполняется ли условие выражения: остаток от деления текста на 2 равен сумме остатков
    деления количества букв в тексте на 2)
    """
    return len(text) % 2 == sum(x % 2 for x in Counter(text).values())


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('refer'))
print(can_be_poly('noon'))
print(can_be_poly('stuhl'))
print(can_be_poly('acbba'))
