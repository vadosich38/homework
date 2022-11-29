people_count = int(input("Сколько всего человек: "))
sdelok = int(input("Сколько всего расписок: "))

#формируем список
friends = [[0]*2 for _ in range(people_count)]
for num in range(people_count):
    friends[num][0] = num+1

for i_borg in range(sdelok):
    creditor = int(input("Номера занимавшего: "))
    bankir = int(input("Номер давшего в долг: "))
    summa = int(input("Сумма задолженности: "))
    friends[creditor-1][1] = friends[creditor-1][1] - summa
    friends[bankir-1][1] = friends[bankir-1][1] + summa

print("Баланс друзей:")
print(friends)