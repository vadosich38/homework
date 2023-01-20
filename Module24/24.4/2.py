class Dot:
    counter = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.id = Dot.counter
        Dot.counter += 1

    def data_print(self):
        print("Точка номер {} имеет координаты:\nx = {}\ny = {}\n".format(self.id+1, self.x, self.y))


dot1 = Dot(1, 2)
dot2 = Dot(2, 1)
dot1.data_print()
dot2.data_print()
print("Создано точек:", Dot.counter)

