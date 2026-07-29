import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        mid_char = ""
        half_counts = {}
        
        for char, count in counts.items():
            if count % 2 != 0:
                mid_char = char
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        L = sum(half_counts.values())
        
        total_ways = math.factorial(L)
        for cnt in half_counts.values():
            total_ways //= math.factorial(cnt)
            
        if k > total_ways:
            return ""
            
        k -= 1
        left_half = []
        sorted_chars = sorted(half_counts.keys())
        
        for _ in range(L):
            for char in sorted_chars:
                if half_counts[char] == 0:
                    continue
                
                ways = total_ways * half_counts[char] // L
                
                if k < ways:
                    left_half.append(char)
                    half_counts[char] -= 1
                    total_ways = ways
                    L -= 1
                    break
                else:
                    k -= ways
                    
        res_left = "".join(left_half)
        
        return res_left + mid_char + res_left[::-1]