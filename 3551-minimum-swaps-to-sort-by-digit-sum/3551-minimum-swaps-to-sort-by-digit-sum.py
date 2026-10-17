class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        
        val_to_target_idx = {val: i for i, val in enumerate(target)}
        
        visited = [False] * n
        cycles = 0
        
        for i in range(n):
            if not visited[i]:
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = val_to_target_idx[nums[curr]]
                cycles += 1
                
        return n - cycles