# K Sum Paths

# Given the root of a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k.

# Note: A path can start and end at any node within the tree but must always move downward (from parent to child).

# Examples:

# Input: root = [8, 4, 5, 3, 2, N, 2, 3, -2, N, 1], k = 7
# Output: 3
# Explanation: The following paths sum to k

# Input: root = [1, 2, 3], k = 3
# Output: 2 
# Explanation: The following paths sum to k

# Constraints:
# 1 ≤ number of nodes ≤ 104
# -100 ≤ node value ≤ 100
# -109 ≤ k ≤ 109

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
#Code
class Solution:
    def countAllPaths(self, root, k):
        prefix = {0: 1}
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.data
            count = prefix.get(curr_sum - k, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1
            return count
        return dfs(root, 0)