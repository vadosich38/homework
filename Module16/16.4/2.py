n = int(input("Сколько участников олимпиады: "))
k = int(input("По сколько человек в команде: "))
members_list = []
i = 1
if n % k == 0:
    for member in range(n // k):
        members_list.append(list(range(i, i+k)))
        i += k
else:
    print(n, "участников невозможно поделить на команды по", k, "человек!")
print(members_list)