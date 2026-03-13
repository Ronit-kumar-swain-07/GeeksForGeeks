# Generate IP Addresses

# Given a string s containing only digits, your task is to restore it by returning all possible valid IP address combinations. 
# You can return your answer in any order.

# A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255(inclusive).

# Note: The numbers cannot be 0 prefixed unless they are 0. For example, 1.1.2.11 and 0.11.21.1 are valid IP addresses,
# while 01.1.2.11 and 00.11.21.1 are not.
# If there are no possible valid IP address return an empty list. The driver code will print -1 in this case.

# Examples:

# Input: s = “255678166”
# Output: [“25.56.78.166”, “255.6.78.166”, “255.67.8.166”, “255.67.81.66”]
# Explanation: These are the only valid possible IP addresses.

# Input: s = “25505011535”
# Output: []
# Explanation: We cannot generate a valid IP address with this string.

# Constraints:
# 1 ≤ s.size() ≤ 16
# s contains only digits(i.e. 0-9)

# Expected Complexities
# Time Complexity: O(27*n)
# Auxiliary Space: O(n)

#Code
class Solution:
    def genIp(self, s):
        res = []
        def dfs(i, parts, cur):
            if parts == 4:
                if i == len(s):
                    res.append(".".join(cur))
                return
            for j in range(i, min(i+3, len(s))):
                p = s[i:j+1]
                if (p[0] == '0' and len(p) > 1) or int(p) > 255:
                    continue
                dfs(j+1, parts+1, cur+[p])
        dfs(0, 0, [])
        return res