"""
Equal Point in Brackets

Given a string s of opening and closing brackets '(' and ')' only, find an equal point in the string. 
An equal point is a position k (0-based) such that the number of opening brackets before position k is equal to the number of, 
closing brackets from position k to the end of the string. If multiple such points exist, return the first valid position.

The string can be split at any position from 0 to n, where n is the length of the string.
If we split at 0, it means there is an empty string on left.
If we split at n, it means there is an empty string on right.

# Examples:

Input: s = "(())))("
Output: 4
Explanation:

Input : s = "))"
Output: 2
Explanation: After index 2, the string splits into "))" and an empty string. The number of opening brackets in the first part is 0 and the number of closing brackets in the second part is also 0.

# Constraints:
1 ≤ s.size() ≤ 105

# Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

"""

#Code
class Solution:
    def findIndex(self, s):
        n = len(s)
        opencnt = 0 
        closecnt = s.count(')')
                
        for i in range(n+1):
            if opencnt == closecnt:
                return i
            
            if i < n:
                if s[i] == '(':
                    opencnt += 1
                if s[i] == ')':
                    closecnt -= 1
        return -1