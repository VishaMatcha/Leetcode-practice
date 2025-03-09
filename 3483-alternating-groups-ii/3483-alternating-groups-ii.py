class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n, current_count, result = len(colors), 1, 0
        
        # Loop up to n + k - 2 (circular array)
        for i in range(n + k - 2):
            if colors[i % n] != colors[(i + 1) % n]:
                current_count += 1
            else:
                current_count = 1
            
            result += (current_count >= k)
        
        return result