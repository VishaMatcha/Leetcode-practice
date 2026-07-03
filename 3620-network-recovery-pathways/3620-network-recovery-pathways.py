from collections import defaultdict, deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        unique_costs = sorted(list(set(cost for _, _, cost in edges)))
        
        adj = defaultdict(list)
        in_degree = [0] * n
        for u, vi, cost in edges:
            if online[u] and online[vi]:
                adj[u].append((vi, cost))
                in_degree[vi] += 1
                
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        while queue:
            curr = queue.popleft()
            topo_order.append(curr)
            for neighbor, _ in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        def isValid(min_allowed_cost: int) -> bool:
            min_cost = [float('inf')] * n
            min_cost[0] = 0
            
            for u in topo_order:
                if min_cost[u] == float('inf'):
                    continue
                for vi, cost in adj[u]:
                    if cost >= min_allowed_cost:
                        if min_cost[u] + cost < min_cost[vi]:
                            min_cost[vi] = min_cost[u] + cost
                            
            return min_cost[n - 1] <= k

        low = 0
        high = len(unique_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if isValid(unique_costs[mid]):
                ans = unique_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans