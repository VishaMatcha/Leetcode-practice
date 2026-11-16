class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_groups = []
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                digit_sum = sum(int(ch) for ch in chunk)
                new_groups.append(str(digit_sum))
            s = "".join(new_groups)
        return s      