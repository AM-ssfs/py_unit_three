import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_rectangle(self):
        self.assertEqual(8, assignment_three.rectangle_area(4, 2))  # add assertion here
        self.assertEqual(18, assignment_three.rectangle_area(3, 6))  # add assertion here
    def test_surface_area(self):
        self.assertEqual(str(22), assignment_three.total_surface_area(1, 2, 3))  # add assertion here
        self.assertEqual(str(24), assignment_three.total_surface_area(2, 2, 2))  # add assertion here


if __name__ == '__main__':
    unittest.main()
