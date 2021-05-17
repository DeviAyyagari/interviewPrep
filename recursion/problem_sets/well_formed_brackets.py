"""
Problem Statement: Given a positive integer n, return ALL strings of length 2*n 
                    with well formed round brackets.
"""

def brackets(n):

    result = []

    def helper(slate, left, right, index):
        
        if right > left:
            return

        # Base case
        if len(slate) == 2 * n:
            if left == right:
                result.append(slate)
            return

        helper(slate + "(", left+1, right, index + 1)
        helper(slate + ")", left, right + 1, index + 1)

    helper("", 0, 0, 0)
    return result

        

if __name__ == "__main__":
    n = 4
    print(brackets(n))