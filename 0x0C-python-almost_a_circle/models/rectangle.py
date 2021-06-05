#!/usr/bin/python3
"""
Created a class called Rectangle inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """ Constructor method to initialize the attribute of the
        instantiated object with four optionals parameters
        and call to the super class Base with id:

        Args:
            width: Is a private attribute
            height: Is a private attribute
            x: Is a private attribute
            y: Is a private attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        # call the super class with id
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
    Private instance attributes, each with its own public
    getter and setter
    """
    @property
    def width(self):
        return self.__width

    """
    Update attribute width
    raising exception:
        - TypeError if the input is not an integer
        - ValueError if width is under or equals 0
    """
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    """
    Update attribute height
    raising exception:
        - TypeError if the input is not an integer
        - ValueError if height is under or equals 0
    """
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    """
    Update attribute x
    raising exception:
        - TypeError if the input is not an integer
        - ValueError if x is under 0
    """
    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    """
    Update attribute y
    raising exception:
        - TypeError if the input is not an integer
        - ValueError if y is under 0
    """
    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ Public method 'area'
            Return:
                    the area value of the Rectangle instance """
        return self.__height * self.__width

    def display(self):
        """ Public method 'display'
            Prints in stdout the character '#'
            by taking care of x and y """
        for s in range(self.__y):
            print("")
        for i in range(self.__height):
            print(self.__x * " ", end="")
            print('#' * self.__width)

    def __str__(self):
        """ Overrinding the special method __str__ """
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """ Public method 'update'
        that assigns a key/value argument to attributes """ 
        if args:
            # create a list which the "keys" or attributes in order
            list_of_key = ["id", "width", "height", "x", "y"]
            for a in range(len(args)):
                setattr(self, list_of_key[a], args[a])
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)
