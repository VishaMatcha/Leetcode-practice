from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        
        total_sum = sum(row_sums)
        
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        current_sum = 0
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True
                
        current_sum = 0
        for j in range(n - 1):
            current_sum += col_sums[j]
            if current_sum == target:
                return True
                
        return False