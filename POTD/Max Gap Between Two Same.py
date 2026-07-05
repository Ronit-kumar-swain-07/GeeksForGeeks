"""
Max Gap Between Two Same

Given a string s consisting of lowercase English letters, find the maximum number of characters between any two identical characters. 
If no character repeats, return -1.

Examples :

Input: s = "socks"
Output: 3
Explanation: There are 3 characters between the two occurrences of 's'.

Input: s = "for"
Output: -1
Explanation: No repeating character present.

Constraints:
1 ≤ |s| ≤ 105

Expected Complexities
Time Complexity: O(|s|)
Auxiliary Space: O(1)

"""

#Code
class Solution:

    def maxCharGap(self, s: str) -> int:
        first = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch in first:
                ans = max(ans, i - first[ch] - 1)
            else:
                first[ch] = i

        return ans
