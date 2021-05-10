"""
Compute n^k
Space complexity: O(n) - At any point in time, there are n activation records 
                            on the call stack
Time complexity: O(n) - The recursion tree has one node at each level, and there are
                            n levels in total.
"""
def power(n, k):
    if k==1:
        return n
    
    return n*power(n, k-1)

if __name__ == "__main__":
    test_set = [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]
    for each in test_set:
        print(power(each[0], each[1]))