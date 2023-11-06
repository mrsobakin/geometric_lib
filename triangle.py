import unittest


def area(a, h):
    '''
    Принимает основание a и высоту h треугольника, возвращает площадь треугольника
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает стороны треугольника a, b, c, возвращает периметр треугольника
    '''
    return a + b + c


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 3), 3)
        self.assertEqual(area(4, 5), 10)
        self.assertEqual(area(0, 5), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4), 9)
        self.assertEqual(perimeter(4, 5, 6), 15)
        self.assertEqual(perimeter(0, 5, 6), 11)
