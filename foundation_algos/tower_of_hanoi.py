"""
Problem statement: Refer https://en.wikipedia.org/wiki/Tower_of_Hanoi
Space complexity: There could be anywhere between 1 and n activation records 
                    on the call stack. O(n)
Time complexity: The recursion tree has 1 node at the root level, 2 nodes
                            at level 1, 4 nodes at level 2, .... 2^i nodes at level i,
                            ....., 2^n nodes at level n.So th total complexity is
                            2^0 + 2^1 + 2^2 + ....... + 2^n ~ O(2^n)
"""

def tower_of_hanoi(n, src, dst, aux):
    if n==1:
        print("Move {} from {} to {}".format(n, src, dst))
        return

    tower_of_hanoi(n-1, src, aux, dst)
    print("Move {} from {} to {}".format(n, src, dst))
    tower_of_hanoi(n-1, aux, dst, src)

if __name__ == "__main__":
    test_set = 3
    tower_of_hanoi(test_set, "A", "B", "C")
