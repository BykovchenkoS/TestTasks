import math


class Shape:
    def area(self):
        raise NotImplementedError("Подклассы должны реализовать этот метод")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2)


class ShapeCalculator:
    @staticmethod
    def calculate_area(shape):
        if isinstance(shape, Shape):
            return shape.area()
        else:
            raise TypeError("Такой фигуры я не знаю(((")
