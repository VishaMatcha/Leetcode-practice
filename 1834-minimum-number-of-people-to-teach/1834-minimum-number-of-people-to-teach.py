class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        masks = [0]*(m+1)
        for i in range(m):
            mask = 0
            for lang in languages[i]:
                mask |= 1 << (lang-1)
            masks[i+1] = mask
        
        candidates = set()
        for u,v in friendships:
            if masks[u] & masks[v] == 0:
                candidates.add(u); candidates.add(v)
        if not candidates:
            return 0
        
        count = [0]*(n+1)
        for u in candidates:
            for lang in range(1,n+1):
                if masks[u] & (1 << (lang-1)):
                    count[lang]+=1
        maxOverlap = max(count)
        return len(candidates) - maxOverlap