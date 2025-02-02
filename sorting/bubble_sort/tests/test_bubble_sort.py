"""
test_bubble_sort.py - Unit Tests for the Bubble Sort Algorithm

Description:
- This file contains unit tests for the `bubble_sort` function using the `unittest` framework.
- The tests cover various edge cases, including already sorted arrays, reverse-sorted arrays,
  negative numbers, single-element arrays, empty arrays, and arrays with duplicates.

Usage:
- Run all tests using Python's unittest framework:
    `python -m unittest test_bubble_sort.py`
- Run all tests in verbose mode (for detailed output):
    `python -m unittest -v test_bubble_sort.py`
- Discover and run all tests in the directory:
    `python -m unittest discover -s tests`
- Run a specific test case:
    `python -m unittest test_bubble_sort.TestBubbleSort.test_duplicates`
   
Metadata:
- Author: Kanagaraj N N
- Date: February 1, 2025
- Version: 1.0
- License: MIT (see LICENSE file for details)
"""

import unittest
from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Test case for the Bubble Sort function."""

    def test_already_sorted(self):
        """Test an already sorted array."""
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Test a reverse sorted array."""
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted(self):
        """Test an unsorted random array."""
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [
                         11, 12, 22, 25, 34, 64, 90])

    def test_negative_numbers(self):
        """Test an array with negative numbers."""
        self.assertEqual(bubble_sort(
            [10, -1, 3, 8, 5, 2, -3, 4]), [-3, -1, 2, 3, 4, 5, 8, 10])

    def test_single_element(self):
        """Test an array with a single element."""
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty_array(self):
        """Test an empty array."""
        self.assertEqual(bubble_sort([]), [])

    def test_duplicates(self):
        """Test an array with duplicate values."""
        self.assertEqual(bubble_sort([4, 2, 2, 8, 3, 3, 1]), [
                         1, 2, 2, 3, 3, 4, 8])


if __name__ == "__main__":
    unittest.main()
