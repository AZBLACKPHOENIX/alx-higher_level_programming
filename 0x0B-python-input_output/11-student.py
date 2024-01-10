#!/usr/bin/python3
"""
Module for defining a Student class.
"""

class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attributes to retrieve.

        Returns:
            dict: A dictionary containing the specified attributes of the Student.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.
        """
        for key, value in json.items():
            setattr(self, key, value)
