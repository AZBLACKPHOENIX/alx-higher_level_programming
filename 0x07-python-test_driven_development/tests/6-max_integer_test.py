#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test max_integer with an unordered list"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        result = max_integer([-1, -5, -3])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative numbers"""
        result = max_integer([-1, 5, -3, 10, 8])
        self.assertEqual(result, 10)

    def test_single_element_list(self):
        """Test max_integer with a list containing a single element"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_duplicate_max_value(self):
        """Test max_integer with a list containing duplicate max values"""
        result = max_integer([2, 2, 2, 2, 2])
        self.assertEqual(result, 2)

    def test_strings_in_list(self):
        """Test max_integer with a list containing strings"""
        result = max_integer(["hello", "world", "python"])
        self.assertEqual(result, "world")

    def test_mixed_data_types(self):
        """Test max_integer with a list containing mixed data types"""
        result = max_integer([1, "two", 3.5, 4])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()

