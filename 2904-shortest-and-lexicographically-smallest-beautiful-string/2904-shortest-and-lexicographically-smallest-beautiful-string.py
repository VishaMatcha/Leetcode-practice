class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, char in enumerate(s) if char == '1']
        
        if len(ones) < k:
            return ""
            
        best_str = ""
        min_len = float('inf')
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start:end + 1]
            
            if len(sub) < min_len:
                min_len = len(sub)
                best_str = sub
            elif len(sub) == min_len:
                if sub < best_str:
                    best_str = sub
                    
        return best_str