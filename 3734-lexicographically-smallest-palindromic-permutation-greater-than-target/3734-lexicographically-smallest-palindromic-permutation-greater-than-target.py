from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        avail = Counter(s)
        odds = [ch for ch, count in avail.items() if count % 2 == 1]
        
        if len(odds) > 1:
            return ""
            
        mid = odds[0] if odds else ""
        
        half_counts = Counter()
        for ch, count in avail.items():
            if count // 2 > 0:
                half_counts[ch] = count // 2
                
        m = len(s) // 2
        t_half = target[:m]
        
        current_counts = Counter(half_counts)
        max_match = 0
        while max_match < m and current_counts[t_half[max_match]] > 0:
            current_counts[t_half[max_match]] -= 1
            max_match += 1
            
        for i in range(max_match, -1, -1):
            if i == m:
                P = t_half + mid + t_half[::-1]
                if P > target:
                    return P
            else:
                rem = Counter(half_counts)
                for j in range(i):
                    rem[t_half[j]] -= 1
                    
                valid_chars = [ch for ch in rem if rem[ch] > 0 and ch > t_half[i]]
                if valid_chars:
                    best_c = min(valid_chars)
                    rem[best_c] -= 1
                    
                    rest = []
                    for ch in sorted(rem.keys()):
                        rest.append(ch * rem[ch])
                        
                    new_half = t_half[:i] + best_c + "".join(rest)
                    return new_half + mid + new_half[::-1]
                    
        return ""