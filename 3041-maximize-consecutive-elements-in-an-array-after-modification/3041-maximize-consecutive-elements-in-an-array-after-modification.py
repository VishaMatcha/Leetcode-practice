class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0

        for x in nums:
            next_len = dp.get(x, 0) + 1
            same_len = dp.get(x - 1, 0) + 1

            dp[x + 1] = next_len
            dp[x] = same_len
            ans = max(ans, next_len, same_len)

        return ans