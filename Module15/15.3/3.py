search_word_list = []
counts = [0, 0, 0]

for _ in range (3):
    word = input("Введите поисковое слово: ")
    search_word_list.append(word)

while word != "end":
    word = input("Введите слово текста: ")
    for i in range(3):
        if word == search_word_list[i]:
            counts[i] += 1

for i in range (3):
    print("\nСлово", search_word_list[i], "встречается:", counts[i], "раз")