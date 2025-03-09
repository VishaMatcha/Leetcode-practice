class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        if k == 0 or k > n:
            return 0
        
        current_w = 0
        for i in range(k):
            if blocks[i] == 'W':
                current_w += 1
        min_ops = current_w
        
        for i in range(k, n):
            outgoing = blocks[i - k]
            if outgoing == 'W':
                current_w -= 1
            incoming = blocks[i]
            if incoming == 'W':
                current_w += 1
            if current_w < min_ops:
                min_ops = current_w
        
        return min_ops