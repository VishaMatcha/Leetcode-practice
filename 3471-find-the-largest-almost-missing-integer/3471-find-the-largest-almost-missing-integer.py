class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = {}
        
        for i in range(len(nums) - k + 1):
            unique_in_subarray = set(nums[i:i+k])
            for num in unique_in_subarray:
                counts[num] = counts.get(num, 0) + 1
                
        res = -1
        for num, count in counts.items():
            if count == 1:
                res = max(res, num)
                
        return res