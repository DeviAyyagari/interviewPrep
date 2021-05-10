"""
Compute factorial of any integer
Factorial(n) is defined as n(n-1)(n-2).....1
Space complexity: O(n) - At any point in time, there are n activation records 
                            on the call stack
Time complexity: O(n) - The recursion tree has one node at each level, and there are
                            n levels in total.
"""
def factorial(n):
    if n < 0:
        print("Factorial cannot be computed for negative integers")
        return None
    
    if n == 0:
        return 0

    if n==1:
        return 1
    
    return n*factorial(n-1)

if __name__ == "__main__":
    test_set = [-10, 0, 1, 2, 3, 4, 5]
    for each in test_set:
        print(factorial(each))