class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = sorted([(r, l, w, i) for i, (l, r, w) in enumerate(intervals)])
        
        ends = [interval[0] for interval in sorted_intervals]
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            r, l, w, idx = sorted_intervals[i - 1]
            
            p = bisect_left(ends, l)
            
            for c in range(1, 5):
                best = dp[i - 1][c]
                
                prev_neg_weight, prev_indices = dp[p][c - 1]
                cand_indices = tuple(sorted(prev_indices + (idx,)))
                cand = (prev_neg_weight - w, cand_indices)
                
                if cand < best:
                    best = cand
                    
                dp[i][c] = best
                
        return list(dp[n][4][1])