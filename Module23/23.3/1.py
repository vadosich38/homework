data = input("Введите строку: ")


try:
    res_file = open("233result.txt", "w", encoding="utf-8")
except FileNotFoundError:
    print("Ошибка! Файл с таким именем не найден!")
except IsADirectoryError:
    print("На открытие указна папка вместо файла!")
except:
    print("непредвиденная ошибка!")
else:
    try:
        res_file.write(data)
    except TypeError:
        print("Тип данных не строка, запись невозможна!")
    except:
        print("непредвиденная ошибка!")
    else:
        print("Файл успешно записан!")
    res_file.close()
finally:
    print("Процесс завершен!")