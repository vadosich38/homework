from typing import List

text: List = list(filter(lambda x: x.isalpha() and x.islower(), input("Введите строку: ")))

print(text)


