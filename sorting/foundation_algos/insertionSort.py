"""
Problem Statement: Sort an integer array in ascending order
Insertion sort: This is an in-place decrease-and-conquer sorting algorithm. 
Intuition: Imagine you already have an array sorted till index k. We then try
            to insert the element at k+1 into this already sorted array.
Time Complexity: Best case = Worst case = Average case = O(n^2)
Space Complexity: O(1)
Stability: stable
"""

def swap(A, index1, index2):
    """ Helper function to swap value at index1 with value at index2 for array A """
    
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp

def insertionSort(A, length):
    """ Insertion sort implementation """
    if length <= 0:
        return
    insertionSort(A, length - 1)
    j = length - 1
    # swap only if one is strictly greater than the other, otherwise let them be as they are.
    # If this an >= comparison, the algorithm will lose its stability
    while j>=0 and A[j] > A[j + 1]:
        swap(A, j + 1, j)
        j = j - 1
    return


if __name__ == "__main__":
    test_cases = [[3, 5, 2, 7, 6], [1, 2, 1, 2], [-9, 8, 2, 0, 1.2], 
                    [8, 7, 6, 5, 4, 3, 2, 1], [1], []]
    for each in test_cases:
        insertionSort(each, len(each) - 1)
        print(each)