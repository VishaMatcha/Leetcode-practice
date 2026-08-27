from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        avail = Counter(s)
        n = len(s)
        m = 0
        while m < n and avail[target[m]] > 0:
            avail[target[m]] -= 1
            m += 1
            
        i = min(m, n - 1)
        if m == n:
            avail[target[n - 1]] += 1
            i = n - 1
            
        while i >= 0:
            valid = [c for c in avail if c > target[i] and avail[c] > 0]
            if valid:
                best_c = min(valid)
                avail[best_c] -= 1
                ans = [target[:i], best_c]
                for c in sorted(avail.keys()):
                    ans.append(c * avail[c])
                return "".join(ans)
            
            if i > 0:
                avail[target[i - 1]] += 1
            i -= 1
            
        return ""