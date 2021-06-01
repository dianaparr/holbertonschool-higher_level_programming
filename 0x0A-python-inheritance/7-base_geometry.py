#!/usr/bin/python3
""" Created a Class BaseGeometry """


class BaseGeometry:
    """ Public instance method that raise an exception
        (for the moment)
    """
    def area(self):
        raise Exception("area() is not implemented")

    """ Public instance method that validates value """
    def integer_validator(self, name, value):
        """ 
        Function that validates if value is a integer 
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
