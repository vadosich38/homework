def user_quation(quation, error_msg="Ошибка, ввод не корректный!", nums=4):
    while True:
        answer = input(quation)
        if answer == "да":
            return 1
        elif answer == "нет":
            return 0
        else:
            nums -= 1
            print(error_msg)
            if nums == 0:
                break
            print("Осталось попыток {}".format(nums))


user_quation("Вы действительно хотите выйти?", error_msg="Неверный ввод. Пожалуйста, введите 'да' или 'нет'.", nums=3)
user_quation("Удалить файл?", error_msg="Так удалить или нет?", nums=3)

user_quation("Записать файл?")
user_quation("Записать файл?", error_msg="Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
user_quation("Записать файл?", nums=6)

