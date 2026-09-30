class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        d = 0
        for char in seq:
            if char == '(':
                ans.append(d % 2)
                d += 1
            else:
                d -= 1
                ans.append(d % 2)
        return ans