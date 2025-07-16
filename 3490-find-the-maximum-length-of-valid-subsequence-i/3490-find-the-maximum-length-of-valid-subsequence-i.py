class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = 0
        odd_count = 0
        alt_even = 0
        alt_odd = 0

        for num in nums:
            p = num % 2  

            if p == 0:
                even_count += 1           
                alt_even = alt_odd + 1    
            else:
                odd_count += 1            
                alt_odd = alt_even + 1    

        return max(even_count, odd_count, alt_even, alt_odd)