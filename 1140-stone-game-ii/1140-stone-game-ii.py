from typing import List
from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @cache
        def dp(i: int, m: int) -> int:
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            max_stones = 0
            for x in range(1, 2 * m + 1):
                current_stones = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, current_stones)
                
            return max_stones
            
        return dp(0, 1)