import unittest


def area(a, b):
    '''
    Принимает стороны прямоугльника a и b, возвращает площадь прямоугольника
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает стороны прямоугльника a и b, возвращает периметр прямоугольника
    '''
    return 2 * (a + b)


class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(4, 5), 20)
        self.assertEqual(area(0, 5), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(4, 5), 18)
        self.assertEqual(perimeter(0, 5), 10)
