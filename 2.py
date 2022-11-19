x1 = float(input("Введите первую точку \nX:"))
y1 = float(input("\nY:"))

x2 = float(input("\nВведите первую точку \nX:"))
y2 = float(input("\nY:"))

x_diff = x1 - x2
y_diff = y1 - y2

if x_diff == 0:
    k = 0
else:
    k = y_diff / x_diff

b = y2 - k * x2
print("Уравнение прямой проходящей через эти точки:")
print("y = ", k, "* x + ", b)