"""
Problem Statement: Given a set S of n distinct numbers, print all its subsets.
Intuition: In the recursive tree, at root node, you choose to either include the
            element or exclude the element from the subset. There are 2 choices to make for every 
            node at every level. Every node at every level is a valid solution.
            
NOTE: In the case of permuations, the root node will have n choices to make and the number of
        choices that can be made by nodes at subsequent levels decreases as height increases.

Time Complexity: There are 2 nodes at level 1, 2^2 nodes at level 2, ...., 2^n nodes
                    at level n. Total number of nodes = 2 + 2^2 + 2^3 + .... + 2^n ~ O(n).
                    Every node at every level performs O(n) work(printing). Total complexity
                    ~ O(n * 2^n)
Space Complexity: At any point in time only one leaf nodes' tree structure
                    resides on the call stack. The height of the tree is n.
                    Space complexity: O(n)
"""

def print_combinations(numbers):
    print_combinations_helper("", numbers)

def print_combinations_helper(slate, domain):
    if len(domain) == 0:
        print(slate)
        return
    
    
    index = len(domain) - 1
    new_domain = domain[:index] + domain[index + 1:]
    print_combinations_helper(slate + str(domain[index]), new_domain)
    print_combinations_helper(slate, new_domain)
 

if __name__ == "__main__":
    test_set = [[1], [1, 2], [1,2,3]]
    for each in test_set:
        print_combinations(each)