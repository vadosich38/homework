data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

def search(dict):
    search_list = input("Введите серию и номер паспорта через пробел: ").split()
    for i_key, i_value in dict.items():
        if i_key[0] == int(search_list[0]) and i_key[1] == int(search_list[1]):
            print("Фамилия: {0} \nИмя: {1}".format(i_value[0], i_value[1]))
search(data)