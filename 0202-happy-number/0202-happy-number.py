class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = square(n)

        return n == 1
            