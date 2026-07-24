class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        pairs = {x ^ y for x in unique_nums for y in unique_nums}
        return len({p ^ c for p in pairs for c in unique_nums})