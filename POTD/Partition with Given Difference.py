class Solution:
    def countPartitions(self, arr, diff):
        total = sum(arr)
        if (total + diff) % 2 != 0 or diff > total:
            return 0
        
        target = (total + diff) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]