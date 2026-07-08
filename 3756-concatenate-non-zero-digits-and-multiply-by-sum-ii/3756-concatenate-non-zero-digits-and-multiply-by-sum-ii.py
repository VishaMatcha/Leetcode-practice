class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pref_sum = [0] * (n + 1)
        pref_val = [0] * (n + 1)
        pref_cnt = [0] * (n + 1)
        
        p10 = [1] * (n + 1)
        for i in range(1, n + 1):
            p10[i] = (p10[i - 1] * 10) % MOD
            
        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                pref_sum[i + 1] = (pref_sum[i] + digit) % MOD
                pref_val[i + 1] = (pref_val[i] * 10 + digit) % MOD
                pref_cnt[i + 1] = pref_cnt[i] + 1
            else:
                pref_sum[i + 1] = pref_sum[i]
                pref_val[i + 1] = pref_val[i]
                pref_cnt[i + 1] = pref_cnt[i]
                
        ans = []
        for l, r in queries:
            s_sum = (pref_sum[r + 1] - pref_sum[l]) % MOD
            
            cnt_right = pref_cnt[r + 1]
            cnt_left = pref_cnt[l]
            num_nonzero = cnt_right - cnt_left
            
            if num_nonzero == 0:
                ans.append(0)
                continue
                
            x = (pref_val[r + 1] - pref_val[l] * p10[num_nonzero]) % MOD
            
            ans.append((x * s_sum) % MOD)
            
        return ans