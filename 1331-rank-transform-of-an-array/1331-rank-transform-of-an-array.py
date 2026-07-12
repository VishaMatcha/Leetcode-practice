class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {}
        for num in sorted(set(arr)):
            rank_map[num] = len(rank_map) + 1
        return [rank_map[num] for num in arr]