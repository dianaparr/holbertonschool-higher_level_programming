#!/usr/bin/python3
"""Import unittest and created a class for unit test
"""
import os
import unittest
from models.rectangle import Rectangle
import models.rectangle
import json


class TestRectangle(unittest.TestCase):
    """ Create a tests for the Rectangle class """
    def test_style_pep8_model(self):
        """ PEP8 python style """
        a = os.system("pep8 models/rectangle.py")
        self.assertEqual(a, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        a = os.system("pep8 tests/test_models/test_rectangle.py")
        self.assertEqual(a, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/rectangle.py", mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.rectangle.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(Rectangle.__doc__) != 0)

    def test_functions_doc(self):
        """ Functions with sufficient documentation """
        self.assertTrue(len(Rectangle.area.__doc__) != 0)
        self.assertTrue(len(Rectangle.display.__doc__) != 0)
        self.assertTrue(len(Rectangle.__str__.__doc__) != 0)
        self.assertTrue(len(Rectangle.update.__doc__) != 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) != 0)

if __name__ == "__main__":
    unittest.main()
