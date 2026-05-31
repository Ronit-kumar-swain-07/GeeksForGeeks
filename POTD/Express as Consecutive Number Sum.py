# Express as Consecutive Number Sum

# Given a number n, find whether n can be expressed as sum of two or more consecutive positive numbers.

# Examples :
# Input: n = 10
# Output: true
# Explanation: 10 can be expressesd as 1 + 2 + 3 + 4.

# Input: n = 8
# Output: false
# Explanation: 8 can't be expressesd sum of two or more consecutive numbers.

# Input: n = 24
# Output: true
# Explanation: 24 can be expressesd as 7 + 8 + 9.

# Constraints:
# 1 ≤ n ≤ 109

# Expected Complexities
# Time Complexity: O(1)
# Auxiliary Space: O(1)

# Code
class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        return (n & (n-1)) != 0                           # Check Power of Two 