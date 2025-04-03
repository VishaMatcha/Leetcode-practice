class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        t_m = nums[0]
        diff = 0
        res = 0 
        for i in range(1,len(nums)):
            res = max(res, diff*nums[i])
            diff = max(diff, t_m-nums[i])
            t_m = max(t_m, nums[i])
        return res