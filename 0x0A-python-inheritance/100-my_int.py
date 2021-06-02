#!/usr/bin/python3
""" Created a class called MyInt """


class MyInt(int):
    """ 
        Reverse the normal order of what comparasion
        operators do
        Use of rich comparasion methods
    """
    def __eq__(self, x: object):
        return super().__eq__(not x)

    def __ne__(self, x: object):
        return super().__ne__(not x)
