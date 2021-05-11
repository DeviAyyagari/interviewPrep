"""
Problem statement: Given a string with n distince characters, print all
                    permutations of the string.
Intuition: At the first level of recursive tree, there are n choices for the node
            to make. Each node passes down the partial solutions
            and the reduced "domain" to the child node.
            At the second level, each of the n nodes have (n-1) choices to make.
            Leaf nodes will have solution.
Space complexity: At any point in time only one leaf nodes' tree structure
                    resides on the call stack. The height of the tree is n.
                    Space complexity: O(n)
Time complexity: The recursive tree has  n + n(n-1) + n(n-1)(n-2) + ..... + n! nodes 
                    and every node except the leaf nodes do O(1) amount of work. 
                    There are n! leaf nodes and each leaf node does
                    O(n) work, because printing takes O(n) time. So, the 
                    asymptotic complexity is O(n*n!)
"""

def permutations(str_):
    permutations_helper("", str_)

def permutations_helper(slate, domain):
    if len(domain) == 0:
        print(slate)
        return

    for index in range(len(domain)):
        new_domain = domain[:index] + domain[index + 1:]
        permutations_helper(slate + domain[index], new_domain)

if __name__ == "__main__":
    test_set = ["abc", "xy", "x", "aaa"]
    for each in test_set:
        permutations(each)
