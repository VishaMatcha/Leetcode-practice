class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if j == 0 or j == i:
                    c[i][j] = 1
                else:
                    c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD
                    
        def dfs(subnums):
            if len(subnums) <= 2:
                return 1
            root = subnums[0]
            left = [x for x in subnums[1:] if x < root]
            right = [x for x in subnums[1:] if x > root]
            
            l_res = dfs(left)
            r_res = dfs(right)
            
            return c[len(subnums) - 1][len(left)] * l_res % MOD * r_res % MOD
            
        return (dfs(nums) - 1) % MOD