import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def to_polar(self):
        return [math.atan2(y, x), math.sqrt(x ** 2 + y ** 2)]


x = int(input("Print first dekart coordinate: "))
y = int(input("Print second dekart coordinate: "))
point = Point(x, y)
print(f"Polar coordinate {point.to_polar()}")

