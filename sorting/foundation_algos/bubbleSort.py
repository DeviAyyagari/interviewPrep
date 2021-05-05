"""
Problem Statement: Sort an integer array in ascending order
Bubble sort: This is an in-place brute force sorting algorithm. 
Intuition: Swap the consecutive elements in the array until the largest element 
            in the array is bubbled up to the last index. 
Time Complexity: Best case = Worst case = Average case = O(n^2)
Space Complexity: O(1)
Stability: stable
"""

def swap(A, index1, index2):
    """ Helper function to swap value at index1 with value at index2 for array A """
    
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp

def bubbleSort(A):
    """ Bubble sort implementation """
    for index in range(len(A)):
        for j in range(0, len(A) - index - 1):
            # swap only if one is strictly greater than the other, otherwise let them be as they are.
            # If this an >= comparison, the algorithm will lose its stability
            if A[j] > A[j+1]: 
                swap(A, j+1, j)


if __name__ == "__main__":
    test_cases = [[3, 5, 2, 7, 6], [1, 2, 1, 2], [-9, 8, 2, 0, 1.2], 
                    [8, 7, 6, 5, 4, 3, 2, 1], [1], []]
    for each in test_cases:
        bubbleSort(each)
        print(each)