asd = list()
amount = int(input('Сколько записей вносится в протокол? '))

for i in range(amount):
    user = input(f'{i + 1}-я запись: ').split()
    while True:
        if user[0] < '0' or '.' in user[0]:
            print('Попробуйте еще раз!')
            user = input(f'{i + 1}-я запись: ').split()
        else:
            user[0] = int(user[0])
            asd.append(tuple(user))
            break

print('\nИтоги соревнований:')

for i in range(3):
    max_number = 0
    max_name = ''
    for i_elem in asd:
        if i_elem[0] > max_number:
            max_number = i_elem[0]
            max_name = i_elem[1]
    for value in asd:
        if value[1] == max_name:
            asd.remove(value)
    print(f'{i + 1}-е место. {max_name} ({max_number})')