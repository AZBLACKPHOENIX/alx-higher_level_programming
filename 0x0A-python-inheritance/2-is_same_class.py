#!/usr/bin/python3
"""define function"""
def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class; otherwise, returns False."""
    return type(obj) is a_class
