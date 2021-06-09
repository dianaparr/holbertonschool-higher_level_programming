#!/usr/bin/python3
"""Import unittest and created a class for unit test
"""
from models.base import Base
import os
import io
import sys
import unittest
from models.rectangle import Rectangle
import models.rectangle
# import json


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

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_rectangle.py", mode='r') as f:
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


class TestRectangleCases(unittest.TestCase):
    """ Create a tests for the rectangle class in edge cases """
    def test_all_attributes(self):
        """ All attributes class Rectangle """
        inst = Rectangle(6, 8, 12, 6)
        self.assertEqual(inst.width, 6)
        self.assertEqual(inst.height, 8)
        self.assertEqual(inst.x, 12)
        self.assertEqual(inst.y, 6)

    def test_raise_must_be_integer(self):
        """ Expects it to be of type integer """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("l", 6)
        with self.assertRaises(TypeError):
            Rectangle(4, 6, "x")
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 1, "y")

    def test_raise_equal_zero(self):
        """ Expects it not to be under or equals 0, height
        and width """
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_raise_equal_zero_x_y(self):
        """ Expects it not to be under or equals 0, x
        and y """
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -9, 0)

    def test_area(self):
        """ Area check correct """
        inst = Rectangle(4, 5)
        self.assertEqual(inst.area(), 20)

    def test_display_zero(self):
        """ Check print in stdout the character '#' """
        display_output = Rectangle(5, 5)
        display_str = "#####\n#####\n#####\n#####\n#####\n"
        output = io.StringIO()
        sys.stdout = output
        display_output.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), display_str)
        output.flush()

    def test_str_rectangle(self):
        """ Output representation informal form """
        inst = Rectangle(5, 8, 1, 12, 5)
        self.assertEqual(inst.__str__(), "[Rectangle] (5) 1/12 - 5/8")

    def test_display_one(self):
        """ Check print in stdout the character '#' x and y """
        display_output = Rectangle(5, 5, 1, 0)
        display_str = " #####\n #####\n #####\n #####\n #####\n"
        output = io.StringIO()
        sys.stdout = output
        display_output.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), display_str)
        output.flush()

    def test_update_args(self):
        """ Update value of the attributes """
        inst = Rectangle(6, 6, 6, 6)
        inst.update(4)
        self.assertEqual(inst.id, 4)
        inst.update(4, 9)
        self.assertEqual(inst.width, 9)
        inst.update(4, 9, 1)
        self.assertEqual(inst.height, 1)
        inst.update(4, 9, 1, 3)
        self.assertEqual(inst.x, 3)
        inst.update(4, 9, 1, 3, 11)
        self.assertEqual(inst.y, 11)

    def test_update_kwargs(self):
        """ Update value with the key of the attributes """
        inst = Rectangle(6, 6, 6, 6)
        inst.update(y=5)
        self.assertEqual(inst.y, 5)
        inst.update(height=9, x=1, y=2, id=34)
        self.assertEqual(inst.width, 6)
        self.assertEqual(inst.height, 9)
        self.assertEqual(inst.x, 1)
        self.assertEqual(inst.y, 2)
        self.assertEqual(inst.id, 34)

    def test_to_dictionary_rectangle(self):
        """ Check returns the dictionary representation """
        inst = Rectangle(5, 8)
        self.assertEqual(inst.to_dictionary(), {'x': 0, 'y': 0, 'id': 14,
                                                'height': 8, 'width': 5})
        inst_two = Rectangle(5, 8, 9)
        self.assertEqual(inst_two.to_dictionary(), {'x': 9, 'y': 0, 'id': 15,
                                                    'height': 8, 'width': 5})
        inst_three = Rectangle(5, 8, 9, 4)
        self.assertEqual(inst_three.to_dictionary(), {'x': 9, 'y': 4, 'id': 16,
                                                      'height': 8, 'width': 5})

if __name__ == "__main__":
    unittest.main()
