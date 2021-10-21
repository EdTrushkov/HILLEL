import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def to_polar():
        return [math.atan2(y, x), math.sqrt(x ** 2 + y ** 2)]


x = int(input("Print first dekart coordinate: "))
y = int(input("Print second dekart coordinate: "))
print(f"Polar coordinate {Point.to_polar(Point(x, y))}")

