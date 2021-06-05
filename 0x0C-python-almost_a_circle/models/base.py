#!/usr/bin/python3
"""
Created a class called Base
"""

import json


class Base:
    """ This class will be the "base" of all other
        classes in this project.

        Purpose: manage id attribute in all classes
                 and to avoid duplicating the same code.

        Created of private class attribute called __nb_objects = 0
        which will be a 'counter' that will provide the id in case
        it is found.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method to initialize the attribute of the
        instantiated object with one parameter:

        Parameter:

            id (integer): Is a public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method using the json.dumps() method
        that allows you to serialize Python objects as a str

        Parameter:
                list_dictionaries: list of dictionaries

        Returns:
                JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        else:
            list_dict = json.dumps(list_dictionaries)
            return list_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes the JSON string representation
        of list_objs to a file.

        Parameters:
                list_objs: list of instances who inherits of Base
        """
        create_list = []
        if not list_objs:
            with open("{}.json".format(cls.__name__), mode='w') as f:
                json.dump(list_objs, f)
        else:
            for a in list_objs:
                # to_instan = cls(a.width, a.height, a.x, a.y, a.id)
                create_list.append(vars(a))
            Base.to_json_string(create_list)
        with open("{}.json".format(cls.__name__), mode='w') as f:
            json.dump(create_list, f)

    @staticmethod
    def from_json_string(json_string):
        """ Static method using the json.load() method
        that allows you to deserialize Python objects as a str

        Parameter:
                json_string: string representing a list of dictionaries

        Returns: the list of the JSON string representation
        """
        if not json_string:
            return []
        else:
            repre_json = json.loads(json_string)
            return repre_json
