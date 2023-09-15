from abc import ABCMeta, abstractmethod
import math

class Figure():
    __metaclass__=ABCMeta


    @abstractmethod
    def get_area(self):
        """Площадь фигуры"""


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        global s
        a, b, c = sorted([self.a, self.b, self.c])
        if a * a + b * b == c * c:
            area = (a*b)/2
        else:
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area