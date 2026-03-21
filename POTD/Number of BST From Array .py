# Number of BST From Array

# You are given an integer array arr[] containing distinct elements.

# Your task is to return an array where the ith element denotes the number of unique BSTs formed when arr[i] is chosen as the root.

# Examples :

# Input: arr[] = [2, 1, 3]
# Output: [1, 2, 2]
# Explanation: 

# Input: arr[] = [2, 1]
# Ouput: [1, 1]

# Constraints:
# 1 ≤ arr.size() ≤ 6
# 1 ≤ arr[i] ≤ 15

# Code

from math import comb

class Solution:
    def catalan(self, n):
        return comb(2*n, n) // (n+1)

    def countBSTs(self, arr):
        n = len(arr)
        res = []
        for root in arr:
            cnt_lft = sum(1 for x in arr if x < root)
            cnt_rit = sum(1 for x in arr if x > root)
            res.append(self.catalan(cnt_lft) * self.catalan(cnt_rit))
        return res