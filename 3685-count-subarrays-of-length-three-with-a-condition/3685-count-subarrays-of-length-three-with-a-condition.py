class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(2*(nums[i-1]+nums[i+1])==nums[i] for i in range(1, len(nums)-1))