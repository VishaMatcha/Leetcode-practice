class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        if not ones1 or not ones2:
            return 0
            
        vector_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                vector_counts[(r2 - r1, c2 - c1)] += 1
                
        return max(vector_counts.values())