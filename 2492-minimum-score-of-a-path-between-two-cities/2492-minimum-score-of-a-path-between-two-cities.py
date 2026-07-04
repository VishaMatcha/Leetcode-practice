from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        
        min_score = float('inf')
        
        while queue:
            curr = queue.popleft()
            for neighbor, weight in adj[curr]:
                min_score = min(min_score, weight)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
        return min_score