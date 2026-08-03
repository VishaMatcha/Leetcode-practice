class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp_1 = dp_2 = dp_3 = 0
        
        for i in range(n - 1, -1, -1):
            take_1 = stoneValue[i] - dp_1
            
            take_2 = float('-inf')
            if i + 1 < n:
                take_2 = stoneValue[i] + stoneValue[i+1] - dp_2
                
            take_3 = float('-inf')
            if i + 2 < n:
                take_3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp_3
                
            dp_current = max(take_1, take_2, take_3)
            
            dp_3 = dp_2
            dp_2 = dp_1
            dp_1 = dp_current
            
        if dp_1 > 0:
            return "Alice"
        elif dp_1 < 0:
            return "Bob"
        return "Tie"