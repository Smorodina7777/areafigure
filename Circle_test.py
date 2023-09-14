import unittest
from Circle import Circle


class CircleTestCase(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(radius=5)


    def test_area(self):
        self.assertAlmostEqual(self.circle.area(), 78.54, places=2)


if __name__ == '__main__':
    unittest.main()
