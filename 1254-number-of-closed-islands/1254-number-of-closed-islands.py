class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(R):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][C - 1] == 0:
                dfs(r, C - 1)
                
        for c in range(C):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[R - 1][c] == 0:
                dfs(R - 1, c)
                
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)
                    
        return count