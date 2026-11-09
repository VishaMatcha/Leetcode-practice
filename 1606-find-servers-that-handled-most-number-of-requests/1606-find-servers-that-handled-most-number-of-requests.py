class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []  
        available = SortedList(range(k))
        counts = [0] * k
        
        for i, (arr, ld) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                _, s_id = heapq.heappop(busy)
                available.add(s_id)
                
            if not available:
                continue
                
            preferred = i % k
            idx = available.bisect_left(preferred)
            if idx == len(available):
                idx = 0
                
            server_id = available[idx]
            available.remove(server_id)
            
            counts[server_id] += 1
            heapq.heappush(busy, (arr + ld, server_id))
            
        max_requests = max(counts)
        return [i for i, c in enumerate(counts) if c == max_requests]