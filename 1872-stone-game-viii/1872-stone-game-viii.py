from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        for i in range(1, n):
            stones[i] += stones[i-1]
            
        dp = stones[-1]
        
        for i in range(n-2, 0, -1):
            if stones[i] - dp > dp:
                dp = stones[i] - dp
                
        return dp