"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
    """

Function that find minimal element in array

:param arr: Array containing numbers
:return: index of first occurrence of minimal element in array
"""

    min_ind = 0

    for i in range(1, int(len(arr))):
        if arr[i] < arr[min_ind]:
            min_ind = i

    return min_ind
