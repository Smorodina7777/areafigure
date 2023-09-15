import unittest
import Figure


class CircleTestCase(unittest.TestCase):
    def setUp(self):
        self.circle = Figure.Circle(radius=5)


    def test_get_area(self):
        self.assertAlmostEqual(self.circle.get_area(), 78.54, places=2)


class TriangleTestCase(unittest.TestCase):
    def setUp(self):
        self.triangle = Figure.Triangle(a=3, b=4, c=5)


    def test_get_area(self):
        self.assertEqual(self.triangle.get_area(), 6)


if __name__ == '__main__':
    unittest.main()
