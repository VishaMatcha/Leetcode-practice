class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                v = lazy[node]
                mid = (l + r) // 2
                
                left = 2 * node
                lazy[left] = (lazy[left] + v) % MOD
                len_l = mid - l + 1
                tree_sq[left] = (tree_sq[left] + 2 * v * tree_sum[left] + v * v * len_l) % MOD
                tree_sum[left] = (tree_sum[left] + v * len_l) % MOD
                
                right = 2 * node + 1
                lazy[right] = (lazy[right] + v) % MOD
                len_r = r - mid
                tree_sq[right] = (tree_sq[right] + 2 * v * tree_sum[right] + v * v * len_r) % MOD
                tree_sum[right] = (tree_sum[right] + v * len_r) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sq[node] = (tree_sq[node] + 2 * v * tree_sum[node] + v * v * length) % MOD
                tree_sum[node] = (tree_sum[node] + v * length) % MOD
                lazy[node] = (lazy[node] + v) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, v)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, v)
                
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        last_seen = {}
        total_ans = 0
        
        for r in range(n):
            l = last_seen.get(nums[r], -1) + 1
            update(1, 0, n - 1, l, r, 1)
            last_seen[nums[r]] = r
            total_ans = (total_ans + tree_sq[1]) % MOD
            
        return total_ans