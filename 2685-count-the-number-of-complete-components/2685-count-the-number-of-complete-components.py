from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_count = 0
        
        for i in range(n):
            if visited[i]:
                continue
                
            component = []
            queue = [i]
            visited[i] = True
            
            for curr in queue:
                component.append(curr)
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        
            v_count = len(component)
            is_complete = True
            
            for node in component:
                if len(adj[node]) != v_count - 1:
                    is_complete = False
                    break
                    
            if is_complete:
                complete_count += 1
                
        return complete_count