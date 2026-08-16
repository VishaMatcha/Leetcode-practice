class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        freq = {}
        
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            
            # Shrink the window if a character appears more than twice
            while freq[char] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
                
            # Record the maximum length of a valid window
            max_len = max(max_len, right - left + 1)
            
        return max_len