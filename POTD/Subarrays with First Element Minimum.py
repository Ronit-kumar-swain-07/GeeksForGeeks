# Subarrays with First Element Minimum

# You are given an integer array arr[ ]. Your task is to count the number of subarrays where the first element is the minimum element of that subarray.

# Note: A subarray is valid if its first element is not greater than any other element in that subarray.

# Examples:

# Input: arr[] = [1, 2, 1]
# Output: 5
# Explanation:
# All possible subarrays are:
# [1], [1, 2], [1, 2, 1], [2], [2, 1], [1]
# Valid subarrays are:
# [1], [1, 2], [1, 2, 1], [2], [1] -> total 5

# Input: arr[] = [1, 3, 5, 2]
# Output: 8
# Explanation:
# Valid subarrays are: [1], [1, 3], [1, 3, 5], [1, 3, 5, 2], [3], [3, 5], [5], [2] -> total 8

# Constraints:
# 1 ≤ arr.size() ≤ 5*104
# 1 ≤ arr[i] ≤ 105

# Code 
class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        ans = 0

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ans += (stack[-1] if stack else n) - i
            stack.append(i)

        return ans
        