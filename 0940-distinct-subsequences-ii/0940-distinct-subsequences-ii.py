class Solution:
    def distinctSubseqII(self, s: str) -> int:
        end = [0] * 26
        MOD = 10**9 + 7
        total = 0
        
        for char in s:
            idx = ord(char) - 97
            added = (total + 1) % MOD
            total = (total + added - end[idx]) % MOD
            end[idx] = added
            
        return total