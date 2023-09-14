from abc import ABCMeta, abstractmethod

class Figure():
    __metaclass__=ABCMeta

@abstractmethod
def area():
    """Площадь фигуры"""