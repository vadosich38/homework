import math


class Round:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        s = math.pi * self.r ** 2
        return s

    def perimetr(self):
        p = 2 * math.pi * self.r
        return p

    def multipy(self, multipricker):
        self.r *= multipricker

    def crossing(self, r2, x2, y2):
        diff = max(abs(self.x - x2), abs(self.y - y2))
        if (self.r + r2) > diff:
            return True
        else:
            return False


round1 = Round()
round2 = Round(10, 2, 1)

while not (round1.crossing(round2.r, round2.x, round2.y)):
    print("Круги не пересекаются!"
          "\nПлощадь первого круга: {}"
          "\nПеремитр первого круга: {}"
          "\nПлощадь второго круга: {}"
          "\nПеремитр второго круга: {}".format(round1.square(), round1.perimetr(), round2.square(), round2.perimetr()))
    print("\nУвеличиваю второй круг в 2 раза!\n")
    round2.multipy(2)
else:
    print("Круги пересекаются!"
          "\nПлощадь первого круга: {}"
          "\nПеремитр первого круга: {}"
          "\nПлощадь второго круга: {}"
          "\nПеремитр второго круга: {}".format(round1.square(), round1.perimetr(), round2.square(), round2.perimetr()))



