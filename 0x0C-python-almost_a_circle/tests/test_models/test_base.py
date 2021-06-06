#!/usr/bin/python3
"""Import unittest and created a class for unit test
"""
import os
import unittest
from models.base import Base
import models.base
import json


class TestBase(unittest.TestCase):
    """ Create a tests for the base class """
    def test_style_pep8_model(self):
        """ PEP8 python style """
        a = os.system("pep8 models/base.py")
        self.assertEqual(a, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        a = os.system("pep8 tests/test_models/test_base.py")
        self.assertEqual(a, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/base.py", mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.base.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(Base.__doc__) != 0)

    def test_functions_doc(self):
        """ Functions with sufficient documentation """
        self.assertTrue(len(Base.to_json_string.__doc__) != 0)
        self.assertTrue(len(Base.save_to_file.__doc__) != 0)
        self.assertTrue(len(Base.from_json_string.__doc__) != 0)
        self.assertTrue(len(Base.create.__doc__) != 0)
        self.assertTrue(len(Base.load_from_file.__doc__) != 0)


if __name__ == "__main__":
    unittest.main()
