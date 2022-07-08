class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            daily_profit = prices[i] - prices[i-1]
            current_profit = max(current_profit + daily_profit, daily_profit)
            max_profit = max(max_profit, current_profit)
        return max_profit