import unittest

from Triangle import Triangle


class TriangleTestCase(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(a=3, b=4, c=5)


    def test_area(self):
        self.assertEqual(self.triangle.area(), 6)


if __name__ == '__main__':
    unittest.main()
