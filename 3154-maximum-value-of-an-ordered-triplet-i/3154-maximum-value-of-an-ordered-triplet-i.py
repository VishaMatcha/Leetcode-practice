class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        i = nums[0]
        for j in range (1,n):
            if nums[j]>i:
                i = nums[j]
            for k in range (j+1, n):
                res = max(res, ((i-nums[j])*nums[k]))
        return res