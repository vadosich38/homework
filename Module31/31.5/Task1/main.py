import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

pattern = re.compile(r"\b\w{4}\b")
res = pattern.findall(text)
print(res)

# Результат:
# ['amet', 'elit', 'eget', 'quam', 'quis', 'quis', 'enim', 'pede']