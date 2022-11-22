cards_count = int(input("Введите количество видеокарт: "))
cards_list = []
new_cards_list = []
max = 0


for i in range(cards_count):
    name = int(input("Введите номер видеокарты: "))
    cards_list.append(name)
for name in cards_list:
    if name > max:
        max = name
for name in cards_list:
    if name != max:
        new_cards_list.append(name)

print("Старый список видеокарт:", cards_list)
print("Новый список:", new_cards_list)