"""
Problem Statement: Sort an integer array in ascending order
Selection sort: This is an in-place brute force sorting algorithm. 
Intuition: For every index in an array, select the element of the array
            that belongs at that index.
Time Complexity: Best case = Worst case = Average case = O(n^2)
Space Complexity: O(1)
Stability: NOT stable
            Selection sort works by finding the minimum element and then 
            inserting it in its correct position by swapping with the element 
            which is in the position of this minimum element. 
            This makes it unstable.
"""

def swap(A, index1, index2):
    """ Helper function to swap value at index1 with value at index2 for array A """
    
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp

def selectionSort(A):
    """ Selection sort implementation """
    for index in range(len(A)):
        min_index = index
        for j in range(index+1, len(A)):
            if A[j] < A[index]:
                min_index = j

        swap(A, index, min_index)


if __name__ == "__main__":
    test_cases = [[3, 5, 2, 7, 6], [1, 2, 1, 2], [-9, 8, 2, 0, 1.2], 
                    [8, 7, 6, 5, 4, 3, 2, 1], [1], []]
    for each in test_cases:
        selectionSort(each)
        print(each)