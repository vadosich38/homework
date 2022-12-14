import math
r = int(input("Введите радиус: "))
hight = int(input("Введите высоту: "))

def calculate(r, hight):
    surface_squar = hight * ((r * 2) * math.pi)
    full_squar = surface_squar + 2*(math.pi*r**2)
    return surface_squar, full_squar

bok_squar, full_squar = calculate(r, hight)
print("Площадь боковой поверзности равна {0}, полная площадь цилиндра равна {1}".format(round(bok_squar, 2), round(full_squar, 2)))
