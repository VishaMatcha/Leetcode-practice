class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        transformed = [1 if x == target else -1 for x in nums]
        
        valid_subarrays = 0
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += transformed[end]
                if current_sum > 0:
                    valid_subarrays += 1
                    
        return valid_subarrays