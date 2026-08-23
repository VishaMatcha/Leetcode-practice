class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        L = 0
        R = 0
        Q_L = 0
        Q_R = 0
        
        for i in range(mid):
            if num[i] == '?':
                Q_L += 1
            else:
                L += int(num[i])
                
        for i in range(mid, n):
            if num[i] == '?':
                Q_R += 1
            else:
                R += int(num[i])
                
        if (Q_L + Q_R) % 2 != 0:
            return True
            
        return (L - R) * 2 != (Q_R - Q_L) * 9