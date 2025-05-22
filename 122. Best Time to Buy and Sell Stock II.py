class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for R in range(1, len(prices)):
            profit = prices[R] - prices[R - 1]
            if profit > 0:
                max_profit += profit
        return max_profit