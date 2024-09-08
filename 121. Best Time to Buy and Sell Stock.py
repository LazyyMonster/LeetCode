class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            p = prices[i]
            profit = max(profit, p - minimum)
            minimum = min(minimum, p)

        return profit