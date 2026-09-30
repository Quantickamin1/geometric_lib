import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(area(2, 3), 6)

    def test2(self):
        self.assertEqual(area(5, 5), 25)

    def test3(self):
        self.assertEqual(area(0, 10), 0)

    def test4(self):
        self.assertAlmostEqual(area(2.5, 4), 10.0)

    def test5(self):
        self.assertEqual(perimeter(2, 3), 10)

    def test6(self):
        self.assertEqual(perimeter(5, 5), 20)

    def test7(self):
        self.assertEqual(perimeter(0, 10), 20)

    def test8(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8.0)
