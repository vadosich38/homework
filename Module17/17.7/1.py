text = input("Введите текст: ")
vowels_letters = [letter for letter in text if letter == "а" or letter == "у"
                  or letter == "о" or letter == "ы" or letter == "и" or letter == "э"
                    or letter == "я" or letter == "ю" or letter == "ё" or letter == "е"]

print("Список гласных букв:", vowels_letters)
