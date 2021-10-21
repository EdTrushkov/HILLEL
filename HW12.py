

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def minus(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def plus(self, vector):
        self.x += vector.x
        self.y += vector.y

    def multiplication(self, b):
        self.x *= b
        self.y *= b

