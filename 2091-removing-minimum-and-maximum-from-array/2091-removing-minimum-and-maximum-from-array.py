from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
            
        min_idx = 0
        max_idx = 0
        
        for k in range(1, n):
            if nums[k] < nums[min_idx]:
                min_idx = k
            if nums[k] > nums[max_idx]:
                max_idx = k
                
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        front_only = j + 1
        back_only = n - i
        both_ends = (i + 1) + (n - j)
        
        return min(front_only, back_only, both_ends)