import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(area(4, 2), 4)

    def test2(self):
        self.assertEqual(area(3, 4), 6)

    def test3(self):
        self.assertEqual(area(10, 0), 0)

    def test4(self):
        self.assertAlmostEqual(area(2.5, 3.0), 3.75)

    def test5(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test6(self):
        self.assertEqual(perimeter(6, 6, 6), 18)

    def test7(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.0), 7.0)

