"""
Check Subset sum divisible by k

Given an array arr[] of positive integers and a value k. Return true if the sum of any non-empty subset of the given array is divisible by k otherwise, return false.

Examples:

Input: arr[] = [3, 1, 7, 5] , k = 6
Output: true
Explanation: If we take the subset {7, 5} then sum will be 12 which is divisible by 6.
Input: arr[] = [1, 2, 6] , k = 5
Output: false
Explanation: All possible subsets of the given set are {1}, {2}, {6}, {1, 2}, {2, 6}, {1, 6} and {1, 2, 6}. There is no subset whose sum is divisible by 5.
Constraints:
1 ≤ arr.size(), k ≤ 103
1 ≤ arr[i] ≤ 103

Expected Complexities
Time Complexity: O(n*k)
Auxiliary Space: O(k)

"""

#Code
class Solution:
    def divisibleByK(self, arr, k):
        dp = [False] * k

        for num in arr:
            new_dp = dp[:]
            
            new_dp[num % k] = True
            
            for r in range(k):
                if dp[r]:
                    new_dp[(r + num) % k] = True

            dp = new_dp

            if dp[0]:
                return True

        return False