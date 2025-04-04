"""

Bubble sort

Bubble sort is a simple sorting algorithm that works by repeatedly stepping through the list,
comparing adjacent elements and swapping them if they are in the wrong order, moving the largest
elements to the end with each pass

1. Looping through list
2. Compares elements of list (list[n] > list[n+1]), swaps them if they are in the wrong order.
3. The pass through the list is repeated until the list is sorted.

"""
import random
import copy

randomlist = [random.randint(0,100) for i in range(0, 7)]


def bubble_sort(some_list: list):

    list_to_sort = copy.deepcopy(some_list)

    for i in range(len(list_to_sort)):
        for k in range(len(list_to_sort)-1):
            if list_to_sort[k] > list_to_sort[k+1]:
                list_to_sort[k], list_to_sort[k + 1] = list_to_sort[k + 1], list_to_sort[k]

    return list_to_sort

print(f"\n --- Sorting list {randomlist} by bubble algorithm --- \n")
print("\n --- After sorting", bubble_sort(randomlist))


