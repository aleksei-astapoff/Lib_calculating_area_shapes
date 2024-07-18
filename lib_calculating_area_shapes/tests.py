import unittest

from lib_calculating_area_shapes.shapes import (
    calculate_area,
    create_shape,
    _Circle,
    _Triangle
)


class TestShape(unittest.TestCase):
    """Тесты для расчета площади фигур"""

    def test_create_shape_circle(self):
        """Тест создания круга"""

        shape = create_shape(5)
        self.assertIsInstance(shape, _Circle)

    def test_create_shape_triangle(self):
        """Тест создания треугольника"""

        shape = create_shape(3, 4, 5)
        self.assertIsInstance(shape, _Triangle)

    def test_create_shape_invalid(self):
        """Тест создания невалидной фигуры"""

        with self.assertRaises(ValueError):
            create_shape(1, 2)
        with self.assertRaises(ValueError):
            create_shape(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            create_shape()

    def test_circle_area(self):
        """Тест вычисления площади круга"""

        circle = _Circle(5)
        self.assertEqual(circle.area(), ('Круг', 78.54))

    def test_triangle_area_right(self):
        """Тест вычисления площади прямоугольного треугольника"""

        triangle = _Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), ('Прямоугольный треугольник', 6.0))

    def test_triangle_area_non_right(self):
        """
        Тест вычисления площади непрямоугольного треугольника по трем сторонам
        """

        triangle = _Triangle(3, 4, 6)
        self.assertEqual(triangle.area(), ('Треугольник', 5.33))

    def test_calculate_area_circle(self):
        """Тест вычисления площади круга через функцию calculate_area"""

        self.assertEqual(calculate_area(5), ('Круг', 78.54))

    def test_calculate_area_triangle_right(self):
        """
        Тест вычисления площади прямоугольного треугольника
        через функцию calculate_area
        """

        self.assertEqual(
            calculate_area(3, 4, 5), ('Прямоугольный треугольник', 6.0)
            )

    def test_calculate_area_triangle_non_right(self):
        """
        Тест вычисления площади непрямоугольного треугольника
        через функцию calculate_area
        """

        self.assertEqual(calculate_area(3, 4, 6), ('Треугольник', 5.33))


if __name__ == '__main__':
    unittest.main()
