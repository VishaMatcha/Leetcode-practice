class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        li = []
        for i in range (0,len(weights)-1):
            li.append(weights[i+1]+weights[i])
        li.sort()
        i=k-1
        max_d = sum(li[-i:])
        min_d = sum(li[:i])
        return max_d-min_d