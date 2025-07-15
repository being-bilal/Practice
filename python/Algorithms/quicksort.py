# QuickSort : it is a divide and conquer sorting algortihm in which a random number (usually the first element of the array is selected) is selected called pivot
# all the numbers greater than the pivot are put in another array which is sorted using the same algorithm again using recursion 
# and all the numbers smaller than the pivot are put in another array which is sorted the same way 
# at the end the result becomes : Less_array + pivot + large_array 

def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    smaller = [x for x in array[1:] if x <= pivot]
    larger = [x for x in array if x > pivot]
    
    return quicksort(smaller) + [pivot] + quicksort(larger)


print(quicksort([7, 3, 7, 8, 3, 2, 1]))
