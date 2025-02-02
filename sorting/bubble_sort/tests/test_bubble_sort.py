import unittest
from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [
                         11, 12, 22, 25, 34, 64, 90])

    def test_single_element_array(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_duplicate_values(self):
        self.assertEqual(bubble_sort([4, 2, 2, 8, 3, 3, 1]), [
                         1, 2, 2, 3, 3, 4, 8])


if __name__ == "__main__":
    unittest.main()
