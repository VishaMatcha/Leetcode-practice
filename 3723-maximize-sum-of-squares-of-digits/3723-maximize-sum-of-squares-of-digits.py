class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
            
        digits = []
        current_sum = sum
        
        for _ in range(num):
            d = min(9, current_sum)
            digits.append(str(d))
            current_sum -= d
            
        return "".join(digits)