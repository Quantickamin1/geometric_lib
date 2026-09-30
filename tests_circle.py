import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test1(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test2(self):
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test3(self):
        self.assertEqual(area(0), 0)

    def test4(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)

    def test5(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test6(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def test7(self):
        self.assertEqual(perimeter(0), 0)

    def test8(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)