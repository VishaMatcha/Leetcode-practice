class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurrence = {}
        left = 0
        max_length = 0
        for right, char in enumerate(s):
            if char in last_occurrence:
                left = max(left, last_occurrence[char] + 1)
            last_occurrence[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length  