from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        all_zero = True
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                all_zero = False
                
        if all_zero:
            return 0
            
        if total_xor != 0:
            return len(nums)
            
        return len(nums) - 1