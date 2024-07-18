import unittest
from task1.shapes import Circle, Triangle, ShapeCalculator
import math


class TestShapeLibrary(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        s = (3 + 4 + 5) / 2
        expected_area = math.sqrt(s * (s - 3) * (s - 4) * (s - 5))
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_non_right_triangle(self):
        triangle = Triangle(2, 3, 4)
        self.assertFalse(triangle.is_right())

    def test_shape_calculator_with_circle(self):
        circle = Circle(5)
        expected_area = math.pi * 25
        self.assertAlmostEqual(ShapeCalculator.calculate_area(circle), expected_area, places=5)

    def test_shape_calculator_with_triangle(self):
        triangle = Triangle(3, 4, 5)
        s = (3 + 4 + 5) / 2
        expected_area = math.sqrt(s * (s - 3) * (s - 4) * (s - 5))
        self.assertAlmostEqual(ShapeCalculator.calculate_area(triangle), expected_area, places=5)

    def test_shape_calculator_with_invalid_shape(self):
        with self.assertRaises(TypeError):
            ShapeCalculator.calculate_area("invalid shape")


if __name__ == '__main__':
    unittest.main()
