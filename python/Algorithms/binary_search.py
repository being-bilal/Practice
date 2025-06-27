# Binary Search : is a search algorithm to find an element in a sorted list or array by repeatedly dividing the search interval in half.
# Time Complexity : O(log n)
# Requirement : Sorted Array

import random

list1 = list(i for i in range(1,101)) # sorted array of numbers
num = random.randint(1,100) # number that we have to search 
high = len(list1) - 1
low = 0

print(f"Number to find : {num}")

for i in range(len(list1)):
    mid = ((low + high)//2)
    if (num > list1[mid]): 
        low = mid + 1
    elif (num < list1[mid]):
        high = mid
    if num == list1[mid]:
        print(f"{list1[mid]} found at index : {mid}")
        break
    
