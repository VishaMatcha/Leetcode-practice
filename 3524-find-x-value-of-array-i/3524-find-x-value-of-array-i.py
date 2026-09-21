class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            newDp = [0] * k
            numMod = num % k
            newDp[numMod] = 1            
            for i in range(k):
                new_mod = (i * numMod) % k
                newDp[new_mod] += dp[i]
            for i in range(k):
                ans[i] += newDp[i]
            dp = newDp
        return ans