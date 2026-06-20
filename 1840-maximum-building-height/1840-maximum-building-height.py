class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            
        m = len(restrictions)
        
        for i in range(1, m):
            id_prev, h_prev = restrictions[i - 1]
            id_curr, h_curr = restrictions[i]
            restrictions[i][1] = min(h_curr, h_prev + (id_curr - id_prev))
            
        for i in range(m - 2, -1, -1):
            id_curr, h_curr = restrictions[i]
            id_next, h_next = restrictions[i + 1]
            restrictions[i][1] = min(h_curr, h_next + (id_next - id_curr))
            
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            current_max = (h1 + h2 + (id2 - id1))  // 2
            max_height = max(max_height, current_max)
            
        return max_height