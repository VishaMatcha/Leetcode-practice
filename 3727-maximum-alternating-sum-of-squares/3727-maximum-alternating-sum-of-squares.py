class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        mid = n // 2
        
        s1 = sum(x * x for x in nums[:mid])
        s2 = sum(x * x for x in nums[mid:])
        
        return s2 - s1