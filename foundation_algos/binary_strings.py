"""
Problem statement: Enumerate all binary strings of length n
Intuition: Every node in the recursive tree gets the domain of the subproblem(in 
            this case size n for level 0, n-1 for level 1 ..... 0 for level n) 
            and the partial solution computed by its parents so far. 
            The leaf nodes have the complete solution.
Space complexity: At any point in time only ine leaf nodes' tree structure
                    resides on the call stack. The height of the tree is n.
                    Space complexity: O(n)
Time complexity: The recursive tree has 2^n nodes and every node except the 
                    leaf node does O(1) amount of work. the leaf nodes do
                    O(n) work, because printing takes O(n) times. So, the 
                    asymptotic complexity is O(n*2^n)
"""

def enumerate_binary_strings(slate, n):
    if n==0:
        print(slate)
        return

    enumerate_binary_strings(slate + str(0), n-1)
    enumerate_binary_strings(slate + str(1), n-1)

if __name__ == "__main__":
    test_set = [2, 3]
    for each in test_set:
        enumerate_binary_strings("", each)
