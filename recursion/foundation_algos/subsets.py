"""
How many subsets of a set of size n are there?
Intuition: For each element in the set, we have two choices. Include
            theat element in the subset or exclude that element from the subset.
            So, total no. of subsets of size n = 2^n = 2 * (2 ^ (n-1))
Space complexity: N activation records on the call stack. O(n)
Time complexity: The recursion tree has n lvels and one node at each level.
                    O(n)
"""
def subsets(n):
    if n == 0:
        return 1

    if n == 1:
        return 2
    
    return 2 * subsets(n-1)

if __name__ == "__main__":
    test_set = [0, 1, 2, 3, 4, 5, 6]
    for each in test_set:
        print(subsets(each))