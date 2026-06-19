class Solution:
    def countStrings(self, n):
        a, b = 0, 1
        
        for _ in range(n + 2):
            a, b = b, a + b
        return a