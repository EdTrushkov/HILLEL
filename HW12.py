class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other, y = 0):
        if isinstance(other, Vector):
            return self.x - other.x, self.y - other.y
        if isinstance((other, y), (int, float)):
            return self.x - other, self.y - y

    def __add__(self, other, y = 0):
        if isinstance(other, Vector):
            return self.x + other.x, self.y + other.y
        if isinstance((other, y), (int, float)):
            return self.x + other, self.y + y

    def __mul__(self, b):
        return self.x * b, self.y * b
