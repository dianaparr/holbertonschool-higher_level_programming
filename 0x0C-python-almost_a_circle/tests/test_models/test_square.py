#!/usr/bin/python3
"""Import unittest and created a class for unit test
"""
import os
import unittest
from models.square import Square
import models.square
# import json


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

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_square.py", mode='r') as f:
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


class TestSquareCases(unittest.TestCase):
    """ Create a tests for the square class in edge cases """
    def test_all_attributes_square(self):
        """ All attributes class Square """
        inst = Square(6, 12, 6)
        self.assertEqual(inst.size, 6)
        self.assertEqual(inst.x, 12)
        self.assertEqual(inst.y, 6)

    def test_str_square(self):
        """ Output representation informal form """
        inst = Square(5, 8, 1, 1)
        self.assertEqual(inst.__str__(), "[Square] (1) 8/1 - 5")

    def test_size(self):
        """ Check of type width """
        with self.assertRaises(TypeError):
            Square("4")

    def test_update_args(self):
        """ Update value of the attributes """
        inst = Square(6, 6, 6, 6)
        inst.update(4)
        self.assertEqual(inst.id, 4)
        inst.update(4, 9)
        self.assertEqual(inst.size, 9)
        inst.update(4, 9, 1)
        self.assertEqual(inst.x, 1)
        inst.update(4, 9, 1, 3)
        self.assertEqual(inst.y, 3)

    def test_update_kwargs_square(self):
        """ Update value with the key of the attributes """
        inst = Square(6, 6, 6, 6)
        inst.update(y=5)
        self.assertEqual(inst.y, 5)
        inst.update(size=9, x=1, y=2, id=34)
        self.assertEqual(inst.size, 9)
        self.assertEqual(inst.x, 1)
        self.assertEqual(inst.y, 2)
        self.assertEqual(inst.id, 34)

if __name__ == "__main__":
    unittest.main()
