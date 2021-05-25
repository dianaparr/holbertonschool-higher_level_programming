import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # self.assertRaises(max_integer((1, 2, 4), 4))
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-87, -900, -357]), -87)
        self.assertEqual(max_integer([87.456, 87.455, 86]), 87.456)

if __name__ == '__main__':
    unittest.main()
