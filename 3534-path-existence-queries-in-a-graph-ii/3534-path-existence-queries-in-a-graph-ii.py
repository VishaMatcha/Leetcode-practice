class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        if n == 0:
            return []
            
        sorted_nodes = sorted(range(n), key=lambda i: nums[i])
        sorted_nums = [nums[i] for i in sorted_nodes]
        
        pos_map = [0] * n
        for i, node in enumerate(sorted_nodes):
            pos_map[node] = i
            
        max_level = n.bit_length() + 1
        jump = [[0] * max_level for _ in range(n)]
        
        right = 0
        for i in range(n):
            while right + 1 < n and sorted_nums[right + 1] - sorted_nums[i] <= maxDiff:
                right += 1
            jump[i][0] = right
            
        for level in range(1, max_level):
            for i in range(n):
                jump[i][level] = jump[jump[i][level - 1]][level - 1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            pu = pos_map[u]
            pv = pos_map[v]
            
            if pu > pv:
                pu, pv = pv, pu
                
            if jump[pu][max_level - 1] < pv:
                ans.append(-1)
                continue
                
            steps = 0
            curr = pu
            for level in range(max_level - 1, -1, -1):
                if jump[curr][level] < pv:
                    curr = jump[curr][level]
                    steps += (1 << level)
                    
            ans.append(steps + 1)
            
        return ans