#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test max_integer with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_list(self):
        """Test max_integer with a reversed list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unsorted_list(self):
        """Test max_integer with an unsorted list"""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test max_integer with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test max_integer with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list containing mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_float_numbers(self):
        """Test max_integer with a list containing float numbers"""
        self.assertEqual(max_integer([1.5, 2.3, 3.7, 4.2]), 4.2)

if __name__ == '__main__':
    unittest.main()
