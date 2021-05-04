"""
Problem Statement: Sort an integer array in ascending order
Insertion sort: This is an in-place divide-and-conquer sorting algorithm. 
Intuition: Ranomly chose a an index in the array. The element at that index
            is called the pivot. Partition the array around the pivot  in such a
            way that all the elements less than the pivot are in the left
            subarray and all the elements greater than the pivot are in the
            right subarray.
Time Complexity: Best case = O(nlogn); Average case = O(nlogn); Worst case = O(n^2)
Space Complexity: O(1)
Stability: NOT stable
"""

import random

def swap(A, index1, index2):
    """ Helper function to swap value at index1 with value at index2 for array A """
    
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp

def quickSortHelper(A, start, end):
    """ Quick sort implementation(Lomuto's partitioning) """

    # Base condition of the recursion
    if start >= end:
        return
    
    #Randomly choose the pivot index
    pivotIndex = random.randint(start, end)
    pivot = A[pivotIndex]
    
    """ Partition around pivot and manipulate such a way that all the elemnts less than
    the pivot lie to the left of the pivot and all the lements greater than the
    pivot lie to the right of the pivot """

    # Swap the pivot element with the element at start
    swap(A, start, pivotIndex)

    smaller = start
    bigger = start

    """ Towards the end of this loop, all elements at index (smaller = 1) are
    greater than the pivot """

    for bigger in range(start + 1, end + 1):
        if A[bigger] < pivot:
            smaller += 1
            swap(A, smaller, bigger)

    #Swap pivot back to its "rightful" place
    swap(A, start, smaller)

    quickSortHelper(A, start, smaller - 1)
    quickSortHelper(A, smaller + 1, end)
    

def quickSort(A):
    quickSortHelper(A, 0, len(A) - 1)

if __name__ == "__main__":
    test_cases = [[3, 5, 2, 7, 6], [1, 2, 1, 2], [-9, 8, 2, 0, 1.2], 
                    [8, 7, 6, 5, 4, 3, 2, 1], [1], []]
    for each in test_cases:
        quickSort(each)
        print(each)