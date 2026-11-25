class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = (1 << 61) - 1
        BASE = 1315423911

        def has_unique(length: int) -> bool:
            if length > n:
                return False

            power = pow(BASE, length - 1, MOD)
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD

            counts = Counter([h])
            for i in range(length, n):
                out_val = (nums[i - length] * power) % MOD
                h = (h - out_val + MOD) % MOD
                h = (h * BASE + nums[i]) % MOD
                counts[h] += 1

            return any(cnt == 1 for cnt in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans