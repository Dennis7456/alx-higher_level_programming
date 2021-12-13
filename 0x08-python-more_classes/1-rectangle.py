#!/usr/bin/python3
"""
A rectangle.
"""


class Rectangle:
    """
    Rectangle functions and data
    """
    def __init__(self, width=0, height=0):
        """
        Instatiation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) != int:
            raise ValueError("Width must be an integer")
        if (value < 0):
            raise ValueError("Integer cannot be less than zero")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) != int:
            raise ValueError("Height must be an integer")
        if (value < 0):
            raise ValueError("Integer cannot be less than zero")
        self.__height = value
        
