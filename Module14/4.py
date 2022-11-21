n = float(input("Введите первое число: "))
k = float(input("Введите второе число: "))

def rev (num):
    unit = num // 1
    shot = round(num - unit, 5)

    unit_rev = str(unit)[::-1]
    shot_rev = str(shot)[::-1]

    while float(shot_rev) > 1:
        shot_rev = float(shot_rev) / 10
    while float(unit_rev) % 1 > 0.01:
        unit_rev = float(unit_rev) * 10

    rev_num = float(round(unit_rev)) + float(shot_rev)
    return rev_num

print("Первое число наоборот: ", rev(n))
print("Второе число наоборот: ", rev(k))