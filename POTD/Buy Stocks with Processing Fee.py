class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0
        
        hold = -arr[0]
        res = 0
        
        for i in range(1, len(arr)):
            hold = max(hold, res - arr[i])
            res = max(res, hold + arr[i] - k)
        
        return res