"""
C(n, k): Number of ways to choose k objects out of n, where repition is not 
allowed and order is not important. Mathematically, C(n, k) = n! / k!(n-k)!
Hint: To visualise the "no repitions" and "order not important" constraints,
think of the problem as "forming a committe of k students from a group of n
students. It does not make sense to pick the same student multiple times(No repitions),
or claim the subsets as "a,b,c" and "b,a,c" as different subsets(order not important).

Intuition: For every element, we either choose to include that element in the subset 
            OR exclude that element from the subset.
Space complexity: N activation records on the call stack. O(n)
Time complexity: The recursion tree has 1 node at the root level, 2 nodes
                            at level 1, 4 nodes at level 2, .... 2^i nodes at level i,
                            ....., 2^k nodes at level k.So th total complexity is
                            2^0 + 2^1 + 2^2 + ....... + 2^k ~ O(2^k)
"""
def C(n, k):
    if k==0 or k ==n:
        return 1
    
    return C(n - 1, k) + C(n-1, k-1)

if __name__ == "__main__":
    test_set = [(5,0), (5, 3), (5, 5)]
    for each in test_set:
        print(C(each[0], each[1]))