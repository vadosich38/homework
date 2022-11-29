list_phrase1 = []
list_phrase2 = []

phrase1 = input("Первое сообщение: ")
phrase2 = input("Второе сообщение: ")
list_phrase1.extend(phrase1)
list_phrase2.extend(phrase2)
count1 = list_phrase1.count("!")
count2 = list_phrase2.count("?")

if count1 > count2:
    print(phrase1, phrase2)
elif count1 < count2:
    print(phrase2, phrase1)
else:
    print("Ой")