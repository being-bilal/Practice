# Selection Sort : It works by repeatedly selecting the smallest (or largest) element from the unsorted part and swapping it with the first unsorted element.
# Time complexity : O(n^2)

import random

original_list = list(random.randint(0, 100) for _ in range(0, 100))
print(original_list, "\n")


def find_smallest(array):
    smallest = original_list[0]
    for i in range(0, len(array)):
        if array[i] < smallest:
            smallest = array[i]

    return array.index(smallest)


def sort_array(array):
    sorted_list = list()
    for i in range(len(array)):
        smallest = find_smallest(array)
        sorted_list.append(array.pop(smallest))
    return sorted_list


print(sort_array(original_list))
