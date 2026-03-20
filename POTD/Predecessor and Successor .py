# Predecessor and Successor

# You are given the root of a BST and an integer key. You need to find the inorder predecessor and successor of the given key. 
# If either predecessor or successor is not found, then set it to NULL.

# Note: In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 

# Examples :

# Input: root = [50, 30, 70, 20, 40, 60, 80], key = 65
# Output: [60, 70]
# Explanation: In the given BST the inorder predecessor of 65 is 60 and inorder successor of 65 is 70.

# Input: root = [8, 1, 9, N, 4, N, 10, 3], key = 8
# Output: [4, 9]
# Explanation: In the given BST the inorder predecessor of 8 is 4 and inorder successor of 8 is 9.

# Constraints: 
# 1 ≤ no. of nodes ≤ 105
# 0 ≤ node->data ≤ 106
# 1 ≤ key ≤ 106

# Code
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    
    def leftM(self, node):
        while node.left:
            node = node.left
        return node
        
    def rightM(self, node):
        while node.right:
            node = node.right
        return node
        
    def findPreSuc(self, root, key):
        pre, suc = None, None
        curr = root
        
        while curr:
            if curr.data < key:
                pre = curr
                curr = curr.right
            elif curr.data > key:
                suc = curr
                curr = curr.left
            else:
                if curr.left:
                    pre = self.rightM(curr.left)
                if curr.right:
                    suc = self.leftM(curr.right)
                break
                
        return [pre, suc]