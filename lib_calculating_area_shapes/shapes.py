import math


class _Shape:
    """Базовый класс фигуры"""
    def __init__(self, *args) -> None:
        self.text = 'Фигура'

    def area(self):
        raise NotImplementedError('Подклассы должны реализовывать этот метод')


class _Circle(_Shape):
    """Круг"""

    def __init__(self, radius):
        self.text = 'Круг'
        self.radius = radius

    def area(self):
        square = math.pi * (self.radius**2)
        return self.text, round(square, 2)


class _Triangle(_Shape):
    """Треугольник"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    def area(self):
        if self.is_right_angle():
            self.text = 'Прямоугольный треугольник'
            sides = sorted([self.a, self.b, self.c])
            square = 0.5 * sides[0] * sides[1]
        else:
            self.text = 'Треугольник'
            p = (self.a + self.b + self.c) / 2
            square = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

        return self.text, round(square, 2)


def create_shape(*args):
    """Создание фигуры"""

    if len(args) == 1:
        return _Circle(args[0])
    elif len(args) == 3:
        return _Triangle(args[0], args[1], args[2])
    else:
        raise ValueError(
            'Недопустимое количество аргументов для создания фигуры'
            )


def calculate_area(*args):
    """Создание фигуры и вычисление ее площади"""

    return create_shape(*args).area()


if __name__ == "__main__":
    print(calculate_area(5))           # Circle
    print(calculate_area(3, 4, 5))     # Right-angled Triangle
    print(calculate_area(3, 4, 6))     # Non-right-angled Triangle
