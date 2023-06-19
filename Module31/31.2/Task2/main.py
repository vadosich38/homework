import re

text = "How much \\wwood+?, would a \\wwood+?chuck \\dwwood+, chuck if a \\wwood+?,chuck could chuck \\wwood?,"

print(text)
# ищем \wwood+?,

pattern = re.compile(r"\\wwood\+\?,")

print("Список всех упоминаний шаблона:", pattern.findall(text))

# ожидаемый результат
# Список всех упоминаний шаблона: ['\\wwood+?,', '\\wwood+?,']
