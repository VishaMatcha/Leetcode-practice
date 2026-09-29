class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
            
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        
        for r in range(m):
            for c in range(n):
                if not dp[r][c]:
                    continue
                
                if c + 1 < n:
                    char = grid[r][c + 1]
                    for b in dp[r][c]:
                        nb = b + (1 if char == '(' else -1)
                        if nb >= 0:
                            dp[r][c + 1].add(nb)
                            
                if r + 1 < m:
                    char = grid[r + 1][c]
                    for b in dp[r][c]:
                        nb = b + (1 if char == '(' else -1)
                        if nb >= 0:
                            dp[r + 1][c].add(nb)
                            
        return 0 in dp[m - 1][n - 1]