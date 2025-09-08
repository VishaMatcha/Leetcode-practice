class Solution:
    def rob(self, nums: List[int]) -> int:
        def linear_rob(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        n=len(nums)
        if n ==0:
            return 0
        elif(n==1):
            return nums[0]
        return max(linear_rob(nums[:-1]),linear_rob(nums[1:]))