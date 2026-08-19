from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = {}
        
        for row, seat in reservedSeats:
            if row not in row_masks:
                row_masks[row] = 0
            row_masks[row] |= (1 << seat)
            
        ans = (n - len(row_masks)) * 2
        
        for mask in row_masks.values():
            if (mask & 60) == 0 and (mask & 960) == 0:
                ans += 2
            elif (mask & 60) == 0 or (mask & 960) == 0 or (mask & 240) == 0:
                ans += 1
                
        return ans