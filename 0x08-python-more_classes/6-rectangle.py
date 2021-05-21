#!/usr/bin/python3
""" Create a class called Rectangle """


class Rectangle:
    """ Constructor method to initialize the attribute of the
        instantiated object with two optionals parameters:

        Args:
            param1 (width): Is a private attribute, type int
            param2 (height): Is a private attribute, type int

        It makes use of an instance counter called number_of_instances
        that increases each time a new instance is created and decreases
        when it is being deleted.
        """
    # public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ Two class methods: area and perimeter, which return
        the indicated operation.

        They give functionality to the class attributes """
    def area(self):
        # return area of the rectangle: A = b*h (base*altura or width*height)
        return self.__width * self.__height

    def perimeter(self):
        # perimeter is the sum from all sides or 2*width + 2*height
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    """ Use of the special method __str__ that returns a string
        with what you want to show, for example, to an end user """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            print_symbol = ""
            for j in range(self.__height):
                for i in range(self.__width):
                    print_symbol += '#'
                print_symbol += '\n'
            # The function rstrip() to remove the line break from
            # a string.
            return print_symbol.rstrip()

    """ Use of the special method __repr__ that returns a string
        representation of the rectangle.

        It's purpose is to recreate a new instance using eval() """
    def __repr__(self):
        # self.__class__.__name__ : automatically adds the name of the class
        # to the string created.
        return "{self.__class__.__name__}\
({self.width}, {self.height})".format(self=self)

    """ The special method __del__ is used to destroy an instance and a
        message is printed when the instance has been deleted. """
    def __del__(self):
        type(self).number_of_instances -= 1
        return print("Bye rectangle...")
