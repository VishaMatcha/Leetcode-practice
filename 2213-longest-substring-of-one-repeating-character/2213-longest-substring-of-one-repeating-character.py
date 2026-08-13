from typing import List

class SegTree:
    def __init__(self, s: str):
        self.n = len(s)
        # Allocate flat arrays for segment tree nodes to maximize Python performance
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.pref_char = [''] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.suff_char = [''] * (4 * self.n)
        self.size = [0] * (4 * self.n)
        
        self.s = s
        self.build(1, 0, self.n - 1)

    def merge(self, node: int, left: int, right: int):
        self.size[node] = self.size[left] + self.size[right]
        self.pref_char[node] = self.pref_char[left]
        self.suff_char[node] = self.suff_char[right]
        
        # Calculate prefix properties
        if self.pref_len[left] == self.size[left] and self.pref_char[left] == self.pref_char[right]:
            self.pref_len[node] = self.size[left] + self.pref_len[right]
        else:
            self.pref_len[node] = self.pref_len[left]
            
        # Calculate suffix properties
        if self.suff_len[right] == self.size[right] and self.suff_char[right] == self.suff_char[left]:
            self.suff_len[node] = self.size[right] + self.suff_len[left]
        else:
            self.suff_len[node] = self.suff_len[right]
            
        # Calculate max properties
        self.max_len[node] = max(self.max_len[left], self.max_len[right])
        if self.suff_char[left] == self.pref_char[right]:
            self.max_len[node] = max(self.max_len[node], self.suff_len[left] + self.pref_len[right])

    def build(self, node: int, start: int, end: int):
        if start == end:
            c = self.s[start]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.pref_char[node] = c
            self.suff_len[node] = 1
            self.suff_char[node] = c
            self.size[node] = 1
            return
        
        mid = (start + end) // 2
        left = 2 * node
        right = 2 * node + 1
        
        self.build(left, start, mid)
        self.build(right, mid + 1, end)
        self.merge(node, left, right)

    def update(self, node: int, start: int, end: int, idx: int, val: str):
        if start == end:
            self.pref_char[node] = val
            self.suff_char[node] = val
            return
        
        mid = (start + end) // 2
        left = 2 * node
        right = 2 * node + 1
        
        if idx <= mid:
            self.update(left, start, mid, idx, val)
        else:
            self.update(right, mid + 1, end, idx, val)
            
        self.merge(node, left, right)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = SegTree(s)
        ans = []
        
        for idx, char in zip(queryIndices, queryCharacters):
            tree.update(1, 0, tree.n - 1, idx, char)
            ans.append(tree.max_len[1])
            
        return ans