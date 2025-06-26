class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count_zeros = s.count('0')
        cnt = count_zeros  # All zeros can be taken

        # Try to include as many ones as possible from right to left
        val = 0
        power = 1
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                if val + power <= k:
                    val += power
                    cnt += 1
                # Else skip this '1'
            if power > k:
                break  # Further ones will exceed k anyway
            power <<= 1  # Multiply by 2 for next bit
        return cnt