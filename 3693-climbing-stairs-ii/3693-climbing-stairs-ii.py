class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(max(0, i - 3), i):
                cost = dp[j] + costs[i - 1] + (i - j) ** 2
                if cost < dp[i]:
                    dp[i] = cost
                    
        return dp[n]