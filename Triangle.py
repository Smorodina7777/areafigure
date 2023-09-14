from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        global s
        a, b, c = sorted([self.a, self.b, self.c])
        if a * a + b * b == c * c:
            area = (a*b)/2
        else:
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area









