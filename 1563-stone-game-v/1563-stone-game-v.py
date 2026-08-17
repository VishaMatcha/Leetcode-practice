class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
            
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j+1] - prefix[i]
            
        dp = [[0] * n for _ in range(n)]
        max_L = [[0] * n for _ in range(n)]
        max_R = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_L[i][i] = stoneValue[i]
            max_R[i][i] = stoneValue[i]
            
        for i in range(n - 1, -1, -1):
            m = i - 1
            for j in range(i + 1, n):
                while m + 1 < j and get_sum(i, m + 1) * 2 <= get_sum(i, j):
                    m += 1
                    
                if m == i - 1:
                    dp[i][j] = max_R[i+1][j]
                else:
                    if get_sum(i, m) * 2 == get_sum(i, j):
                        dp[i][j] = max(max_L[i][m], max_R[m+1][j])
                    else:
                        val1 = max_L[i][m] if m >= i else 0
                        val2 = max_R[m+2][j] if m + 1 < j else 0
                        dp[i][j] = max(val1, val2)
                                        
                dp_val = dp[i][j]
                current_sum = get_sum(i, j)
                max_L[i][j] = max(max_L[i][j-1], current_sum + dp_val)
                max_R[i][j] = max(max_R[i+1][j], current_sum + dp_val)
                
        return dp[0][n-1]