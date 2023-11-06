import unittest
import math


def area(r):
    '''
    Принимает радиус круга r, возвращает площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус окружности r, возвращает длину (периметр) окружности
    '''
    return 2 * math.pi * r


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi, places=2)
        self.assertAlmostEqual(area(2), 4 * math.pi, places=2)
        self.assertAlmostEqual(area(0), 0, places=2)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=2)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi, places=2)
        self.assertAlmostEqual(perimeter(0), 0, places=2)
