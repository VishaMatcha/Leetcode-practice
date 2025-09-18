class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10
            return total_sum

        slow = n
        fast = square(n)
        while (fast!=1 and slow!=fast):
            slow = square(slow)
            fast = square(square(fast))

        return fast == 1