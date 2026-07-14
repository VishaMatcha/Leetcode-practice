from math import gcd
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def dp(i: int, g1: int, g2: int) -> int:
            if i == n:
                return 1 if (g1 > 0 and g1 == g2) else 0
                
            num = nums[i]
            
            res = dp(i + 1, g1, g2)
            
            new_g1 = num if g1 == 0 else gcd(g1, num)
            res = (res + dp(i + 1, new_g1, g2)) % MOD
            
            new_g2 = num if g2 == 0 else gcd(g2, num)
            res = (res + dp(i + 1, g1, new_g2)) % MOD
            
            return res
            
        return dp(0, 0, 0)