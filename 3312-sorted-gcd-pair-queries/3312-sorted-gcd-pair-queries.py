from bisect import bisect_right
from itertools import accumulate

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        
        count_divisors = [0] * (max_num + 1)
        for num in nums:
            count_divisors[num] += 1
            
        for i in range(1, max_num + 1):
            for j in range(2 * i, max_num + 1, i):
                count_divisors[i] += count_divisors[j]
                
        count_gcd_pairs = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            total_pairs = count_divisors[g] * (count_divisors[g] - 1) // 2
            
            for multiple in range(2 * g, max_num + 1, g):
                total_pairs -= count_gcd_pairs[multiple]
                
            count_gcd_pairs[g] = total_pairs
            
        prefix_sums = list(accumulate(count_gcd_pairs))
        
        return [bisect_right(prefix_sums, q) for q in queries]