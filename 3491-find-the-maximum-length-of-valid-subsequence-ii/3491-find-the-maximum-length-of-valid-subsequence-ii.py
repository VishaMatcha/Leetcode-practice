class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        max_length = 2

        for target_mod in range(k):
            remainder_dp = [0] * k

            for num in nums:
                num_mod = num % k
                required_mod = (target_mod - num_mod + k) % k
                remainder_dp[num_mod] = remainder_dp[required_mod] + 1

            max_length = max(max_length, max(remainder_dp))

        return max_length