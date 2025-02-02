**Bubble Sort Algorithm in Python**
==================================

**Description:**
  - This repository contains an implementation of the Bubble Sort Algorithm in Python, along with comprehensive unit tests using the unittest framework.
  - Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, swaps adjacent elements if they are in the wrong order, and moves the largest element to the end in each iteration.

**Features:**
  - Pure Python Implementation
        – Uses built-in Python constructs.
  - Well-structured Code
        – Follows industry best practices with docstrings and type hints.
  - Unit Tests Included
        – Covers all edge cases such as sorted arrays, reverse-sorted arrays, empty lists, negative numbers, and duplicate values.
  - CI/CD Integrated
        - Runs tests automatically using GitHub Actions on every commit.

**Time Complexity:**
  - Worst Case (Reverse sorted array):	O(N²)
  - Average Case (Random order):	O(N²)
  - Best Case (Already sorted array):	O(N)

**Space Complexity:** 
  - O(1) (In-place sorting)

**Installation & Usage:**
  - Clone the repository
      - $ git clone https://github.com/kanagarajnn/python-programming-solutions.git
      - $ cd python-programming-solutions
  - Run Bubble Sort as a standalone script
      - $ python sorting/bubble_sort/src/bubble_sort.py
  - Import and use in another script
      - $ from sorting.bubble_sort.src.bubble_sort import bubble_sort
      - $ array = [64, 34, 25, 12, 22, 11, 90]
      - $ sorted_array = bubble_sort(array)
      - $ print(sorted_array)  # Output: [11, 12, 22, 25, 34, 64, 90]

**Running Unit Tests:**
  - Unit tests are included to validate the correctness of the implementation.
  - Run all tests
      - $ python -m unittest discover -s sorting/bubble_sort/tests -v
  - Run a specific test case
      - $ python -m unittest sorting.bubble_sort.tests.test_bubble_sort.TestBubbleSort.test_unsorted

**Continuous Integration (CI) with GitHub Actions**
  - This project is configured with GitHub Actions for automated testing.

  - CI/CD Workflow Details
      - Runs tests automatically on every push and pull request to the main branch.
      - Uses Python 3.10 on an Ubuntu runner.
      - Ensures code correctness before merging.

  - How to Check CI/CD Status
      - Push your changes:
        $ git push origin main
      - Navigate to your GitHub repository → Actions tab.
      - Check the workflow Python CI to view test results.

**License**
  - This project is licensed under the MIT License. See the LICENSE file for details.


**Author:** Kanagaraj N N
**Email:** n.n.kanagaraj.upm@gmail.com
**GitHub:** https://github.com/kanagarajnn

Contributions Welcome!
Want to improve this project? Feel free to submit pull requests or report issues.

Happy Programming!

