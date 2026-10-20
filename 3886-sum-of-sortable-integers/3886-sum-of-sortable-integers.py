class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        divs = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divs.append(i)
                if i * i != n:
                    divs.append(n // i)
                    
        ans = 0
        for k in divs:
            valid = True
            prev_max = -float('inf')
            
            for start in range(0, n, k):
                end = start + k - 1
                drops = []
                for i in range(start, end + 1):
                    nxt = start + (i - start + 1) % k
                    if nums[i] > nums[nxt]:
                        drops.append(i)
                        
                if len(drops) > 1:
                    valid = False
                    break
                    
                if len(drops) == 1:
                    i = drops[0]
                    nxt = start + (i - start + 1) % k
                    min_val = nums[nxt]
                    max_val = nums[i]
                else:
                    min_val = nums[start]
                    max_val = nums[end]
                    
                if min_val < prev_max:
                    valid = False
                    break
                prev_max = max_val
                
            if valid:
                ans += k
                
        return ans