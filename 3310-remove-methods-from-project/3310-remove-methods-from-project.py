from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)
                    
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
                
        return [i for i in range(n) if not suspicious[i]]