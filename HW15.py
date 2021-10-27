
class Figures:
    pi = 3.14

    def area_S(self):
        pass

    def perimeter_P(self):
        pass

class Circle(Figures):
    def __init__(self, diameter):
        self.D = diameter
        self.R = diameter/2

    def perimeter_P(self):
        return 2 * self.pi * self.R

    def area_S(self):
        return self.pi * self.R ** 2

class Triangel(Figures):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area_S(self):
        p = (self.a + self.b + self.c)/2
        return p ** (0.5) * (p - self.a) * (p - self.b) * (p - self.c)

    def perimeter_P(self):
        return self.a + self.b + self.c

class Square(Figures):
    def __init__(self, a):
        self.a = a

    def area_S(self):
        return self.a ** 2

    def perimeter_P(self):
        return 4 * self.a
