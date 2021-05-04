"""
Problem Statement: Sort an integer array in ascending order
Insertion sort: This is an out-of-place divide-and-conquer sorting algorithm. 
Intuition: Divide an array into two equal partitions. Sort each partition.  
            Merge the two partitions
Time Complexity: Best case = Worst case = Average case = O(nlogn)
Space Complexity: O(n)
Stability: stable
"""

def merge(A, start, mid, end):
    """ Merge contents of two slices. Start, mid and end indices are used to find slices """

    # Initialize two variables i and j which are used pointers when 
    # iterating through the two slices.
    i = start
    j = mid + 1
    # Initialize an empty list output that will be populated with sorted elements.
    aux_array = []
    
    # Executes the while loop if both pointers i and j are less than the 
    # length of the left and right slices
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            aux_array.append(A[i])
            i += 1
        else:
            aux_array.append(A[j])
            j += 1
    
    # The remnant elements are picked from the current pointer value to the 
    # end of the respective slice
    while i <= mid:
        aux_array.append(A[i])
        i += 1

    while j <= end:
        aux_array.append(A[j])
        j += 1
    
    # Copy sorted list into A
    for i in range(len(aux_array)):
        A[start] = aux_array[i]
        start += 1
    
def mergeSort(A, start, end):
    """ Merge sort implementation """
    if end <= start:
        return
    mid = (start + end) // 2
    mergeSort(A, start, mid)
    mergeSort(A, mid+1, end)

    merge(A, start, mid, end)
    


if __name__ == "__main__":
    test_cases = [[3, 5, 2, 7, 6], [1, 2, 1, 2], [-9, 8, 2, 0, 1.2], 
                    [8, 7, 6, 5, 4, 3, 2, 1], [1], []]
    for each in test_cases:
        mergeSort(each, 0, len(each) - 1)
        print(each)