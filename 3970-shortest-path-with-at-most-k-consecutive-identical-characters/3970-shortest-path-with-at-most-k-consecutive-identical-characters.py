class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g= [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u][count]:
                continue
            for v, w in g[u]:
                nxt = 1 if labels[v] != labels[u] else count + 1
                if nxt <= k:
                    nd = d + w
                    if nd < dist[v][nxt]:
                    
                        dist[v][nxt] = nd
                        heapq.heappush(pq, (nd, v, nxt))
                        
        return -1