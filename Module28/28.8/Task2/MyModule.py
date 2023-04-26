import math
from abc import ABC


class MyMath(ABC):
    """
    Абстрактный класс с методами расчета по формулам
    """
    @classmethod
    def circle_len(cls, radius: int) -> float:
        "вычисление длины окружности"
        cl = 2 * math.pi * radius
        return cl

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        "вычисление площади окружности"
        cs = math.pi * radius**2
        return cs

    @classmethod
    def vol_cube(cls, len: int) -> float:
        "вычисление объёма куба"
        vc = len**3
        return vc

    @classmethod
    def sphere_surface_area(cls, radius: int) -> float:
        "вычисление площади поверхности сферы"
        ssa = math.pi * radius**2 * 4
        return ssa
