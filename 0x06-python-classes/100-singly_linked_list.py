#!/usr/bin/python3
"""define a node class"""
class Node:
    """Define a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a node with data and next_node."""
        self.data = data
        self.next_node = next_node
    """property"""
    @property
    def data(self):
        """Retrieve the value of data."""
        return self.__data
    """data setter"""
    @data.setter
    def data(self, value):
        """Set the value of data with validation."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    """property"""
    @property
    def next_node(self):
        """Retrieve the value of next_node."""
        return self.__next_node
    """setter"""
    @next_node.setter
    def next_node(self, value):
        """Set the value of next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
"""define singly linked class"""
class SinglyLinkedList:
    """Define a singly linked list."""
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
