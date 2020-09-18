"""
Quick Sort is one of the most efficient sorting algorithms.
It is based on the splitting of the input list into smaller lists.
Quick Sort works better with smaller data sets in comparison to merge sort.
"""

import random

rand_list = [random.randint(1, 100) for i in range(0,8)]

def swap(arr: list, i: int, k: int) -> None:
    """

    :param arr: input array
    :type arr: list
    :param i: first element to swap in list
    :type i: int
    :param k: second element to swap in list
    :type k: int
    :return: None
    """
    arr[i], arr[k] = arr[k], arr[i]

