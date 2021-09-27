import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_add_two(self):

        self.assertEqual(1, return_addtion.add_two(-7, 8))
        self.assertEqual(-14, return_addtion.add_two(-11, -3))


    def test_triangle_area(self):
        pass
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))


if __name__ == '__main__':
    unittest.main()
