while True:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третее число: "))
    num4 = int(input("Введите четвертое число: "))
    if int(num1) > 250 or int(num2) > 250 or int(num3) > 250 or int(num4) > 250:
        print("Ошибка! Число должно быть меньше 250!")
    else:
        break
ip_address = "{num1}.{num2}.{num3}.{num4}".format(
                                                num1=num1,
                                                num2=num2,
                                                num3=num3,
                                                num4=num4)
print(ip_address)