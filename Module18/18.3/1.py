words_list = input("Введите поисковые слова: ").split(", ")
text_list = input("Введите текст: ").split(" ")
counter_list = [0 for _ in range(len(words_list))]
index = 0
for search_word in words_list:
    for word in text_list:
        if search_word == word:
            counter_list[index] += 1
    index += 1

for index in range(len(counter_list)):
    print("Слово", words_list[index], "встречались столько раз:", counter_list[index])