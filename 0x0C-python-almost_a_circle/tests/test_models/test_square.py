#!/usr/bin/python3
"""Import unittest and created a class for unit test
"""
import os
import unittest
from models.square import Square
import models.square
import json


class TestSquare(unittest.TestCase):
    """ Create a tests for the square class """
    def test_style_pep8_model(self):
        """ PEP8 python style """
        a = os.system("pep8 models/square.py")
        self.assertEqual(a, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        a = os.system("pep8 tests/test_models/test_square.py")
        self.assertEqual(a, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/square.py", mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.square.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(Square.__doc__) != 0)

    def test_functions_doc(self):
        """ Functions with sufficient documentation """
        self.assertTrue(len(Square.__str__.__doc__) != 0)
        self.assertTrue(len(Square.update.__doc__) != 0)
        self.assertTrue(len(Square.to_dictionary.__doc__) != 0)


if __name__ == "__main__":
    unittest.main()
