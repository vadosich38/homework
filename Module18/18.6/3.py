start = "@№$%^&*()."
end_list = [".txt", ".docx"]
file_name = input("Введите имя файла: ")
name_end = file_name[file_name.find("."):]

if not file_name[0] in start:
    if name_end in end_list:
        print("Файл назван верно.")
    else:
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Ошибка: название начинается на один из специальных символов")

