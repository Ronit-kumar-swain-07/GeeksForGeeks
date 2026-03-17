# Burning Tree

# Given the root of a binary tree and a target node, determine the minimum time required to burn the entire tree if the target node is set on fire. 
# In one second, the fire spreads from a node to its left child, right child, and parent.

# Note: The tree contains unique values.

# Examples : 

# Input: root = [1, 2, 3, 4, 5, 6, 7], target = 2
# Output: 3
# Explanation: Initially 2 is set to fire at 0 sec 
# At 1 sec: Nodes 4, 5, 1 catches fire.
# At 2 sec: Node 3 catches fire.
# At 3 sec: Nodes 6, 7 catches fire.
# It takes 3s to burn the complete tree.

# Input: root = [1, 2, 3, 4, 5, N, 7, 8, N, N, 10], target = 10
# Output: 5
# Explanation: Initially 10 is set to fire at 0 sec 
# At 1 sec: Node 5 catches fire.
# At 2 sec: Node 2 catches fire.
# At 3 sec: Nodes 1 and 4 catches fire.
# At 4 sec: Node 3 and 8 catches fire.
# At 5 sec: Node 7 catches fire.
# It takes 5s to burn the complete tree.

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
from collections import deque

class Solution:
    def minTime(self, root, target):
        parent = {}
        q = deque([root])
        target_node = None
        while q:
            node = q.popleft()
            if node.data == target:
                target_node = node
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        visited = {target_node}
        q = deque([target_node])
        time = -1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left, node.right, parent.get(node)):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            time += 1
        return time