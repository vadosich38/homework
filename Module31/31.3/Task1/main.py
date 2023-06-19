import re

text = "Even if they are djinns, I will get djinns that can outdjinn them."
# Первый содержит все слова, которые начинаются на гласную букву латинского алфавита
# (в этот раз слово может состоять и из одной буквы, например I).
pattern1 = re.compile(r"\b[AEIOUYaeiouy]\w*")
result1 = pattern1.findall(text)
print("Слова на гласную:", result1)

# Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
# исключаем пробел, запятую, точку и гласные буквы
pattern2 = re.compile(r"\b[^ ,.AEIOUYaeiouy]\w*")
result2 = pattern2.findall(text)
print("Слова на любой символ, кроме гласной:", result2)


# Ожидаемый результат:
# Слова на гласную: ['Even', 'if', 'are', 'I', 'outdjinn']
# Слова на любой символ, кроме гласной: ['they', 'djinns', 'will', 'get', 'djinns', 'that', 'can', 'them']
