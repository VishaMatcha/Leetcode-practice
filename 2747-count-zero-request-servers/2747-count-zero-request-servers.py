class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        indexed_queries = sorted((q, i) for i, q in enumerate(queries))
        
        ans = [0] * len(queries)
        server_count = defaultdict(int)
        
        left = 0
        right = 0
        m = len(logs)
        
        for q, orig_idx in indexed_queries:
            start_time = q - x
            end_time = q
            
            while right < m and logs[right][1] <= end_time:
                server_count[logs[right][0]] += 1
                right += 1
                
            while left < m and logs[left][1] < start_time:
                s_id = logs[left][0]
                server_count[s_id] -= 1
                if server_count[s_id] == 0:
                    del server_count[s_id]
                left += 1
                
            ans[orig_idx] = n - len(server_count)
            
        return ans