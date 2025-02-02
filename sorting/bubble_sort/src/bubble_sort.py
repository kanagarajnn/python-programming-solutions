"""
bubble_sort.py - Implementation of the Bubble Sort Algorithm in Python

Description:
- This module implements the Bubble Sort algorithm in Python.
- Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps
  through the list, swaps adjacent elements if they are in the wrong order,
  and moves the largest element to the end in each iteration.

Time Complexity:
- Worst Case: O(N^2) (When the array is reverse sorted)
- Average Case: O(N^2) (For a randomly shuffled array)
- Best Case: O(N) (When the array is already sorted)

Space Complexity:
- O(1) (In-place sorting algorithm)

Usage:
- Import in another script: 
    `from bubble_sort import bubble_sort`
- Run as standalone script: 
    `python bubble_sort.py`

Metadata:
- Author: Kanagaraj N N
- Date: February 1, 2025
- Version: 1.0
- License: MIT (see LICENSE file for details)
"""


from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """
    Sorts an array using the Bubble Sort algorithm.

    Args:
        array (List[int]): List of integers to be sorted.

    Returns:
        List[int]: Sorted list in ascending order.
    """
    n = len(array)
    if n <= 1:
        return array  # No sorting needed for empty or single-element lists

    is_sorted = False
    pass_counter = 0  # Tracks the number of passes

    while not is_sorted:
        is_sorted = True

        # Perform a pass through the array
        for i in range(n - 1 - pass_counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i +
                                               1], array[i]  # Swap elements
                is_sorted = False  # Mark that swapping occurred

        pass_counter += 1  # Increment counter after each pass

    return array


# Example Usage & Testing
if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [10, -1, 3, 8, 5, 2, -3, 4],
        [],
        [42]
    ]

    print("Testing Bubble Sort Algorithm:")
    for case in test_cases:
        print(f"Original: {case}")
        # Use case[:] to avoid modifying original
        print(f"Sorted  : {bubble_sort(case[:])}\n")
