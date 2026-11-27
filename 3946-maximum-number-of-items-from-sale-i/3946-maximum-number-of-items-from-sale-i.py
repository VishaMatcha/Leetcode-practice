class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n
        min_price = items[0][1]

        for i in range(n):
            fi, pi = items[i]
            if pi < min_price:
                min_price = pi
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)
        for i in range(n):
            price = items[i][1]
            val = 1 + bonus[i]
            for b in range(budget, price - 1, -1):
                candidate = dp[b - price] + val
                if candidate > dp[b]:
                    dp[b] = candidate

        ans = 0
        for b in range(budget + 1):
            total = dp[b] + (budget - b) // min_price
            if total > ans:
                ans = total

        return ans