class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        i = nums[0]
        for j in range (1,len(nums)):
            if nums[j] > i:
                i=nums[j]
            for k in range (j+1, len(nums)):
                res = max(res,(i-nums[j])*nums[k])
        return res