class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
        bars_bought = 0
        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue
            if coins < price:
                break
            count_to_buy = min(freq[price], coins // price)
            bars_bought += count_to_buy
            coins -= count_to_buy * price
            if coins < price:
                break
        return bars_bought