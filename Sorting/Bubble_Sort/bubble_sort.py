# Language: Python
# Solution 1: Bubble Sort Algorithm
# Time: Worst - O(N^2), Avg - O(N^2), Best - O(N)
# Space: O(1)

def bubbleSort(array):
    is_sorted = False
    counter = 0

    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
        counter += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
