# Top View of Binary Tree

# You are given the root of a binary tree, and your task is to return its top view. 
# The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

# Note:
# Return the nodes from the leftmost node to the rightmost node.
# If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view.

# Examples:

# Input: root = [1, 2, 3]
# Output: [2, 1, 3]
# Explanation: The Green colored nodes represents the top view in the below Binary tree.

# Input: root = [10, 20, 30, 40, 60, 90, 100]
# Output: [40, 20, 10, 30, 100]
# Explanation: The Green colored nodes represents the top view in the below Binary tree.


# Constraints:
# 1 ≤ number of nodes ≤ 105
# 1 ≤ node->data ≤ 105

# Code
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        mp = {}
        def dfs(node, hd, level):
            if not node:
                return
            if hd not in mp or level < mp[hd][1]:
                mp[hd] = (node.data, level)
            dfs(node.left, hd - 1, level + 1)
            dfs(node.right, hd + 1, level + 1)
        dfs(root, 0, 0)
        res = []
        for hd in sorted(mp):
            res.append(mp[hd][0])
        return res