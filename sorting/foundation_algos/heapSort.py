"""
Problem Statement: Sort an integer array in ascending order
Insertion sort: This is an out-of-place transform-and-conquer sorting algorithm. 
Intuition: Transform array to heap. The top element of the heap will be the 
            min element of the array. Keep popping until you pop all elements
            of the heap.
Time Complexity: Best case = O(nlogn); Average case = O(nlogn); Worst case = O(nlingn)
Space Complexity: O(n) # Anmol says it's possible to implement this in-place. ???
Stability: NOT stable
"""

import heapq

def heapSort(A):
    """ Heap sort implementation """

    heapq.heapify(A)
    return [heapq.heappop(A) for i in range(len(A))]


if __name__ == "__main__":
    test_cases = [[3, 5, 2, 7, 6], [1, 2, 1, 2], [-9, 8, 2, 0, 1.2], 
                    [8, 7, 6, 5, 4, 3, 2, 1], [1], []]
    for each in test_cases:
        sorted_ = heapSort(each)
        print(sorted_)