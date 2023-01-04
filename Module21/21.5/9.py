count = int(input("Введите количество дисков: "))

def move(balls, start, finish):
    if balls == 1:
        print("Переставьте кольцо {0} на столб {1}".format(balls, finish))
    else:
        temp = 6 - (start+finish)
        move(balls-1, start, temp)
        print("Переставьте кольцо {0} на столб {1}".format(balls, finish))
        move(balls - 1, temp, finish)
move(count, 1, 3)
