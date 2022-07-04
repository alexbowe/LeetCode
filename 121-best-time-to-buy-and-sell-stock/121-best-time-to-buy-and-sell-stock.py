class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0
        for i in range(1, len(prices)):
            day_profit = prices[i] - prices[i-1]
            current_profit = max(day_profit, current_profit+day_profit)
            max_profit = max(max_profit, current_profit)
        return max_profit
            
            