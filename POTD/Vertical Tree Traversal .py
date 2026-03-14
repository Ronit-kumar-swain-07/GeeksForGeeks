# Vertical Tree Traversal

# Given the root of a Binary Tree, find the vertical traversal of the tree starting from the leftmost level to the rightmost level.

# Note: If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

# Examples:

# Input: root = [1, 2, 3, 4, 5, 6, 7, N, N, N, 8, N, 9, N, 10, 11, N]
# Output: [[4], [2], [1, 5, 6, 11], [3, 8, 9], [7], [10]]
# Explanation: The below image shows the horizontal distances used to print vertical traversal starting from the leftmost level to the rightmost level.

# Input: root = [1, 2, 3, 4, 5, N, 6]
# Output: [[4], [2], [1, 5], [3], [6]]
# Explanation: From left to right the vertical order will be [[4], [2], [1, 5], [3], [6]]

# Constraints:
# 1 ≤ number of nodes ≤ 105
# 1 ≤ node->data ≤ 10

# Code
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        mp = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, hd = q.popleft()
            mp[hd].append(node.data)
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        ans = []
        for key in sorted(mp):
            ans.append(mp[key])
        return ans