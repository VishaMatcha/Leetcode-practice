class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        
        curr_max = 0
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            prefix_gcd[i] = math.gcd(nums[i], curr_max)
            
        prefix_gcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_sum