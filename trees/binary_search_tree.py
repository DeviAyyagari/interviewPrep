"""
Insert, Search
"""

from node import Node
from display_tree import display

def insert(root, k):
    """ Insert an elemnent into a tree"""
    if root is None:
        root.val = k
        return
    
    newNode = Node(k)

    prev = None
    curr = root

    # Find the leaf node to insert the key at. prev tracks the parent to establish 
    # relationships later
    while curr:
        if k == curr.val:
            print("val already exists")
            return
        elif k < curr.val:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right
    
    # Figure out if it has to be left child or right child
    if k < prev.val:
        prev.left = newNode
    else:
        prev.right = newNode
    
    return root

def search(root, target):
    """ return node if tearget exists in tree, else return None"""
    if root is None:
        return None
    
    curr = root
    while curr:
        if target == curr.val:
            return curr
        elif target < curr.val:
            curr = curr.left
        else:
            curr = curr.right
        
    return curr

def delete(root, target):
    if root == None:
        return None
    
    # Traverse the tree to find the target
    prev = None
    curr = root
    while curr:
        if target == curr.val:
            break   
        elif target < curr.val:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right
    

    # If target is a leaf node
    if curr.left is None and curr.right is None:
        # Deleting the only single node in the tree
        if prev == None:
            return None

        if prev.left is not None and prev.left.val == target:
            prev.left = None
        else:
            prev.right = None
        return root

    # If target has one child
    if curr.left is None or curr.right is None:
        if curr.left is not None:
            curr.val = curr.left.val
            curr.left = None
        else:
            curr.val = curr.right.val
            curr.right = None
        return root

    # If target has two children. Find successor of the element, swap the value of
    # the target with the value of the successor, delete the successor.
    #Successor = min element of right subtree

    successor = curr.right
    successor_prev = curr
    while successor.left is not None:
        successor_prev = successor
        successor = successor.left
    
    # Assign curr value to successor's value
    curr.val = successor.val
    # If successor is leaf node
    if successor.right is None and successor.left is None:
        if successor.val < successor_prev.val:
            successor_prev.left = None
        else:
            successor_prev.right = None
        return root
    
    # If successor has one child
    if successor.left is None or successor.right is None:
        if successor.left is not None:
            successor.val = successor.left.val
            successor.left = None
        else:
            successor.val = successor.right.val
            successor.right = None
        return root


def test():
    arr = [17, 88, 8, 32, 65, 97, 28, 54, 82, 93, 29, 76, 80]
    root = Node(44)

    # test insert
    for each in arr:
        root = insert(root, each)
    
    display(root)

    # test search
    search_key = 66
    node_ = search(root, search_key)
    print(node_.val if node_ else "{} does not exist in tree".format(search_key))

    delete_key = 80
    root = delete(root, delete_key)
    delete_key = 97
    root = delete(root, delete_key)
    delete_key = 65
    root = delete(root, delete_key)
    delete_key = 44
    root = delete(root, delete_key)
    display(root)


if __name__ == "__main__":
    test()
