from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Compute prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i-1]
            
        # Base case: choosing the last available index (taking all remaining stones)
        dp = stones[-1]
        
        # Traverse backwards to calculate the DP
        # We stop at 1 because a player must choose x > 1 stones (i.e., at least index 1)
        for i in range(n-2, 0, -1):
            if stones[i] - dp > dp:
                dp = stones[i] - dp
                
        return dp