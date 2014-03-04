
#!/usr/bin/env python
import unittest
from find_closest_points import find_closest_points


class FindClosestPointsTest(unittest.TestCase):

    def test1(self):
        points = [(1, 1), (1, 2), (1, 3)]
        closest_points = [(1, 1), (1, 2)]
        self.assertEqual(closest_points, find_closest_points(2, points))

    def test2(self):
        points = [(2, 6), (18, 14), (4, 18), (17, 3), (4, 2), (9, 10),
                  (16, 10), (4, 18), (15, 11), (9, 8), (9, 14), (18, 4),
                  (4, 16), (1, 13), (10, 14), (14, 12), (15, 4), (4, 6),
                  (7, 16), (0, 19)]
        closest_points = [(2, 6), (4, 6), (9, 8), (1, 13), (4, 2)]
        self.assertEqual(closest_points, find_closest_points(5, points))


if __name__ == '__main__':
    unittest.main()