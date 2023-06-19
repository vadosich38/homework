import re

text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
pattern = re.compile(r"How")
result = pattern.match(text)

print("result.groups()", result.groups()) #этот метод возвращает все найденные подгруппы в tuple
print("result.group()", result.group()) #этот метод возвращает полное совпадение (или совпадение конкретной подгруппы)
print("result.groupdict()", result.groupdict()) #возвращает словарь в формате "искомый ключ":"найденное значение ключа"

print()
print("result.start()", result.start()) #начало вхождения в искомой строке
print("result.end()", result.end()) #конец вхождения в искомой строке

print()
print("result.span()", result.span()) #диапазон вхождения в искомой строке