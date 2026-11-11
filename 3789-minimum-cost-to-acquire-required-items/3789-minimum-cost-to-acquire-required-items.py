class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2
            
        ans = float('inf')
        candidates = set([0, need1, need2, max(need1, need2)])
        
        for i in candidates:
            rem1 = max(0, need1 - i)
            rem2 = max(0, need2 - i)
            cost = i * costBoth + rem1 * cost1 + rem2 * cost2
            ans = min(ans, cost)
                    
        return ans