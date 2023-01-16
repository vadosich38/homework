words_file = open("words.txt", "r", encoding="utf-8")
log_file = open("errors.log", "a", encoding="utf-8")
words = words_file.read().split()
words_file.close()
counter = 0
pal_counter = 0

for i_word in words:
    counter += 1
    try:
        if not i_word.strip().isalpha():
            raise ValueError("{0} - это слово состоит не только из букв! Номер слова {1}".format(i_word.strip(),
                                                                                                            counter))
        else:
            if i_word.strip() == i_word.strip()[::-1]:
                print("Слово '{}' является палиндромом!".format(i_word))
                pal_counter += 1
            else:
                print("Слово '{}' не является палиндромом!".format(i_word))
    except ValueError:
        print("Ошибка! '{0}' - это слово состоит не только из букв! Слово номер {1}".format(i_word.strip(), counter))
        log_file.write("'{0}' - это слово состоит не только из букв! Слово номер {1}\n".format(i_word.strip(), counter))
    finally:
        print("Всего обнаружено палиндромов: {}".format(pal_counter))
        log_file.close()