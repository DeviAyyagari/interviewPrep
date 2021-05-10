"""
C(n, k): Number of ways to choose k objects out of n, where repition is not 
allowed and order is not important.
Space complexity:
Time complexity:
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