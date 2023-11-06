import unittest


def area(a):
    '''
    Принимает сторону квадрата a, возвращает площадь квадрата
    '''
    return a * a


def perimeter(a):
    '''
    Принимает сторону квадрата a, возвращает периметр квадрата
    '''
    return 4 * a


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3), 9)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(0), 0)
