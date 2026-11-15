class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        curr_sum = 0
        ans = 0
        
        for x in arr:
            curr_sum += x
            if curr_sum % 2 == 1:
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                ans = (ans + odd_count) % MOD
                even_count += 1
                
        return ans