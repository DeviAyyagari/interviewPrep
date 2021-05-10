"""
Print Fibonacci series of a given n
Space complexity: O(n) - At any point in time, there are n activation records 
                            on the call stack
Time complexity: O(2^n) - The recursion tree has 1 node at the root level, 2 nodes
                            at level 1, 4 nodes at level 2, .... 2^i nodes at level i,
                            ....., 2^n nodes at level n.So th total complexity is
                            2^0 + 2^1 + 2^2 + ....... + 2^n ~ O(2^n)
"""
def fib(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    test_set = [0, 1, 2, 3, 4, 5, 6]
    for each in test_set:
        print(fib(each))