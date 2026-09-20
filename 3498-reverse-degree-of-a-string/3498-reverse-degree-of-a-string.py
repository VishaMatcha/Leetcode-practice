class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for i, char in enumerate(s, 1):
            rev_val = 26 - (ord(char) - ord('a'))
            total_degree += rev_val * i
            
        return total_degree