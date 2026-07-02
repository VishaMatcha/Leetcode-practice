from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        min_damage = [[float('inf')] * n for _ in range(m)]
        
        min_damage[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_damage = min_damage[r][c] + grid[nr][nc]
                    
                    if new_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = new_damage
                        queue.append((nr, nc))
                        
        return min_damage[m - 1][n - 1] < health