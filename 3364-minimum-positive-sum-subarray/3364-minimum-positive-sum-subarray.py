class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        min_sum = float('inf')
        
        for i in range(n):
            for j in range(i + l - 1, min(n, i + r)):
                sub_sum = prefix[j + 1] - prefix[i]
                if sub_sum > 0:
                    min_sum = min(min_sum, sub_sum)
                    
        return min_sum if min_sum != float('inf') else -1