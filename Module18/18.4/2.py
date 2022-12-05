path = input("Введите путь к файлу: ")
drive = input("Введите название диска: ")
extention = input("Введите расширение файла: ")

if not path.startswith(drive):
    print("Ошибка, указан неверный диск!")
elif not path.endswith(extention):
    print("Ошибка, указано неверное расширение файла!")
else:
    print("Все верно!")