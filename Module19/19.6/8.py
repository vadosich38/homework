import random
maximum_n = int(input("Введите максимальное число: "))
n = random.randint(1, maximum_n)
#print("Загаданное число:", n)

while True:
    cmd = input("Угадай числа: ")
    if cmd == "Помогите!":
        print("Артём мог загадать следующие числа:",  *(set_true - set_false))
        break
    else:
        cmd_list_str = cmd.split()
        cmd_list_int = list(map(int, cmd_list_str))
        cmd_set = set(cmd_list_str)
        if cmd_set == n:
            print("Вы угадали число!")
            break
        elif n in cmd_set:
            print("В этой последовательности есть загаданое число!")
            set_true = cmd_set
        elif n not in cmd_set:
            print("Не угадали! Попробуйте заново!")
            set_false = cmd_set


