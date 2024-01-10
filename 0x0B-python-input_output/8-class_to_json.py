#!/usr/bin/python3
"""
Module for converting a class instance to a JSON-serializable dictionary.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary with serializable attributes of the object.
    """
    return obj.__dict__

if __name__ == "__main__":
    class_to_json()
