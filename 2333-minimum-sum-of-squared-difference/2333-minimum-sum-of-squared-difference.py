class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_diff = sum(diffs)
        
        k = k1 + k2
        if total_diff <= k:
            return 0
            
        max_d = max(diffs)
        freq = [0] * (max_d + 1)
        for d in diffs:
            freq[d] += 1
            
        for d in range(max_d, 0, -1):
            if freq[d] > 0:
                take = min(freq[d], k)
                freq[d] -= take
                freq[d - 1] += take
                k -= take
                if k == 0:
                    break
                    
        ans = 0
        for d in range(len(freq)):
            if freq[d] > 0:
                ans += freq[d] * (d ** 2)
                
        return ans