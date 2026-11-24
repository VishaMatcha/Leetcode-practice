class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                val = nums[j]
                prod *= val
                g = val if g == 0 else math.gcd(g, val)
                l = math.lcm(l, val)

                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans