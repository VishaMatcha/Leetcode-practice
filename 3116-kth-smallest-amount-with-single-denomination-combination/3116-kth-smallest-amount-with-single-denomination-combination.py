import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(list(set(coins)))
        filtered_coins = []
        for c in coins:
            if not any(c % f == 0 for f in filtered_coins):
                filtered_coins.append(c)
                
        high = filtered_coins[0] * k
        pie_lcms = []
        
        def dfs(idx, curr_lcm, cnt):
            if idx == len(filtered_coins):
                if cnt > 0:
                    sign = 1 if cnt % 2 == 1 else -1
                    pie_lcms.append((curr_lcm, sign))
                return
            
            dfs(idx + 1, curr_lcm, cnt)
            
            nlcm = math.lcm(curr_lcm, filtered_coins[idx])
            if nlcm <= high:
                dfs(idx + 1, nlcm, cnt + 1)
                
        dfs(0, 1, 0)
        
        def count_amounts(x):
            res = 0
            for lcm_val, sign in pie_lcms:
                res += sign * (x // lcm_val)
            return res

        low = 1
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans