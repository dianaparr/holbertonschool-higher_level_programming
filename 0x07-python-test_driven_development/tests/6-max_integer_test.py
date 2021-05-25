#!/usr/bin/python3
"""
Import unittest and created a class for unit test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class called TestMaxInteger. This would be a subclass of
        the TestCase class of the unittest module. 
    """
    def test_max_integer(self):
        """ Method representing tests. In this case, which return
            the max integer in a list of integers.
        
        Methods of the class TestCase:
            assertEqual: make sure they are equal
            assertNotEqual: make sure they are not the same
            assertRaises: verifies the production of exceptions
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertNotEqual(max_integer([-87, -900, -357]), -900)
        self.assertEqual(max_integer([87.456, 87.455, 86]), 87.456)
        self.assertEqual(max_integer([87.456, 87.456, 87.456]), 87.456)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([8]), 8)
        self.assertEqual(max_integer((6, 7, 8)), 8)
        with self.assertRaises(TypeError):
            max_integer([86, 87.455, "h"])
        with self.assertRaises(TypeError):
            max_integer([6, [-7, 9, 10.89], 8, (60, 90)])

""" Final block to run the tests.
        unittest.main(): provides the command line interface
                         for the test script.
"""
if __name__ == '__main__':
    unittest.main()
