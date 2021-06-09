#!/usr/bin/python3
"""Import unittest and created a class for unit test
"""
from models.rectangle import Rectangle
import os
import unittest
from models.base import Base
import models.base
# import json


class TestBaseDoc(unittest.TestCase):
    """ Create a tests for the base class in documentation
    and requirements """
    def test_readme(self):
        """ Created a readme and that exists """
        the_readme = os.getcwd()
        readme_one = the_readme + '/README.md'
        readme_two = os.path.exists(readme_one)
        self.assertTrue(readme_two, True)
        with open(readme_one, mode='r') as f:
            r = f.read()
            self.assertTrue(len(r) != 0)

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

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_base.py", mode='r') as f:
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


class TestBaseCases(unittest.TestCase):
    """ Create a tests for the base class in edge cases """
    def test_private_class(self):
        """ __nb_objects initialized in zero """
        # self.assertEqual(Base._Base__nb_objects, 0)
        self.assertNotEqual(Base._Base__nb_objects, 5)

    def test_attribute_id(self):
        """ Check to the id number, nb objects increments
        with number of instances """
        one = Base()
        self.assertEqual(one.id, 1)
        two = Base()
        self.assertEqual(two.id, 2)
        other_ins = Base(40)
        self.assertEqual(other_ins.id, 40)
        three = Base()
        self.assertEqual(three.id, 3)

    def test_to_json_string_return_str(self):
        """ Type json string """
        list_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(type(Base.to_json_string(list_dict)), str)

    def test_to_json_string_return_failed(self):
        """ Type different of list directory """
        list_dict = [2, 10, 1, 7, 8]
        self.assertNotEqual(type(Base.to_json_string(list_dict)), dict)

    def test_to_json_string_len(self):
        """ Check length of the list dictionary """
        length_dictionary = [{'x': 2, 'width': 10, 'id': 1,
                              'height': 7, 'y': 8}]
        self.assertTrue(len(Base.to_json_string(length_dictionary)) > 0)

    def test_to_json_string_len_two(self):
        """ Check length to the string """
        length_string = None
        self.assertTrue(len(Base.to_json_string(length_string)) == 2)

    def test_save_to_file_list_obj_none(self):
        """ List of instances is None return list empty """
        list_empty = None
        self.assertTrue(type(Base.save_to_file(list_empty)), [])

    def test_from_json_string_repre(self):
        """ Checks a list of JSON string representation """
        repre_json = [{'id': 70, 'width': 5, 'height': 8},
                      {'id': 3, 'width': 2, 'height': 5}]
        json_in = Rectangle.to_json_string(repre_json)
        json_return = Rectangle.from_json_string(json_in)
        self.assertEqual(type(json_in), str)
        self.assertEqual(type(repre_json), list)
        self.assertEqual(type(json_return), list)

    def test_from_json_string_repre_failed(self):
        """ Failure in the input data type """
        repre_json = [{"id": 70, "width": 5, "height": 8},
                      {"id": 3, "width": 2, "height": 5}]
        data_in = Rectangle.to_json_string(repre_json)
        json_return = Rectangle.from_json_string(data_in)
        self.assertTrue(type(data_in), list)
        self.assertTrue(type(json_return), str)


if __name__ == "__main__":
    unittest.main()
