def pass_check():
    password = input("Введите пароль: ")
    nums_in_pass = [num for num in password if num.isdigit()]
    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов!")
        pass_check()
    elif password.islower():
        print("Пароль должен содержать минимум одну большую букву!")
        pass_check()
    elif len(nums_in_pass) < 3:
        print("Пароль должен содержать минимум три цифры!")
    else:
        print("Пароль подходит.")

pass_check()