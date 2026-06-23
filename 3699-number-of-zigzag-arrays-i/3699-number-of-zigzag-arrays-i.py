class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        dp_inc = [0] * (M + 1)
        dp_dec = [0] * (M + 1)
        for v in range(1, M + 1):
            dp_inc[v] = v - 1
            dp_dec[v] = M - v
        for i in range(3, n + 1):
            next_inc = [0] * (M + 1)
            next_dec = [0] * (M + 1)  
            pref_dec = 0
            for v in range(1, M + 1):
                pref_dec = (pref_dec + dp_dec[v - 1]) % MOD
                next_inc[v] = pref_dec   
            suff_inc = 0
            for v in range(M, 0, -1):
                if v < M:
                    suff_inc = (suff_inc + dp_inc[v + 1]) % MOD
                next_dec[v] = suff_inc
            dp_inc = next_inc
            dp_dec = next_dec
        total_valid = (sum(dp_inc) + sum(dp_dec)) % MOD
        return total_valid