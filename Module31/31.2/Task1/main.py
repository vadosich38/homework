import re

text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
pattern = re.compile(r"wo")

print("Поиск шаблона в начале строки:", pattern.match(text))
print("Поиск первого найденного совпадения по шаблону:", pattern.search(text))
print("Содержимое найденной подстроки:", pattern.search(text).group())
print("Начальная позиция:", pattern.search(text).start())
print("Конечная позиция:", pattern.search(text).end())
print("Список всех упоминаний шаблона:", pattern.findall(text))
print("Текст после замены:", pattern.sub("ЗАМЕНА", text))

# Поиск шаблона в начале строки: None
# Поиск первого найденного совпадения по шаблону: <re.Match object; span=(9, 11), match='wo'>
# Содержимое найденной подстроки: wo
# Начальная позиция: 9
# Конечная позиция: 11
# Список всех упоминаний шаблона: ['wo', 'wo', 'wo', 'wo', 'wo']
# Текст после замены: How much ЗАМЕНАod ЗАМЕНАuld a ЗАМЕНАodchuck chuck if a ЗАМЕНАodchuck could chuck ЗАМЕНАod?