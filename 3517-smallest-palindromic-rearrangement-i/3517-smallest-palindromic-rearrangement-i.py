from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        left_half = []
        mid_char = ""
        
        for char in sorted(counts.keys()):
            if counts[char] % 2 != 0:
                mid_char = char
            left_half.append(char * (counts[char] // 2))
            
        first_half_str = "".join(left_half)
        
        return first_half_str + mid_char + first_half_str[::-1]