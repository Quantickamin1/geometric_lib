import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(area(4), 16)

    def test2(self):
        self.assertEqual(area(1), 1)

    def test3(self):
        self.assertEqual(area(0), 0)

    def test4(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test5(self):
        self.assertEqual(perimeter(4), 16)

    def test6(self):
        self.assertEqual(perimeter(1), 4)

    def test7(self):
        self.assertEqual(perimeter(0), 0)

    def test8(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)

