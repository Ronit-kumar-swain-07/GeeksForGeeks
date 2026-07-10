"""
Ways to Express as Sum of Consecutives

Given a number n, find the number of ways to represent this number as a sum of 2 or more consecutive natural numbers.

Examples:

Input: n = 10
Output: 1
Explanation: There is only one way, 10 = 1+2+3+4.

Input: n = 15
Output: 3
Explanation: There are 3 ways, (15 = 1+2+3+4+5), (15 = 4+5+6) and (15 = 7+8).

Constraints:
1 ≤ n ≤ 108

Expected Complexities
Time Complexity: O(sqrt(n))
Auxiliary Space: O(1)

"""

#Code
class Solution:
    def getCount(self, n):
        
        count = 0
        k = 2
        while True:
            baseSum = (k * (k - 1)) // 2
            if baseSum >= n:
                break 
            if (n - baseSum) % k == 0:
                count += 1
            
            k += 1

        return count