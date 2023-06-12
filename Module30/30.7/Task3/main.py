from collections import deque


def can_be_poly(text: str) -> bool:
    """
    Функция проверяет, является ли поданый текст палиндромом, перебирая строку слева направо и справа налево одновременно,
    происходит сравнение знаков. Как только знаки не равны, возвращается False, если остался лишь один знак, возвращается
    истина True
    :param text: входящий текст
    :return: истина или ложь
    """
    text = text.replace(" ", "").lower()
    my_deque = deque(text)

    while len(my_deque) > 1:
        if my_deque.popleft() != my_deque.pop():
            return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('refer'))
print(can_be_poly('noon'))
print(can_be_poly('stuhl'))
print(can_be_poly('acbba'))
