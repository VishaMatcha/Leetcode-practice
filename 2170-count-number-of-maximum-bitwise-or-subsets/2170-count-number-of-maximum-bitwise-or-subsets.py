class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for v in nums:
            max_or |= v

        dp = {0: 1}
        for v in nums:
            for prev_or, cnt in list(dp.items()):
                new_or = prev_or | v
                dp[new_or] = dp.get(new_or, 0) + cnt
        return dp.get(max_or, 0)